

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json 

class MainModel:
    def __init__(self, driverFactory, jsonManager):
        self.driverFactory = driverFactory
        self.jsonManager = jsonManager
        pass
    
    def updateDriverFactory(self, newDriverFactory):
        self.driverFactory = newDriverFactory

    def setDriver(self, webLink):
        driver = self.driverFactory.getDriver()
        if driver != None:
            driver.get(webLink)
            self.getSectionsAndItems(driver)

    def getSectionsAndItems(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'main-content')))
        mainContent = driver.find_element(By.ID, 'main-content')
        #json that contains sections and items
        jsonScript = mainContent.find_element(By.XPATH, ".//script[@type='application/ld+json']")
        jsonContentString = jsonScript.get_attribute('textContent')
        jsonObject = json.loads(jsonContentString) #method used to parse a JSON string and convert it into a Dictionary. 
        self.jsonManager.saveToFile(jsonObject, "json1")
        print("Contenido JSON:", json.dumps(jsonObject, indent=4))
