from src.main.classes.rentestimate.ListingsClass import ListingsClass
from src.main.classes.rentestimate.RentEstimateResultsClass import RentEstimateResultsClass
from src.main.services.rentestimate.api import getRentEstimates
import json

class RentEstimateClass:

    def __init__(self):
        self.address = None
        self.bedrooms = None
        self.bathrooms = None
        self.propertyType = None
        self.squareFootage = None
        self.compCount = None
        self.longitude = None
        self.latitude = None
        self.daysOld = None
        self.results = None

    def getRentEstimate(self):
        params = {}
        params["address"] = self.address
        params["bedrooms"] = self.bedrooms
        params["bathrooms"] = self.bathrooms
        params["propertyType"] = self.propertyType
        params["squareFootage"] = self.squareFootage
        params["compCount"] = self.compCount
        params["longitude"] = self.longitude
        params["latitude"] = self.latitude
        params["daysOld"] = self.daysOld

        getRequestResult = getRentEstimates(params)
        self.results = self.jsonToClass(getRequestResult)

    def jsonToClass(self, jsonResult):
        content = json.loads(jsonResult)

        rent = content["rent"]
        rentRangeLow = content["rentRangeLow"]
        rentRangeHigh = content["rentRangeHigh"]
        longitude = content["longitude"]
        latitude = content["latitude"]
        listResults = []

        for listing in content["listings"]:
            listingId = listing["id"]
            formattedAddress = listing["formattedAddress"]
            listingLongitude = listing["longitude"]
            listingLatitude = listing["latitude"]
            city = listing["city"]
            state = listing["state"]
            zipcode = listing["zipcode"]
            listingPrice = listing["price"]
            listingPublishedDate = listing["publishedDate"]
            listingDistance = listing["distance"]
            listingDaysOld = listing["daysOld"]
            listingCorrelation = listing["correlation"]
            listingAddress = listing["address"]
            listingBedrooms = listing["bedrooms"]
            listingBathrooms = listing["bathrooms"]
            listingPropertyType = listing["propertyType"]
            listingSquareFootage = listing["squareFootage"]
            listResults.append(ListingsClass(listingId, formattedAddress, listingLongitude, listingLatitude, city, state, zipcode, listingPrice, listingPublishedDate, listingDistance, listingDaysOld, listingCorrelation, listingAddress, listingBedrooms, listingBathrooms, listingPropertyType, listingSquareFootage))

        return RentEstimateResultsClass(rent, rentRangeLow, rentRangeHigh, longitude, latitude, listResults)