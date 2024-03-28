from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from .IDriverFactory import IDriverFactory

class FirefoxDriverFactory(IDriverFactory):
    def getDriver(self):
        try:
            service = FirefoxService(executable_path=GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)
            return driver
        
        except Exception as e:
            print(f"Error while installing Firefox Driver: {e}")
            return None
    
    def closeDriver(self, driver):
        driver.quit()