import datetime
from money import Money

class GeoCoord:
    latitude = 0.0
    longitude = 0.0

    def __init__(self, coords):
        self.latitude = coords['latitude']
        self.longitude = coords['longitude']

class Location:
    def __init__(self, street, city, zipcode, state, coords={'latitude': 0.0, 'longitude': 0.0}):
        self.street = street
        self.city = city
        self.zipcode = zipcode
        self.state = state
        self.coords = GeoCoord(coords)
        
class Price:
    def __init__(self, amount, updatedAt=None):
        self.amount = Money(amount, 'USD')
        self.updatedAt = updatedAt if updatedAt else date.today().strftime("%d/%m/%Y")

class Property:
    priceHistory = []

    def __init__(self, price, location):
        self.currentPrice = price
        self.priceHistory.append(self.currentPrice)
        self.location = location

    def updatePrice(self, amount):
        self.currentPrice = Price(amount)
        self.priceHistory.append(self.currentPrice)

class ZillowUnit(Property):
    def __init__(self, 
        zpid, zIndexValue,
        homeDetailsURL, mapThisHomeURL, comparablesURL, 
        localRealEstateOverviewURL, localRealEstateForSaleByOwnerURL, localRealEstateForSaleURL,
        lowValuationRange, highValuationRange, regionName, regionId, regionType,
        price, location
    ):
        self.zpid = zpid # zillow property id
        self.zIndexValue = zIndexValue

        self.homeDetailsURL = homeDetailsURL # ??
        self.mapThisHomeURL = mapThisHomeURL # ??
        self.comparablesURL = comparablesURL # ??
        self.localRealEstateOverviewURL = localRealEstateOverviewURL
        self.localRealEstateForSaleByOwnerURL = localRealEstateForSaleByOwnerURL
        self.localRealEstateForSaleURL = localRealEstateForSaleURL

        self.lowValuationRange = lowValuationRange
        self.highValuationRange = highValuationRange

        self.regionName = regionName
        self.regionId = regionId
        self.regionType = regionType

        super().__init__(price, location)

