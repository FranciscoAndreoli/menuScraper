from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from .abstract_driver_factory import AbstractDriverFactory

class FirefoxDriverFactory(AbstractDriverFactory):
    def getDriver(self):
        try:
            return webdriver.Firefox(executable_path=GeckoDriverManager().install())
        
        except Exception as e:
            print(f"Error while installing Firefox Driver: {e}")
            return None