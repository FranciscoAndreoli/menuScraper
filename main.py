
from model.main_model import MainModel
from services.webDriverManager.web_driver_manager import WebDriverManager
from view.main_view import MainView
from controller.main_controller import MainController
from services.driverFactory.chrome_driver_factory import ChromeDriverFactory  
from services.iJsonManager import IJsonManager
from services.json_manager import JsonManager

if __name__ == '__main__':
    jsonManager: IJsonManager = JsonManager()
    driverManager = WebDriverManager()

    model = MainModel()
    view = MainView()
    controller = MainController(view, model, jsonManager, driverManager)
    
    view.mainloop()