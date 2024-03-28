from model.interfaces.IUberEatsScraper import IUberEatsScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json 
from selenium.common.exceptions import TimeoutException
#La clase está implementando una interfaz IUberEatsScraper, lo cual indica qué métodos deben existir en la clase
class UberEatsScraper(IUberEatsScraper):

    def __init__(self, driver, jsonManager, webLink):
        self.webLink = webLink
        self.driver = driver
        self.driver.get(self.webLink)
        self.jsonManager = jsonManager
        self.menuJson = None
        self.getMainContent()
        if self.mainContent:
            self.getMenuJSON()
        

    def getMainContent(self):
        try:
            self.mainContent = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'main-content')))
            self.getMenuJSON()

        except TimeoutException:
            print("Timeout waiting for 'main-content' element to load.")
            self.driver.quit()

    def getMenuJSON(self):
        try:
            jsonScript = self.mainContent.find_element(By.XPATH, ".//script[@type='application/ld+json']")
            jsonContentString = jsonScript.get_attribute('textContent')
            self.menuJson = json.loads(jsonContentString) #parse a JSON string and convert it into a Dictionary. 
            self.jsonManager.saveToFile(self.menuJson, "json3")

            wrapper_element = self.driver.find_element(By.ID, 'wrapper')
            wrapper_html = wrapper_element.get_attribute('innerHTML')
            with open('C://Users//franc//content.txt', 'w', encoding='utf-8') as file:
                file.write(wrapper_html)
                
        except Exception as e:
            print(f"Error obteniendo application/ld+json: {e}")

        