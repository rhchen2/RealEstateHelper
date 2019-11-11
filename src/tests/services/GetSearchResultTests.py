from unittest import TestCase

from main.classes.SearchResultClass import SearchResultClass

class  getResultsTests(TestCase):

    def test_get(self):
        # print("test")
        zwsid = "X1-ZWz17jvxcowwln_7lwvq",
        citystatezip = "60611",
        address = "420 E Ohio St"

        searchResult = SearchResultClass(zwsid,citystatezip,address)
        searchResult.getSearchResultsHelper()

        assert searchResult.results[0].zpid == "2097525662"
        assert searchResult.results[0].homeDetailsLink == "https://www.zillow.com/homedetails/420-E-Ohio-St-STUDIO-Chicago-IL-60611/2097525662_zpid/"
        assert searchResult.results[0].mapThisHomeLink == "http://www.zillow.com/homes/2097525662_zpid/"
        assert searchResult.results[0].comparablesLink == "http://www.zillow.com/homes/comps/2097525662_zpid/"
        assert searchResult.results[0].streetAddress == "420 E Ohio St # STUDIO"
        assert searchResult.results[0].zipcodeAddress == "60611"
        assert searchResult.results[0].cityAddress == "Chicago"
        assert searchResult.results[0].stateAddress == "IL"
        assert searchResult.results[0].latitudeAddress == "41.892863"
        assert searchResult.results[0].longitudeAddress == "-87.616655"
        assert searchResult.results[0].amount == "393587"
        assert searchResult.results[0].lastUpdated == "11/08/2019"
        assert searchResult.results[0].valueChange == "-18426"
        assert searchResult.results[0].lowValuationRange == "338485"
        assert searchResult.results[0].highValuationRange == "452625"
        assert searchResult.results[0].regionName == "The Loop"
        assert searchResult.results[0].regionId == "269593"
        assert searchResult.results[0].regionType == "neighborhood"
        assert searchResult.results[0].zIndexValue == "286,700"
        assert searchResult.results[0].localRealEstateOverviewLinks == "http://www.zillow.com/local-info/IL-Chicago/The-Loop/r_269593/"
        assert searchResult.results[0].localRealEstateForSaleByOwnerLinks == "http://www.zillow.com/the-loop-chicago-il/fsbo/"
        assert searchResult.results[0].localRealEstateForSaleLinks == "http://www.zillow.com/the-loop-chicago-il/"
