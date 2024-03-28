class MenuItemOptionSets:
    def __init__(self, MenuId, Name, MenuItemOptionSetId, IsMasterOptionSet,
                 DisplayOrder, MinSelectCount, MaxSelectCount, IsDeleted, MenuItemOptionSetItems,
                 ImageName, ImageUrl, MinPrice, MenuItemId, ExternalImageUrl):
    
        self._MenuId = MenuId
        self._Name = Name
        self._MenuItemOptionSetId = MenuItemOptionSetId
        self._IsMasterOptionSet = IsMasterOptionSet
        self._DisplayOrder = DisplayOrder
        self._MinSelectCount = MinSelectCount
        self._MaxSelectCount = MaxSelectCount
        self._IsDeleted = IsDeleted
        #self._PublicId = PublicId
        self._MenuItemOptionSetItems = MenuItemOptionSetItems if MenuItemOptionSetItems is not None else []
        self._ImageName = ImageName
        self._ImageUrl = ImageUrl
        self._MinPrice = MinPrice
        self._MenuItemId = MenuItemId
        self._MenuItemOptionSetMetadata = []
        self._ExternalImageUrl = ExternalImageUrl

    # Getters
    def getMenuId(self):
        return self._MenuId

    def getName(self):
        return self._Name

    def getMenuItemOptionSetId(self):
        return self._MenuItemOptionSetId

    def getIsMasterOptionSet(self):
        return self._IsMasterOptionSet

    def getDisplayOrder(self):
        return self._DisplayOrder

    def getMinSelectCount(self):
        return self._MinSelectCount

    def getMaxSelectCount(self):
        return self._MaxSelectCount

    def getMenuItemOptionSetItems(self):
        return self._MenuItemOptionSetItems

    def getMinPrice(self):
        return self._MinPrice

    def getMenuItemId(self):
        return self._MenuItemId
    
    # Setters
    def setMenuItemOptionSetItems(self, MenuItemOptionSetItems):
        self._MenuItemOptionSetItems = MenuItemOptionSetItems

    def setMenuId(self, MenuId):
        self._MenuId = MenuId

    def setName(self, Name):
        self._Name = Name

    def setMenuItemOptionSetId(self, MenuItemOptionSetId):
        self._MenuItemOptionSetId = MenuItemOptionSetId

    def setIsMasterOptionSet(self, IsMasterOptionSet):
        self._IsMasterOptionSet = IsMasterOptionSet

    def setDisplayOrder(self, DisplayOrder):
        self._DisplayOrder = DisplayOrder

    def setMinSelectCount(self, MinSelectCount):
        self._MinSelectCount = MinSelectCount

    def setMaxSelectCount(self, MaxSelectCount):
        self._MaxSelectCount = MaxSelectCount

    def setMinPrice(self, MinPrice):
        self._MinPrice = MinPrice

    def setMenuItemId(self, MenuItemId):
        self._MenuItemId = MenuItemId
    
    def setImageName(self, ImageName):
        self._ImageName = ImageName

    def setImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    def setExternalImageUrl(self, ExternalImageUrl):
        self._ExternalImageUrl = ExternalImageUrl

    def toDict(self):
        return {
            "MenuId": self._MenuId,
            "Name": self._Name,
            "MenuItemOptionSetId": self._MenuItemOptionSetId,
            "IsMasterOptionSet": self._IsMasterOptionSet,
            "DisplayOrder": self._DisplayOrder,
            "MinSelectCount": self._MinSelectCount,
            "MaxSelectCount": self._MaxSelectCount,
            "IsDeleted": self._IsDeleted,
            "MenuItemOptionSetItems": [item.toDict() for item in self._MenuItemOptionSetItems],  
            "ImageName": self._ImageName,
            "ImageUrl": self._ImageUrl,
            "MinPrice": self._MinPrice,
            "MenuItemId": self._MenuItemId,
            "MenuItemOptionSetMetadata": self._MenuItemOptionSetMetadata,
            "ExternalImageUrl": self._ExternalImageUrl
        }