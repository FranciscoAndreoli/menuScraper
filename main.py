
from model.main_model import MainModel
from view.main_view import MainView
from controller.main_controller import MainController
from services.chrome_driver_factory import ChromeDriverFactory  # Asegúrate de importar correctamente

if __name__ == '__main__':
    chromeDriverFactory = ChromeDriverFactory()
    model = MainModel(chromeDriverFactory)
    view = MainView()
    controller = MainController(view, model)
    
    view.mainloop()