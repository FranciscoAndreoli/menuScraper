from abc import abstractmethod
from .IScraper import IScraper


class IUberEatsScraper(IScraper):

    @abstractmethod
    def getMenuJSON(self):
        """Uber Eats has an HTML elemnt with a JSON containing sections and items"""
        pass