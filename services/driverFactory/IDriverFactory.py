from abc import ABC, abstractmethod

class IDriverFactory(ABC):

    @abstractmethod
    def getDriver(self):
        pass

    @abstractmethod
    def closeDriver(self, driver):
        pass