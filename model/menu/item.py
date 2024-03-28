class Item:
    def __init__(self, MenuId, MenuItemId, Name, Description, Price, DisplayOrder, IsDeleted,
                 Alcohol, IsAvailable, TaxRate, TaxRateId, TaxValue, TaxRateName, MenuSectionId, ImageName, ImageUrl, ExternalImageUrl, DailySpecialHours, ActualPrice, DisableVouchers,
                 ExcludeFromVoucherDiscounting, PriceCanIncrease, MenuItemOptionSets=None):
#underscore prefixes for attributes means these attributes are intended for internal use and should not be accessed directly 
#outside the class. private attributes     
        self._MenuId = MenuId
        self._MenuItemId = MenuItemId
        self._Name = Name
        self._Description = Description
        self._Price = Price
        #self._DepositReturnFee = DepositReturnFee
        self._DisplayOrder = DisplayOrder
        #self._SpicinessRating = SpicinessRating
        self._IsDeleted = IsDeleted
        self._Alcohol = Alcohol
        #self._CatalogItemId = CatalogItemId
        #self._PublicId = PublicId
        self._IsAvailable = IsAvailable
        self._TaxRate = TaxRate
        self._TaxRateId = TaxRateId
        self._TaxValue = TaxValue
        self._TaxRateName = TaxRateName
        self._MenuSectionId = MenuSectionId
        self._ImageName = ImageName
        self._ImageUrl = ImageUrl
        self._ExternalImageUrl = ExternalImageUrl
        self._DailySpecialHours = DailySpecialHours if DailySpecialHours is not None else []
        self._ActualPrice = ActualPrice
        self._DisableVouchers = DisableVouchers
        self._ExcludeFromVoucherDiscounting = ExcludeFromVoucherDiscounting
        self._PriceCanIncrease = PriceCanIncrease
        self._MenuItemMetadata = []
        self._MenuItemOptionSets = MenuItemOptionSets if MenuItemOptionSets is not None else []
        
    # Getters
    def getMenuId(self):
        return self._MenuId

    def getMenuSectionId(self):
        return self._MenuSectionId

    def getItemId(self):
        return self._MenuItemId

    def getName(self):
        return self._Name

    def getDescription(self):
        return self._Description

    def getPrice(self):
        return self._Price

    def getOptionSets(self):
        return self._OptionSets
    
    def getDailySpecialHours(self):
        return self._DailySpecialHours
    
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
    
    def getImageName(self):
        return self._ImageName

    def getImageUrl(self):
        return self._ImageUrl
    
    def getExternalImageUrl(self):
        return self._ExternalImageUrl
    
    def getDisplayOrder(self):
        return self._DisplayOrder

    def getIsDeleted(self):
        return self._IsDeleted
    
    # Setters
    def setItemId(self, MenuItemId):
        self._MenuItemId = MenuItemId

    def setOptionSets(self, OptionSets):
        self._OptionSets = OptionSets

    def setDailySpecialHours(self, DailySpecialHours):
        self._DailySpecialHours = DailySpecialHours
    
    def setTaxRateId(self, TaxRateId):
        self._TaxRateId = TaxRateId

    def setTaxRate(self, TaxRate):
        self._TaxRate = TaxRate

    def setTaxValue(self, TaxValue):
        self._TaxValue = TaxValue

    def setTaxRateName(self, TaxRateName):
        self._TaxRateName = TaxRateName

    def setImageName(self, ImageName):
        self._ImageName = ImageName

    def setImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    def setExternalImageUrl(self, ExternalImageUrl):
        self._ExternalImageUrl = ExternalImageUrl
    
    def toDict(self):
        return {
            "MenuId": self._MenuId,
            "MenuItemId": self._MenuItemId,
            "Name": self._Name,
            "Description": self._Description,
            "Price": self._Price,
            "DisplayOrder": self._DisplayOrder,
            "IsDeleted": self._IsDeleted,
            "Alcohol": self._Alcohol,
            "IsAvailable": self._IsAvailable,
            "TaxRate": self._TaxRate,
            "TaxRateId": self._TaxRateId,
            "TaxValue": self._TaxValue,
            "TaxRateName": self._TaxRateName,
            "MenuSectionId": self._MenuSectionId,
            "ImageName": self._ImageName,
            "ImageUrl": self._ImageUrl,
            "ExternalImageUrl": self._ExternalImageUrl,
            "DailySpecialHours": self._DailySpecialHours,
            "ActualPrice": self._ActualPrice,
            "DisableVouchers": self._DisableVouchers,
            "ExcludeFromVoucherDiscounting": self._ExcludeFromVoucherDiscounting,
            "PriceCanIncrease": self._PriceCanIncrease,
            "MenuItemMetadata": self._MenuItemMetadata,
            "MenuItemOptionSets": [optionSet.toDict() for optionSet in self._MenuItemOptionSets]  
        }