
from model.main_model import MainModel
from view.main_view import MainView
from controller.main_controller import MainController
from services.driverFactory.chrome_driver_factory import ChromeDriverFactory  
from services.IJsonManager import IJsonManager
from services.json_manager import JsonManager

if __name__ == '__main__':
    driverFactory = ChromeDriverFactory()
    jsonManager: IJsonManager = JsonManager()

    model = MainModel(driverFactory)
    view = MainView()
    controller = MainController(view, model, jsonManager)
    
    view.mainloop()