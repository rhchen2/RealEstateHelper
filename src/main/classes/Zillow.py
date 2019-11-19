from bs4 import BeautifulSoup
from src.main.services.zillow.api import zillowSearch 
from src.main.classes.Property import *

def search(zwsid, citystatezip, address):
    result = zillowSearch({
        'zws-id': zwsid, 
        'citystatezip': citystatezip, 
        'address': address, 
    })

    contents = BeautifulSoup(result, 'xml')
    findAllResults = contents.find_all("results")
    results = []
    for result in findAllResults:
        results.append(instaniateSearchResult(result))
    return results

def instaniateSearchResult(content):
    street = content.address.street.string
    city = content.address.city.string
    zipcode = content.address.zipcode.string
    state = content.address.state.string

    latitude = float(content.address.latitude.string)
    longitude = float(content.address.longitude.string)

    amount = float(content.zestimate.amount.string)

    zpid = content.zpid.string
    zIndexValue = content.localRealEstate.region.zindexValue.string

    homeDetailsURL = content.links.homedetails.string
    mapThisHomeURL = content.links.mapthishome.string
    comparablesURL = content.links.comparables.string
    localRealEstateOverviewURL = content.localRealEstate.region.links.overview.string
    localRealEstateForSaleByOwnerURL = content.localRealEstate.region.links.forSaleByOwner.string
    localRealEstateForSaleURL = content.localRealEstate.region.links.forSale.string

    lastUpdated  =  content.find('last-updated').string
    # valueChange = content.zestimate.valueChange.string
    lowValuationRange = content.zestimate.valuationRange.low.string
    highValuationRange = content.zestimate.valuationRange.high.string
    regionName = content.localRealEstate.region['name']
    regionId = content.localRealEstate.region['id']
    regionType = content.localRealEstate.region['type']
    

    price = Price(amount, lastUpdated) # check type of lastUpdated

    location = Location(street, city, zipcode, state, coords={'latitude': latitude, 'longitude': longitude})

    # TODO: refactor to only necessary fields...
    return ZillowUnit(
        zpid, zIndexValue,
        homeDetailsURL, mapThisHomeURL, comparablesURL, 
        localRealEstateOverviewURL, localRealEstateForSaleByOwnerURL, localRealEstateForSaleURL,
        lowValuationRange, highValuationRange, regionName, regionId, regionType,
        price, location
    )

    # return SearchResults(zpid, homeDetailsLink, mapThisHomeLink,comparablesLink,streetAddress,zipcodeAddress, cityAddress, stateAddress, latitudeAddress, longitudeAddress, amount, lastUpdated, valueChange, lowValuationRange, highValuationRange, regionName, regionId, regionType, zIndexValue, localRealEstateOverviewLinks, localRealEstateForSaleByOwnerLinks, localRealEstateForSaleLinks)
