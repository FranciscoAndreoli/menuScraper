
from model.main_model import MainModel
from view.main_view import MainView
from controller.main_controller import MainController
from services.driverFactory.chrome_driver_factory import ChromeDriverFactory  # Asegúrate de importar correctamente
from services.json_manager import JsonManager

if __name__ == '__main__':
    chromeDriverFactory = ChromeDriverFactory()
    jsonManager = JsonManager()
    model = MainModel(chromeDriverFactory, jsonManager)
    view = MainView()
    controller = MainController(view, model)
    
    view.mainloop()