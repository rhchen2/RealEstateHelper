from src.main.classes.rentestimate.RentEstimateClass import RentEstimateClass
from src.main.classes.zillow.ZillowSearchResultClass import SearchResultClass

def run():

    rent = RentEstimateClass()
    rent.address = "6168 Paseo Pueblo Dr, San Jose, CA"
    rent.getRentEstimate()
    rent.printShit()
