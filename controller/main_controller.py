from services.driverFactory.chrome_driver_factory import ChromeDriverFactory
from services.driverFactory.firefox_driver_factory import FirefoxDriverFactory
from model.uber_eats_scraper import UberEatsScraper

class MainController:
    def __init__(self, view, model, jsonManager):
        self.view = view
        self.model = model
        self.jsonManager = jsonManager
        self.initialize_view()

    def initialize_view(self):

        self.view.btn_scrap['command'] = self.handle_button_click

    def handle_button_click(self):
        browser = self.view.combo_browser.get()
        webName = self.view.combo_webpage.get()
        webLink = self.view.entry_link.get()

        if(self.verifyData(webName, webLink)):
           driver = self.setDriverFactory(browser)
           self.setScraper(driver, webName, webLink)
        
        else:
            self.view.displayMessage("Error", "The data entered is not correct.")

    def verifyData(self, webName, webLink):
        if("ubereats.com" in webLink.lower() and webName == "Uber Eats"):
            return True
        else:
            return False
    
    def setDriverFactory(self, selectedBrowser):
        if selectedBrowser == "Chrome" and not isinstance(self.model.driverFactory, ChromeDriverFactory):
            self.model.updateDriverFactory(ChromeDriverFactory())
        
        elif selectedBrowser == "Firefox" and not isinstance(self.model.driverFactory, FirefoxDriverFactory):
            self.model.updateDriverFactory(FirefoxDriverFactory())

        return self.model.setDriver()
    
    def setScraper(self, driver, webName, webLink):
        if(webName == "Uber Eats"):
            UberEatsScraper(driver, self.jsonManager, webLink)
        