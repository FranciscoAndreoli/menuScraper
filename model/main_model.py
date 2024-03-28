from services.driverFactory.IDriverFactory import IDriverFactory
#La interfaz IDriverFactory se utiliza como tipo para un parámetro del constructor, indicando que MainModel puede trabajar con cualquier implementación
#de esa interfaz, sin necesidad de saber qué implementación concreta es. 
#Esto último promueve la flexibilidad y la desacoplamiento entre MainModel y las clases que crean los objetos driver.
class MainModel:
    def __init__(self, driverFactory: IDriverFactory):
        self.driverFactory = driverFactory
    
    def updateDriverFactory(self, newDriverFactory):
        self.driverFactory = newDriverFactory

    def setDriver(self):
        driver = self.driverFactory.getDriver()
        if driver != None:
            return driver
        else:
            return None

