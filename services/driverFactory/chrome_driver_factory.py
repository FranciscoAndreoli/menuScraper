
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from .abstract_driver_factory import AbstractDriverFactory

class ChromeDriverFactory(AbstractDriverFactory):
    def getDriver(self):
        try:
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        
        except Exception as e:
            print(f"Error while installing Chrome Driver: {e}")
            return None
        