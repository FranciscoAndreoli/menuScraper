from abc import ABC, abstractmethod

class IJsonManager(ABC):
    @staticmethod
    @abstractmethod
    def serialize(objeto):
        pass

    @staticmethod
    @abstractmethod
    def deserialize(cadena_json):
        pass

    @staticmethod
    @abstractmethod
    def saveToFile(objeto, filename):
        pass

    @staticmethod
    @abstractmethod
    def loadFromFile(filename):
        pass
