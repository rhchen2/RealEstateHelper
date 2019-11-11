from main.services.zillow.GetSearchResults import getSearchResults
from main.classes.SearchResults import SearchResults
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
        zpid = content.zpid.string
        homeDetailsLink=content.links.homedetails.string
        mapThisHomeLink=content.links.mapthishome.string
        comparablesLink=content.links.comparables.string
        streetAddress=content.address.street.string
        zipcodeAddress=content.address.zipcode.string
        cityAddress=content.address.city.string
        stateAddress=content.address.state.string
        latitudeAddress=content.address.latitude.string
        longitudeAddress=content.address.longitude.string
        amount=content.zestimate.amount.string
        lastUpdated = content.find('last-updated').string
        valueChange=content.zestimate.valueChange.string
        lowValuationRange=content.zestimate.valuationRange.low.string
        highValuationRange=content.zestimate.valuationRange.high.string
        regionName=content.localRealEstate.region['name']
        regionId=content.localRealEstate.region['id']
        regionType=content.localRealEstate.region['type']
        zIndexValue=content.localRealEstate.region.zindexValue.string
        localRealEstateOverviewLinks=content.localRealEstate.region.links.overview.string
        localRealEstateForSaleByOwnerLinks=content.localRealEstate.region.links.forSaleByOwner.string
        localRealEstateForSaleLinks=content.localRealEstate.region.links.forSale.string

        return SearchResults(zpid, homeDetailsLink, mapThisHomeLink,comparablesLink,streetAddress,zipcodeAddress, cityAddress, stateAddress, latitudeAddress, longitudeAddress, amount, lastUpdated, valueChange, lowValuationRange, highValuationRange, regionName, regionId, regionType, zIndexValue, localRealEstateOverviewLinks, localRealEstateForSaleByOwnerLinks, localRealEstateForSaleLinks)
