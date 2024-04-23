from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from .IDriverFactory import IDriverFactory
from selenium.webdriver.firefox.options import Options

class FirefoxDriverFactory(IDriverFactory):
    def getDriver(self):
        try:
            service = FirefoxService(executable_path=GeckoDriverManager().install())
            options = Options()
            options.page_load_strategy = 'eager'
            driver = webdriver.Firefox(options=options, service=service)
            return driver
        
        except Exception as e:
            print(f"Error while installing Firefox Driver: {e}")
            return None
    
    def closeDriver(self, driver):
        driver.quit()