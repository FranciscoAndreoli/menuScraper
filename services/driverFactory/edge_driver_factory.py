from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from .IDriverFactory import IDriverFactory
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('webdriver_manager')

class EdgeDriverFactory(IDriverFactory):
    def getDriver(self):
        try:
            service = Service(executable_path=EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service)
            return driver
        
        except Exception as e:
            print(f"Error while installing Edge Driver: {e}")
            return None
    
    def closeDriver(self, driver):
        driver.quit()
