class Section:
    def __init__(self, MenuSectionId, Name, Description, DisplayOrder, MenuItems, IsDeleted, IsAvailable, 
                 IsHiddenFromUsers, ImageName, ImageUrl, ExternalImageUrl, MenuSectionAvailability=None):
        
        self._MenuSectionId = MenuSectionId
        self._Name = Name
        self._Description = Description
        self._DisplayOrder = DisplayOrder
        self._MenuItems = MenuItems if MenuItems is not None else []
        #self._PublicId = PublicId
        self._IsDeleted = IsDeleted
        self._IsAvailable = IsAvailable
        self._IsHiddenFromUsers = IsHiddenFromUsers
        self._ImageName = ImageName
        self._ImageUrl = ImageUrl
        self._ExternalImageUrl = ExternalImageUrl
        # Attributes without getters/setters
        self._MenuSectionAvailability = MenuSectionAvailability if MenuSectionAvailability is not None else {"AvailableTimes": [], "MenuSectionId": MenuSectionId, "AvailabilityMode": 1}
        #self._ConcessionStoreId = ConcessionStoreId
        self._MenuSectionMetadata = []
        
    # Getters
    def getMenuSectionId(self):
        return self._MenuSectionId

    def getName(self):
        return self._Name

    def getDescription(self):
        return self._Description

    def getDisplayOrder(self):
        return self._DisplayOrder

    def getMenuItems(self):
        return self._MenuItems

    def getPublicId(self):
        return self._PublicId

    def getIsDeleted(self):
        return self._IsDeleted

    def getIsAvailable(self):
        return self._IsAvailable

    def getIsHiddenFromUsers(self):
        return self._IsHiddenFromUsers

    def getImageName(self):
        return self._ImageName

    def getImageUrl(self):
        return self._ImageUrl

    def getExternalImageUrl(self):
        return self._ExternalImageUrl

    # Setters
    def setMenuSectionId(self, MenuSectionId):
        self._MenuSectionId = MenuSectionId

    def setName(self, Name):
        self._Name = Name

    def setDescription(self, Description):
        self._Description = Description

    def setDisplayOrder(self, DisplayOrder):
        self._DisplayOrder = DisplayOrder

    def setMenuItems(self, MenuItems):
        self._MenuItems = MenuItems

    def setPublicId(self, PublicId):
        self._PublicId = PublicId

    def setIsDeleted(self, IsDeleted):
        self._IsDeleted = IsDeleted

    def setIsAvailable(self, IsAvailable):
        self._IsAvailable = IsAvailable

    def setIsHiddenFromUsers(self, IsHiddenFromUsers):
        self._IsHiddenFromUsers = IsHiddenFromUsers

    def setImageName(self, ImageName):
        self._ImageName = ImageName

    def setImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    def setExternalImageUrl(self, ExternalImageUrl):
        self._ExternalImageUrl = ExternalImageUrl

    def toDict(self):
        return {
            "MenuSectionId": self._MenuSectionId,
            "Name": self._Name,
            "Description": self._Description,
            "DisplayOrder": self._DisplayOrder,
            "MenuItems": [menuItem.toDict() for menuItem in self._MenuItems],
            "IsDeleted": self._IsDeleted,
            "IsAvailable": self._IsAvailable,
            "IsHiddenFromUsers": self._IsHiddenFromUsers,
            "ImageName": self._ImageName,
            "ImageUrl": self._ImageUrl,
            "ExternalImageUrl": self._ExternalImageUrl,
            "MenuSectionAvailability": self._MenuSectionAvailability,
            "MenuSectionMetadata": self._MenuSectionMetadata
        }