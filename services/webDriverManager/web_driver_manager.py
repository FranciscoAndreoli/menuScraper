from services.driverFactory.chrome_driver_factory import ChromeDriverFactory
from services.driverFactory.firefox_driver_factory import FirefoxDriverFactory
from services.driverFactory.edge_driver_factory import EdgeDriverFactory
from services.webDriverUtilities.web_driver_utilities import retryOperation
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException, StaleElementReferenceException
import time

class WebDriverManager:
    def __init__(self, driverFactory=None):
        
        self.driverFactory = driverFactory
        self.driver = None

    def setDriverFactory(self, driverFactory):
        self.driverFactory = driverFactory

    def createDriver(self, browserType):
        if browserType == "Chrome":
            self.setDriverFactory(ChromeDriverFactory())
        elif browserType == "Firefox":
            self.setDriverFactory(FirefoxDriverFactory())
        elif  browserType == "Edge":
            self.setDriverFactory(EdgeDriverFactory())
            
        if self.driverFactory:
            self.driver = self.driverFactory.getDriver()
        else:
            raise Exception("No driver factory set.")
        
    def navigateTo(self, url):
        self.driver.get(url)

    def findElement(self, by=By.ID, value=None):
        """Find an element given a By strategy and locator."""
        try:
            return self.driver.find_element(by, value)
        except NoSuchElementException:
            print(f"Element not found with {by} and value {value}.")
            self.takeScreenshot(r"C:\Users\franc\OneDrive\Escritorio\error_screenshotNotFoundElement.png")
            return None
        
    def findElementsWithinElement(self, parentElement, by=By.ID, value=None):
        """Find a list of elements within a parent element given a By strategy and locator for the child."""
        try:
            return parentElement.find_elements(by, value)
        except NoSuchElementException:
            print(f"Child elements not found within parent with {by} and value {value}.")
            self.takeScreenshot(r"C:\Users\franc\OneDrive\Escritorio\error_screenshotNotFoundElementsWithinElement.png")
            return None    
        
    def findElementWithinElement(self, parentElement, by=By.ID, value=None):
        """Find an element within a parent element given a By strategy and locator for the child."""
        try:
            return parentElement.find_element(by, value)
        except NoSuchElementException:
            #print(f"Child element not found within parent with {by} and value {value}.")
            self.takeScreenshot(r"C:\Users\franc\OneDrive\Escritorio\error_screenshotNotFoundElementWithinElement.png")
            return None       
        
    def findTextInElement(self, parentElement, text):
        """Searches for the specified text within an element and all of its child elements. """
        try:
            # Prepare the text for a case-insensitive search
            upper_text = text.upper()
            lower_text = text.lower()
            translated_text = ''.join(['ABCDEFGHIJKLMNOPQRSTUVWXYZ' if char.isupper() else 'abcdefghijklmnopqrstuvwxyz' for char in text])
            
            # Using XPath to check for the text anywhere within the element, case-insensitively
            if parentElement.find_element(By.XPATH, f".//*[contains(translate(., '{upper_text}', '{lower_text}'), '{lower_text}')]"):
                return True
        except NoSuchElementException:
            pass

        return False
    
    def waitForPresenceOfElement(self, by, argument, timeout=30):
        """Wait for an element to be present."""
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, argument)))
            return element
        except TimeoutException:
            print(f"Timeout waiting for element {argument}.")
            self.takeScreenshot(r"C:\Users\franc\OneDrive\Escritorio\error_screenshotWaitForPresenceOfElement.png")
            #self.quit()
            return None
    
    def waitForPresenceOfElementWithinElement(self, element, by, argument, timeout=30):
        """Wait for an element to be present."""
        try:
            element = WebDriverWait(element, timeout).until(EC.presence_of_element_located((by, argument)))
            return element
        except TimeoutException:
            print(f"Timeout waiting for element {argument}.")
            self.takeScreenshot(r"C:\Users\franc\OneDrive\Escritorio\error_screenshotWaitForPresenceOfElementWithinElement.png")
            #self.quit()
            return None
        
    def waitForPresenceOfAllElementsLocatedWithinElement(self, parentElement, by, value, timeout=30):
        """Waits for all elements that match the given locator within the parent element to be present in the DOM."""
        try:
            elements = WebDriverWait(parentElement, timeout).until(
                EC.presence_of_all_elements_located((by, value))
            )
            return elements
        except TimeoutException:
            print(f"Timeout waiting for elementS by {by} with value '{value}' to be present in the DOM.")
            self.takeScreenshot(r"C:\Users\franc\OneDrive\Escritorio\error_screenshotWaitForPresenceOfAllElementsLocatedWithinElement.png")
            return None
        
    def waitForVisibilityOfElementWithinElement(self, element, by, argument, timeout=30):
        """Wait for an element to be visible, inside another element."""
        try:
            element = WebDriverWait(element, timeout).until(EC.visibility_of_element_located((by, argument)))
            return element
        except TimeoutException:
            print(f"Timeout waiting for element by {by} with value '{argument}' to be visible.")
            self.takeScreenshot(r"C:\Users\franc\OneDrive\Escritorio\error_screenshotWaitForVisibilityOfElementWithinElement.png")

            return None
        
    def waitForVisibilityOfElement(self, by, value, timeout=30):
        """Waits for any element that matches the given locator to become visible."""
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))
            return element
        except TimeoutException:
            print(f"Timeout waiting for visibility of element {value}.")
            self.takeScreenshot(r"C:\Users\franc\OneDrive\Escritorio\error_screenshotWaitForVisibilityOfElement.png")
            #self.quit()
            return None
        
    def waitForLocatedElementToBeVisible(self, element, timeout=30):
        """Waits for a specific WebElement that has already been found to become visible."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of(element))
        except TimeoutException:
            print(f"Timeout waiting for located element to be visible: {element}.")
            self.takeScreenshot(r"C:\Users\franc\OneDrive\Escritorio\error_screenshotWaitForLocatedElementToBeVisible.png")
            #self.quit()
            return None      
        
    def waitForOpacity(self, element, timeout=30):
        """Wait for an element to be fully opaque."""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: element.value_of_css_property('opacity') == '1'
            )
        except TimeoutException:
            print(f"Timeout waiting for opacity of element: {element}.")
            self.takeScreenshot(r"C:\Users\franc\OneDrive\Escritorio\error_screenshotWaitForOpacity.png")
            ##self.quit()
            return None
        
        except WebDriverException as e:
            print(f"Error del WebDriver: {e}")
            self.takeScreenshot(r"C:\Users\franc\OneDrive\Escritorio\error_screenshotWebDriver.png")
            ##self.quit()
            return None
        
    def scrollToAllLinks(self, element):
        """Scroll through all links in the given element to ensure they are loaded."""
        seenLinks = set()
        newFound = True

        while newFound:
            newFound = False
            currentLinks = element.find_elements(By.TAG_NAME, 'a')

            for link in currentLinks:
                linkHref = link.get_attribute('href')
                if linkHref not in seenLinks:
                    seenLinks.add(linkHref)  # Mark this link as seen
                    self.scrollToElement(link) 
                    time.sleep(0.5)
                    newFound = True 

        return list(seenLinks)
    
    def getHrefLinks(self, element):
        """Get hrefs from a specific element, ensuring dynamic content loads while scrolling."""
        try:
            links = self.scrollToAllLinks(element)
            return links
        except Exception as e:
            print(f"Could not get href links from element: {element}. Error: {str(e)}")
            self.takeScreenshot(r"C:\Users\franc\OneDrive\Escritorio\error_screenshotGetHrefLinks.png")
            return None
        
    def getHrefAttributes(self, links):
        """Extract href attributes from a list of link elements."""
        try:
            hrefs = [link.get_attribute('href') for link in links if link.get_attribute('href') is not None]
            return hrefs
        except Exception as e:
            print(f"Could not extract hrefs. Error: {str(e)}")
            self.takeScreenshot(r"C:\Users\franc\OneDrive\Escritorio\error_screenshotGetHrefLinksAttributes.png")
            return None
    
    @retryOperation(maxAttempts=5, delay=1)
    def getParentElement(self, element):
            WebDriverWait(self.driver, 30).until(EC.visibility_of(element))
            parentElement = element.find_element(By.XPATH, "..")
            return parentElement

        
    def getAttribute(self, element, attributeName):
        """Get an attribute from a WebElement."""
        try:
            attributeValue = element.get_attribute(attributeName)
            return attributeValue
        except NoSuchElementException:
            print(f"The element does not exist, could not get attribute '{attributeName}'.")
            self.takeScreenshot(r"C:\Users\franc\OneDrive\Escritorio\error_getAttribute.png")
        except Exception as e:
            print(f"An error occurred while getting attribute '{attributeName}': {e}")
            self.takeScreenshot(r"C:\Users\franc\OneDrive\Escritorio\error_getAttribute.png")
        return None
    
    def executeScriptAndReturn(self, script):
        try:
            return self.driver.execute_script(script)
        except:
            print(f"Could not excute script: {script}.")
    
    def getCurrentWindowHandle(self):
        """Returns the identifier (handle) of the current browser window that the  WebDriver is focused on."""
        return self.driver.current_window_handle
    
    def openNewTab(self, url):
        self.driver.execute_script(f"window.open('{url}', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def closeCurrentTab(self, originalWindowHandle):
        self.driver.close()
        self.driver.switch_to.window(originalWindowHandle)

    def takeScreenshot(self, screenshotPath):
        self.driver.save_screenshot(screenshotPath)
    
    def quit(self):
        self.driver.quit()

    def close(self):
        self.driver.close()

    def implicitlyWait(self, time):
        self.driver.implicitly_wait(time)
        
    def scrollToElement(self, element):
        """Instantly scroll to the given element on the page."""
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        except Exception as e:
            print(f"Failed to scroll to element. Error: {str(e)}")
