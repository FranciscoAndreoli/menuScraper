class MainController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.initialize_view()

    def initialize_view(self):

        self.view.btn_scrap['command'] = self.handle_button_click

    def handle_button_click(self):
        browser = self.view.combo_browser.get()
        webName = self.view.combo_webpage.get()
        webLink = self.view.entry_link.get()

        if(self.verifyData(webName, webLink)):
           self.setDriverFactory(browser)
           self.model.setDriver(webLink)
        else:
            self.view.displayMessage("Error", "The data entered is not correct.")

    def verifyData(self, webName, webLink):
        if("ubereats.com" in webLink.lower() and webName == "Uber Eats"):
            return True
        else:
            return False
    
    def setDriverFactory(self, selectedBrowser):
        if selectedBrowser == "Chrome" and not isinstance(self.model.driver_factory, ChromeDriverFactory):
            self.model.update_driver_factory(ChromeDriverFactory())
        elif selectedBrowser == "Firefox":
            self.model.update_driver_factory(FirefoxDriverFactory())
        