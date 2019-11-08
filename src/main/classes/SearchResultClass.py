from services.zillow.GetSearchResults import getSearchResults
from classes.SearchResults import SearchResults
from bs4 import BeautifulSoup

class SearchResultClass:
    def __init__(self, zwsid, citystatezip, address):
        self.zwsid = zwsid
        self.citystatezip = citystatezip
        self.address = address
        self.results = []

    def getSearchResultsHelper(self):
        params = {}
        params["zws-id"] = self.zwsid
        params["citystatezip"] = self.citystatezip
        params["address"] = self.address
        getRequestResult = getSearchResults(params)

        self.xmlToClass(getRequestResult)

    def xmlToClass(self, xmlResult):
        contents = BeautifulSoup(xmlResult,'xml')
        results = contents.find_all("results")
        for result in results:
            self.results.append(self.instaniateSearchResult(result))

    def instaniateSearchResult(self, content):
        zpid = content.zpid
        homeDetailsLink=content.links.homedetails
        mapThisHomeLink=content.links.mapethishome
        comparablesLink=content.links.comparable
        streetAddress=content.address.street
        zipcodeAddress=content.address.zipcode
        cityAddress=content.address.city
        stateAddress=content.address.state
        latitudeAddress=content.address.latitude
        longitudeAddress=content.address.longitude
        amount=content.zestimate.amount
        # lastUpdated = content.zestimate.last-updated
        lastUpdated = content.find('last-updated')
        valueChange=content.zestimate.valueChange
        lowValuationRange=content.zestimate.valuationRange.low
        highValuationRange=content.zestimate.valuationRange.high
        regionName=content.localRealEstate.region['name']
        regionId=content.localRealEstate.region['id']
        regionType=content.localRealEstate.region['type']
        zIndexValue=content.localRealEstate.region.zindexValue
        localRealEstateOverviewLinks=content.localRealEstate.region.links.overview
        localRealEstateForSaleByOwnerLinks=content.localRealEstate.region.links.forSaleByOwner
        localRealEstateForSaleLinks=content.localRealEstate.region.links.forSale

        return SearchResults(zpid, homeDetailsLink, mapThisHomeLink,comparablesLink,streetAddress,zipcodeAddress, cityAddress, stateAddress, latitudeAddress, longitudeAddress, amount, lastUpdated, valueChange, lowValuationRange, highValuationRange, regionName, regionId, regionType, zIndexValue, localRealEstateOverviewLinks, localRealEstateForSaleByOwnerLinks, localRealEstateForSaleLinks)
