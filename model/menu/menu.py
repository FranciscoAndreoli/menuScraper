
class Menu:
    def __init__(self, Name, TaxRates, TaxType, DisplayTax, MenuSections):
        
        self._MenuId = 0
        self._Name = Name
        self._WhiteLabelConfigId = 0
        self._Locked = False
        self._Deleted = False
        self._VersionNumber = 0
        self._EditedSinceJsonCreated = True
        self._VersionGuid = "c7677f75-1acf-40fe-a67d-1f7c6c59323a"
        self._TsUpdate = "2024-01-15T15:31:07.053"
        self._TaxRates = TaxRates if TaxRates is not None else []
        self._TaxType = TaxType
        self._DisplayTax = DisplayTax
        self._Currency = 0
        self._MenuSectionBehaviour = 1
        self._DisplaySectionLinks = True
        self._MenuSections = MenuSections if MenuSections is not None else []
        self._ImageName = None,
        self._ImageUrl = None
        self._ConcessionStores = []
        self._MenuCheckpointSetId = None
        self._MenuCheckpointSet = None
        self._ExternalImageUrl = None
        
    # Getters
    def getMenuId(self):
        return self._MenuId

    def getName(self):
        return self._Name

    def getWhiteLabelConfigId(self):
        return self._WhiteLabelConfigId

    def getLocked(self):
        return self._Locked

    def getDeleted(self):
        return self._Deleted

    def getVersionNumber(self):
        return self._VersionNumber

    def getEditedSinceJsonCreated(self):
        return self._EditedSinceJsonCreated

    def getVersionGuid(self):
        return self._VersionGuid

    def getTsUpdate(self):
        return self._TsUpdate

    def getTaxRates(self):
        return self._TaxRates

    def getTaxType(self):
        return self._TaxType

    def getDisplayTax(self):
        return self._DisplayTax

    def getCurrency(self):
        return self._Currency

    def getMenuSectionBehaviour(self):
        return self._MenuSectionBehaviour

    def getDisplaySectionLinks(self):
        return self._DisplaySectionLinks

    def getMenuSections(self):
        return self._MenuSections

    def getImageName(self):
        return self._ImageName

    def getImageUrl(self):
        return self._ImageUrl

    def getConcessionStores(self):
        return self._ConcessionStores

    def getMenuCheckpointSetId(self):
        return self._MenuCheckpointSetId

    def getMenuCheckpointSet(self):
        return self._MenuCheckpointSet

    def getExternalImageUrl(self):
        return self._ExternalImageUrl

    # Setters
    def setMenuId(self, MenuId):
        self._MenuId = MenuId

    def setName(self, Name):
        self._Name = Name

    def setWhiteLabelConfigId(self, WhiteLabelConfigId):
        self._WhiteLabelConfigId = WhiteLabelConfigId

    def setLocked(self, Locked):
        self._Locked = Locked

    def setDeleted(self, Deleted):
        self._Deleted = Deleted

    def setVersionNumber(self, VersionNumber):
        self._VersionNumber = VersionNumber

    def setEditedSinceJsonCreated(self, EditedSinceJsonCreated):
        self._EditedSinceJsonCreated = EditedSinceJsonCreated

    def setVersionGuid(self, VersionGuid):
        self._VersionGuid = VersionGuid

    def setTsUpdate(self, TsUpdate):
        self._TsUpdate = TsUpdate

    def setTaxRates(self, TaxRates):
        self._TaxRates = TaxRates

    def setTaxType(self, TaxType):
        self._TaxType = TaxType

    def setDisplayTax(self, DisplayTax):
        self._DisplayTax = DisplayTax

    def setCurrency(self, Currency):
        self._Currency = Currency

    def setMenuSectionBehaviour(self, MenuSectionBehaviour):
        self._MenuSectionBehaviour = MenuSectionBehaviour

    def setDisplaySectionLinks(self, DisplaySectionLinks):
        self._DisplaySectionLinks = DisplaySectionLinks

    def setMenuSections(self, MenuSections):
        self._MenuSections = MenuSections

    def setImageName(self, ImageName):
        self._ImageName = ImageName

    def setImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    def setConcessionStores(self, ConcessionStores):
        self._ConcessionStores = ConcessionStores

    def setMenuCheckpointSetId(self, MenuCheckpointSetId):
        self._MenuCheckpointSetId = MenuCheckpointSetId

    def setMenuCheckpointSet(self, MenuCheckpointSet):
        self._MenuCheckpointSet = MenuCheckpointSet

    def setExternalImageUrl(self, ExternalImageUrl):
        self._ExternalImageUrl = ExternalImageUrl

    def toDict(self):
        return {
            "MenuId": self._MenuId,
            "Name": self._Name,
            "WhiteLabelConfigId": self._WhiteLabelConfigId,
            "Locked": self._Locked,
            "Deleted": self._Deleted,
            "VersionNumber": self._VersionNumber,
            "EditedSinceJsonCreated": self._EditedSinceJsonCreated,
            "VersionGuid": self._VersionGuid,
            "TsUpdate": self._TsUpdate,
            "TaxRates": self._TaxRates,
            "TaxType": self._TaxType,
            "DisplayTax": self._DisplayTax,
            "Currency": self._Currency,
            "MenuSectionBehaviour": self._MenuSectionBehaviour,
            "DisplaySectionLinks": self._DisplaySectionLinks,
            "MenuSections": [section.toDict() for section in self._MenuSections],  
            "ImageName": self._ImageName,
            "ImageUrl": self._ImageUrl,
            "ConcessionStores": self._ConcessionStores,
            "MenuCheckpointSetId": self._MenuCheckpointSetId,
            "MenuCheckpointSet": self._MenuCheckpointSet,
            "ExternalImageUrl": self._ExternalImageUrl
        }