from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class AbstractDriverFactory(ABC):

    @abstractmethod
    def get_driver(self):
        pass