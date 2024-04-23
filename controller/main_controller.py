from services.driverFactory.chrome_driver_factory import ChromeDriverFactory
from services.driverFactory.firefox_driver_factory import FirefoxDriverFactory
from services.driverFactory.edge_driver_factory import EdgeDriverFactory
from model.uber_eats_scraper import UberEatsScraper
from services.webDriverManager.web_driver_manager import WebDriverManager
class MainController:
    def __init__(self, view, model, jsonManager, webDriverManager):
        self.view = view
        self.model = model
        self.jsonManager = jsonManager
        self.webDriverManager = webDriverManager
        self.initialize_view()

    def initialize_view(self):

        self.view.btn_scrap['command'] = self.handle_button_click

    def handle_button_click(self):
        browser = self.view.combo_browser.get()
        webName = self.view.combo_webpage.get()
        webLink = self.view.entry_link.get()

        if(self.verifyData(webName, webLink)):
           self.webDriverManager.createDriver(browser)
           self.setScraper(webName, webLink)
        
        else:
            self.view.displayMessage("Error", "The data entered is not correct.")

    def verifyData(self, webName, webLink):
        if("ubereats.com" in webLink.lower() and webName == "Uber Eats"):
            return True
        else:
            return False
    
    def setScraper(self, webName, webLink):
        if(webName == "Uber Eats"):
            UberEatsScraper(self.jsonManager, webLink, self.webDriverManager)
        