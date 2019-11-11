import unittest

import src.main.classes.SearchResultClass

def getResultsTests():
    zwsid = "X1-ZWz17jvxcowwln_7lwvq",
    citystatezip = "60611",
    address = "420 E Ohio St"

    searchResult = src.SearchResultClass(zwsid, citystatezip, address)
    searchResult.getSearchResultsHelper()

    assert searchResult.results[0].zpid == 2097525662
