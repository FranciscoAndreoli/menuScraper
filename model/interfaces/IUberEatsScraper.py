from abc import abstractmethod
from .IScraper import IScraper


class IUberEatsScraper(IScraper):
    @abstractmethod
    def getMainContent(self):
        """Gets the main element from the HTML"""
        pass
    @abstractmethod
    def getMenuJSON(self):
        """Uber Eats has an HTML element with a JSON containing sections and items"""
        pass