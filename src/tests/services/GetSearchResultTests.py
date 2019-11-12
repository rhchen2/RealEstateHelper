from unittest import TestCase
from unittest.mock import patch

import src.main.services.zillow.GetSearchResults as GSR
from src.main.classes.SearchResultClass import SearchResultClass
from src.main.classes.SearchResults import SearchResults


def mocked_requests_get(self, *args, **kwargs):
    class MockResponse:
        def __init__(self, sResult):
            self.sResult = sResult

    if args[0] == 'https://ZillowdimashirokovV1.p.rapidapi.com/GetSearchResults.htm':
        return MockResponse(self.getTestObject())
    return MockResponse(None)

class getResultsTests(TestCase):
    @patch('src.main.services.zillow.GetSearchResults.requests.get', side_effect=mocked_requests_get)
    def test_get(self, mock_get):
        zwsid = "X1-ZWz17jvxcowwln_7lwvq",
        citystatezip = "60611",
        address = "420 E Ohio St"

        testResults = self.getTestObject()

        mock_get.return_value.ok = True

        params = {
            "zws-id": zwsid,
            "citystatezip": citystatezip,
            "address": address
        }

        results = GSR.getSearchResults(params)
        sClass = SearchResultClass(zwsid, citystatezip, address)
        searchResult = sClass.xmlToClass(results)

        print(searchResult[0].zpid)

        assert searchResult[0].zpid == testResults.zpid
        assert searchResult[0].homeDetailsLink == testResults.homeDetailsLink
        assert searchResult[0].mapThisHomeLink == testResults.mapThisHomeLink
        assert searchResult[0].comparablesLink == testResults.comparablesLink
        assert searchResult[0].streetAddress == testResults.streetAddress
        assert searchResult[0].zipcodeAddress == testResults.zipcodeAddress
        assert searchResult[0].cityAddress == testResults.cityAddress
        assert searchResult[0].stateAddress == testResults.stateAddress
        assert searchResult[0].latitudeAddress == testResults.latitudeAddress
        assert searchResult[0].longitudeAddress == testResults.longitudeAddress
        assert searchResult[0].amount == testResults.amount
        assert searchResult[0].lastUpdated == testResults.lastUpdated
        assert searchResult[0].valueChange == testResults.valueChange
        assert searchResult[0].lowValuationRange == testResults.lowValuationRange
        assert searchResult[0].highValuationRange == testResults.highValuationRange
        assert searchResult[0].regionName == testResults.regionName
        assert searchResult[0].regionId == testResults.regionId
        assert searchResult[0].regionType == testResults.regionType
        assert searchResult[0].zIndexValue == testResults.zIndexValue
        assert searchResult[0].localRealEstateOverviewLinks == testResults.localRealEstateOverviewLinks
        assert searchResult[0].localRealEstateForSaleByOwnerLinks == testResults.localRealEstateForSaleByOwnerLinks
        assert searchResult[0].localRealEstateForSaleLinks == testResults.localRealEstateForSaleLinks

    def getTestObject(self):
        zpid = "2097525662"
        homeDetailsLink = "https://www.zillow.com/homedetails/420-E-Ohio-St-STUDIO-Chicago-IL-60611/2097525662_zpid/"
        mapThisHomeLink = "http://www.zillow.com/homes/2097525662_zpid/"
        comparablesLink = "http://www.zillow.com/homes/comps/2097525662_zpid/"
        streetAddress = "420 E Ohio St # STUDIO"
        zipcodeAddress = "60611"
        cityAddress = "Chicago"
        latitudeAddress = "41.892863"
        stateAddress = "IL"
        longitudeAddress = "-87.616655"
        amount = "405962"
        lastUpdated = "11/10/2019"
        valueChange = "-2684"
        lowValuationRange = "345068"
        highValuationRange = "470916"
        regionName = "The Loop"
        regionId = "269593"
        regionType = "neighborhood"
        zIndexValue = "286,700"
        localRealEstateOverviewLinks = "http://www.zillow.com/local-info/IL-Chicago/The-Loop/r_269593/"
        localRealEstateForSaleByOwnerLinks = "http://www.zillow.com/the-loop-chicago-il/fsbo/"
        localRealEstateForSaleLinks = "http://www.zillow.com/the-loop-chicago-il/"

        return SearchResults(zpid, homeDetailsLink, mapThisHomeLink, comparablesLink, streetAddress, zipcodeAddress,
                             cityAddress, stateAddress, latitudeAddress, longitudeAddress, amount, lastUpdated,
                             valueChange, lowValuationRange, highValuationRange, regionName, regionId, regionType,
                             zIndexValue, localRealEstateOverviewLinks, localRealEstateForSaleByOwnerLinks,
                             localRealEstateForSaleLinks)
