from abc import ABC, abstractmethod

class AbstractDriverFactory(ABC):

    @abstractmethod
    def getDriver(self):
        pass