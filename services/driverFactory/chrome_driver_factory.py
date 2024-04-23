
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from .IDriverFactory import IDriverFactory
#import os
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

class ChromeDriverFactory(IDriverFactory):
    def getDriver(self):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger()
        options = Options()
        #options.page_load_strategy = 'normal'
        options.add_argument("--log-level=3")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        #options.add_argument("--headless")
        options.add_argument("--disable-extensions")
        options.add_argument("--start-maximized")
        
        try:
            #pathToChromeDriver = "C:\\Users\\franc\\OneDrive\\Escritorio\\chromedriver-win64\\chromedriver.exe"  # Update this path
            
            # Check if the path to the driver is valid
            #if not os.path.isfile(pathToChromeDriver):
            #    raise FileNotFoundError(f"ChromeDriver not found at: {pathToChromeDriver}")

            #d = DesiredCapabilities.CHROME
            #d['goog:loggingPrefs'] = { 'browser':'ALL' }
            
            #service = ChromeService(executable_path=pathToChromeDriver)
            #driver = webdriver.Chrome(options=options, service=service)
            #return driver

            driver = webdriver.Chrome(options, service=ChromeService(ChromeDriverManager().install()))
            return driver
        
        except Exception as e:
            print(f"Error while installing Chrome Driver: {e}")
            logger.error(f"An error occurred while installing Chrome Driver: {e}")
            return None

    def closeDriver(self, driver):
        driver.quit()