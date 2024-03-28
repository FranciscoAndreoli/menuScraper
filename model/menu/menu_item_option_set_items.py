class MenuItemOptionSetItems:
    def __init__(self, MenuId, MenuItemOptionSetItemId, Name, Price,
                 TaxRateId, TaxRate, TaxValue, TaxRateName, IsAvailable, DisplayOrder,
                 IsDeleted, Tags, NextMenuItemOptionSetId, ImageName, ImageUrl, ExternalImageUrl):
        
        self._MenuId = MenuId
        self._MenuItemOptionSetItemId = MenuItemOptionSetItemId
        self._Name = Name
        self._Price = Price
        #self._DepositReturnFee = DepositReturnFee
        self._TaxRateId = TaxRateId
        self._TaxRate = TaxRate
        self._TaxValue = TaxValue
        self._TaxRateName = TaxRateName
        self._IsAvailable = IsAvailable
        self._DisplayOrder = DisplayOrder
        self._IsDeleted = IsDeleted
        self._Tags = Tags if Tags is not None else []
        self._NextMenuItemOptionSetId = NextMenuItemOptionSetId
        self._ImageName = ImageName
        self._ImageUrl = ImageUrl
        self._ExternalImageUrl = ExternalImageUrl
        self._OptionSetItemMetadata = []

    # Getters
    def getMenuId(self):
        return self._MenuId

    def getMenuItemOptionSetItemId(self):
        return self._MenuItemOptionSetItemId

    def getName(self):
        return self._Name

    def getPrice(self):
        return self._Price

    def getDepositReturnFee(self):
        return self._DepositReturnFee

    def getTaxRateId(self):
        return self._TaxRateId

    def getTaxRate(self):
        return self._TaxRate

    def getTaxValue(self):
        return self._TaxValue

    def getTaxRateName(self):
        return self._TaxRateName

    def getIsAvailable(self):
        return self._IsAvailable

    def getDisplayOrder(self):
        return self._DisplayOrder

    def getIsDeleted(self):
        return self._IsDeleted

    def getTags(self):
        return self._Tags

    def getNextMenuItemOptionSetId(self):
        return self._NextMenuItemOptionSetId

    def getImageName(self):
        return self._ImageName

    def getImageUrl(self):
        return self._ImageUrl

    def getExternalImageUrl(self):
        return self._ExternalImageUrl

    # Setters
    def setMenuId(self, MenuId):
        self._MenuId = MenuId

    def setMenuItemOptionSetItemId(self, MenuItemOptionSetItemId):
        self._MenuItemOptionSetItemId = MenuItemOptionSetItemId

    def setName(self, Name):
        self._Name = Name

    def setPrice(self, Price):
        self._Price = Price

    def setDepositReturnFee(self, DepositReturnFee):
        self._DepositReturnFee = DepositReturnFee

    def setTaxRateId(self, TaxRateId):
        self._TaxRateId = TaxRateId

    def setTaxRate(self, TaxRate):
        self._TaxRate = TaxRate

    def setTaxValue(self, TaxValue):
        self._TaxValue = TaxValue

    def setTaxRateName(self, TaxRateName):
        self._TaxRateName = TaxRateName

    def setIsAvailable(self, IsAvailable):
        self._IsAvailable = IsAvailable

    def setDisplayOrder(self, DisplayOrder):
        self._DisplayOrder = DisplayOrder

    def setIsDeleted(self, IsDeleted):
        self._IsDeleted = IsDeleted

    def setTags(self, Tags):
        self._Tags = Tags

    def setNextMenuItemOptionSetId(self, NextMenuItemOptionSetId):
        self._NextMenuItemOptionSetId = NextMenuItemOptionSetId

    def setImageName(self, ImageName):
        self._ImageName = ImageName

    def setImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    def setExternalImageUrl(self, ExternalImageUrl):
        self._ExternalImageUrl = ExternalImageUrl

    def toDict(self):
        return {
            "MenuId": self._MenuId,
            "MenuItemOptionSetItemId": self._MenuItemOptionSetItemId,
            "Name": self._Name,
            "Price": self._Price,
            "TaxRateId": self._TaxRateId,
            "TaxRate": self._TaxRate,
            "TaxValue": self._TaxValue,
            "TaxRateName": self._TaxRateName,
            "IsAvailable": self._IsAvailable,
            "DisplayOrder": self._DisplayOrder,
            "IsDeleted": self._IsDeleted,
            "Tags": self._Tags,
            "NextMenuItemOptionSetId": self._NextMenuItemOptionSetId,
            "ImageName": self._ImageName,
            "ImageUrl": self._ImageUrl,
            "ExternalImageUrl": self._ExternalImageUrl,
            "OptionSetItemMetadata": self._OptionSetItemMetadata
        }
