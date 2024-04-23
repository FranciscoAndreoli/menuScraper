from model.interfaces.IUberEatsScraper import IUberEatsScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from services.js_scripts.jsScripts import GET_HREFS_SCRIPT
from services.webDriverUtilities.web_driver_utilities import retryOperation
import re
import json

#La clase está implementando una interfaz IUberEatsScraper, lo cual indica qué métodos deben existir en la clase
class UberEatsScraper(IUberEatsScraper):

    def __init__(self, jsonManager, webLink, WebDriverManager):
        self.jsonManager = jsonManager
        self.webLink = webLink
        self.webDriverManager = WebDriverManager
        self.webDriverManager.navigateTo(self.webLink)
        self.menuJson = None
        self.itemDialog = None
        self.mainContent = self.getMainContent()
        if(self.mainContent):
            self.getMenuJSON()
            self.getStoreElements()
    
    def getMainContent(self):
        self.mainContent = self.webDriverManager.waitForPresenceOfElement(By.ID, 'main-content')
        return self.mainContent
                                                                                                        
    def getMenuJSON(self):
        try:
            jsonScript = self.webDriverManager.findElement(By.XPATH, ".//script[@type='application/ld+json']")
            jsonContentString = self.webDriverManager.getAttribute(jsonScript,'textContent')
            self.menuJson = json.loads(jsonContentString) #parse a JSON string and convert it into a Dictionary. 
            self.jsonManager.saveToFile(self.menuJson, "json3")

        except Exception as e:
            print(f"Error obteniendo application/ld+json: {e}")
            #self.webDriverManager.quit()

    def getStoreElements(self):
        unwantedTitles = ["Schedule pick-up", "Oops, something went wrong"]
        menuData = []
        sectionsElements = self.getSectionsElements()

        for sectionElement in sectionsElements:
            self.webDriverManager.scrollToElement(sectionElement)
            sectionData = self.getSectionData(sectionElement)
            itemsHrefElements = self.webDriverManager.getHrefLinks(sectionElement)
            print("Longitud: ", len(itemsHrefElements))
            print("SectionName: ", sectionData['Name'])
            itemsData = []
            originalWindow = self.webDriverManager.getCurrentWindowHandle()  # Store the original window handle

            for hrefItems in itemsHrefElements:
                self.itemDialog = self.tryOpenItemDialog(hrefItems, originalWindow, unwantedTitles)
                if self.itemDialog != None:
                    itemData = self.getItemData()
                    #print(f"itemData: {itemData}")

                    optionSetsElements = self.getOptionSetsElements()
                    optionSetsData = []

                    if(optionSetsElements is not None):
                        for optionSet in optionSetsElements: #optionSet li
                            optionSetData = self.getOptionSetData(optionSet)
                            optionSetItems = self.getOptionSetItemsData(optionSet)
                            optionSetData['MenuItemOptionSets'] = optionSetItems
                            optionSetsData.append(optionSetData)

                    itemData['MenuItemOptionSets'] = optionSetsData
                    itemsData.append(itemData)
    
                    self.webDriverManager.closeCurrentTab(originalWindow)

                else:
                    print(f"Failed to open correct dialog for href: {hrefItems}")
            
            sectionData['MenuItems'] = itemsData
            jsonprint = self.jsonManager.serialize(sectionData)
            print(f"SECTION: {jsonprint}")
           

        #self.webDriverManager.waitForPresenceOfAllElementsLocatedWithinElement(self.mainContent,By.XPATH,".//li[starts-with(@data-test, 'store-item')]")
        #featuredSectionElement = self.getFeaturedSection()
        #if(featuredSectionElement != None):
        #    featuredSectionName = self.getSectionName(featuredSectionElement)
        #    featuredSectionItems = self.getItemsFromFeaturedSection(featuredSectionElement)

        #menuItemsList = self.getMenuItems(GET_HREFS_SCRIPT)
        #self.jsonManager.saveToFile(menuItemsList, "TEST")
        #print("Items:", menuItemsList)

    def getSectionsElements(self):
        """Returns a list of sections elements"""
        featuredSectionElement = self.getFeaturedSection()
        if(featuredSectionElement is not None):
            featuredSectionClassName = self.webDriverManager.getAttribute(featuredSectionElement, "class")
            sectionContainer = self.webDriverManager.findElementWithinElement(self.mainContent, By.XPATH, f".//ul[not(ancestor::*[contains(@class, '{featuredSectionClassName}')])][./li]")
            sectionsElements = self.webDriverManager.findElementsWithinElement(sectionContainer, By.XPATH, "./li")
            sectionsElements.insert(0, featuredSectionElement)
        else:
            sectionContainer = self.webDriverManager.findElementWithinElement(self.mainContent, By.XPATH, ".//ul[./li]")
            sectionsElements = self.webDriverManager.findElementsWithinElement(sectionContainer, By.XPATH, "./li")

        return sectionsElements
    
    def getSectionData(self, sectionElement):
        sectionName = self.getSectionName(sectionElement)
        #sectionDescription = self.getSectionDescription()

        sectionData = { 'Name': sectionName,
                        'Description': None,
                        'MenuItems': []
                      }
        return sectionData
    
    def getOptionSetsElements(self):
        """Returns a list of Option Sets elements inside an item"""
        optionSetsContainer = self.webDriverManager.findElementWithinElement(self.itemDialog, By.XPATH, ".//ul")
        if(optionSetsContainer is not None):
            optionSetsElement = self.webDriverManager.findElementsWithinElement(optionSetsContainer, By.XPATH, "./li")
            return optionSetsElement
        else:
            return None
        
    

    @retryOperation(maxAttempts=5, delay=1)
    def isCorrectDialog(self, unwantedTitles):
        unwantedSubstring = "Opens"
        dialogElement = self.webDriverManager.waitForPresenceOfElement(By.CSS_SELECTOR, '[role="dialog"]')
        self.webDriverManager.waitForLocatedElementToBeVisible(dialogElement)
        self.webDriverManager.waitForOpacity(dialogElement)

        textElements = self.webDriverManager.findElementsWithinElement(dialogElement, By.XPATH, ".//*[not(self::script) and not(self::style) and normalize-space(text())]")
        textContents = [element.text.strip() for element in textElements]

        for text in textContents:
            if text in unwantedTitles or unwantedSubstring in text:
                return None

        return dialogElement

    def tryOpenItemDialog(self, href, originalWindow, unwantedTitles):
        for attempt in range(5):
            self.webDriverManager.openNewTab(href)
            dialogElement = self.isCorrectDialog(unwantedTitles)
            if dialogElement != None:
                return dialogElement
            self.webDriverManager.closeCurrentTab(originalWindow)
        return None       
    
    @retryOperation(maxAttempts=5, delay=1)
    def getFeaturedSection(self):
        featuredSectionElement = self.webDriverManager.findElement(By.XPATH, "//main[@id='main-content']/div/li")
        
        return featuredSectionElement

    def getSectionName(self, element):
        sectionName = self.webDriverManager.findElementWithinElement(element, By.CSS_SELECTOR, 'h3')

        return sectionName.text
    
    @retryOperation(maxAttempts=5, delay=1)
    def getItemData(self):
        itemNameElement = self.getItemNameElement()
        itemNameText = itemNameElement.text
        itemPrice = self.getItemPrice()
        parentElement = self.webDriverManager.getParentElement(itemNameElement)
        if parentElement:
            itemDescription = self.getItemDescription(parentElement)
        else:
            itemDescription = None

        itemData = {
            'Name': itemNameText, 
            'Price': itemPrice,
            'Description': itemDescription,
            'MenuItemOptionSets': []
        }

        return itemData
        

    @retryOperation(maxAttempts=5, delay=1)
    def getItemNameElement(self):
        itemNameElement = self.webDriverManager.waitForPresenceOfElementWithinElement(self.itemDialog, By.CSS_SELECTOR, 'h1')
        if(itemNameElement is not None):
            return itemNameElement
        else:
            return None
    
    @retryOperation(maxAttempts=5, delay=1)
    def getItemPrice(self):
        itemPriceElement = self.webDriverManager.waitForPresenceOfElementWithinElement(self.itemDialog, By.CSS_SELECTOR, 'span[data-testid="rich-text"]')
        if(itemPriceElement is not None):
            priceText = itemPriceElement.text

            priceNumber = self.formatPrice(priceText)
            return priceNumber
        else:
            return 0.00
            
                
    def formatPrice(self, priceText):
        try:
            priceText = priceText.replace("€", "").replace("$", "").replace("£", "").replace(",", ".")
            priceNumber = float(priceText)
            
            return "{:.2f}".format(priceNumber)
        except ValueError:
            print("Error: priceText contains invalid characters for conversion.")
            return None
        except TypeError:
            print("Error: priceText is of an invalid type.")
            return None
    
    @retryOperation(maxAttempts=5, delay=1)
    def getItemDescription(self, parentElement):   
        descriptionElement = self.webDriverManager.findElementWithinElement(parentElement, By.XPATH, ".//div[normalize-space(text())]")
        if(descriptionElement is not None):    
            return descriptionElement.text
        else:
            # escribir aqui
            return None
    
    def getOptionSetData(self, optionSet):
        optionSetHeaderElement = self.webDriverManager.findElementWithinElement(optionSet, By.XPATH, "(.//div)[2]")
        optionSetNameElement = self.getOptionSetNameElement(optionSetHeaderElement)
        selectCount = self.getOptionSetSelectCount(optionSet, optionSetHeaderElement)

        optionSetData = {
        'Name': optionSetNameElement.text,
        'MinSelectCount': selectCount[0],
        'MaxSelectCount': selectCount[1],
        'IsMasterOptionSet': False,
        'MenuItemOptionSets': []
        }

        return optionSetData
    
    def getOptionSetNameElement(self, optionSetHeader):
        optionSetNameElement = self.webDriverManager.findElementWithinElement(optionSetHeader, By.XPATH, ".//div[normalize-space(text())]")
        return optionSetNameElement
    
    def getOptionSetSelectCount(self, optionSet, optionSetHeader):    
        maxCount = self.getMaxCount(optionSet, optionSetHeader)
        minCount = self.getMinCount(optionSetHeader)

        return [minCount, maxCount]
        
    def getMaxCount(self, optionSet, optionSetHeader):
        maxCountText = self.webDriverManager.findElementWithinElement(optionSetHeader, By.TAG_NAME, "span")
        optionSetItems = self.getOptionSetItems(optionSet)
        optionSetLength = len(optionSetItems)
        if(maxCountText is not None):
            maxCountNum = self.extractNumberFromText(maxCountText.text)
            if(maxCountNum > optionSetLength): 
                return optionSetLength
            else:
                return maxCountNum
        else:
            return optionSetLength
        
    def getMinCount(self, optionSetHeader):
        if(self.webDriverManager.findTextInElement(optionSetHeader, "Required")):
            return 1
        else:
            return 0
        
    def getOptionSetItems(self, optionSet):
        """Returns items inside the option set"""
        optionSetItemsContainer = self.getOptionSetItemsContainer(optionSet)
        childDivs = self.webDriverManager.findElementsWithinElement(optionSetItemsContainer, By.XPATH, "./div")

        return childDivs
    
    def getOptionSetItemsContainer(self, optionSet):
        customizationDiv = self.webDriverManager.findElementWithinElement(optionSet, By.XPATH, ".//div[starts-with(@data-testid, 'customization')]")
        optionSetItemsContainer = self.webDriverManager.findElementWithinElement(customizationDiv, By.XPATH, "(./div)[2]")

        return optionSetItemsContainer
    
    def extractNumberFromText(self, text):
        """Extracts the first number found in the given text."""
        numbers = re.findall(r'\d+', text)
        if numbers:
            return int(numbers[0])  # Return the first number found as an integer
        else:
            return None
        
    def getOptionSetItemsData(self, optionSet):
        optionSetItems = []
        optionSetItemsElements = self.getOptionSetItems(optionSet)

        for optionSetItemElement in optionSetItemsElements:
            optionSetItemName = self.getOptionSetItemName(optionSetItemElement)
            parentElement = self.webDriverManager.getParentElement(optionSetItemName)

            if parentElement:
                optionSetItemPrice = self.getOptionSetItemPrice(parentElement)
            else:
                optionSetItemPrice = None

            optionSetItem = {
                "Name": optionSetItemName.text,
                "Price": optionSetItemPrice,
                "NextMenuItemOptionSetId": None
                }
            
            optionSetItems.append(optionSetItem)

        return optionSetItems
    
    def getOptionSetItemName(self, optionSetItemElement):
        optionSetItemName = self.webDriverManager.findElementWithinElement(optionSetItemElement, By.XPATH, ".//div[normalize-space(text())]")

        return optionSetItemName

    def getOptionSetItemPrice(self, parentElement):
        pricePattern = re.compile(r'\+[$€£]\d+(\.\d{1,2})?')
        textElements = self.webDriverManager.findElementsWithinElement(parentElement, By.XPATH, ".//div[normalize-space(text())]")

        for element in textElements:
            elementText = element.text.strip()
            match = pricePattern.search(elementText)
            if match:
                price = self.formatPrice(match.group())
                return price
        return None