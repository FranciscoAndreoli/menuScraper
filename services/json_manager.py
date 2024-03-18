import json
from .iJsonManager import IJsonManager
import os

class JsonManager(IJsonManager):

    @staticmethod
    def serialize(objeto):
        """Serialize a JSON object."""
        try:
            return json.dumps(objeto)
        except TypeError as e:
            print(f"Error serializing object: {e}")
            return None

    @staticmethod
    def deserialize(jsonString):
        """Deserialize a JSON string to an object."""
        try:
            return json.loads(jsonString)
        except json.JSONDecodeError as e:
            print(f"Error deserializing JSON string: {e}")
            return None

    @staticmethod
    def saveToFile(objeto, filename):
        """Saves an object as a JSON file."""
        try:
            filePath = os.path.join(os.environ["USERPROFILE"], filename)
            with open(filePath, "w") as jsonFile:
                json.dump(objeto, jsonFile)
        except (IOError, OSError, TypeError) as e:
            print(f"Error saving object to file: {e}")

    @staticmethod
    def loadFromFile(filename):
        """Loads an object from a JSON file."""
        try:
            with open(filename, 'r') as jsonFile:
                return json.load(jsonFile)
        except (IOError, OSError, json.JSONDecodeError) as e:
            print(f"Error loading object from file: {e}")
            return None