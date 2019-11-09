from main.services.zillow.GetSearchResults import getSearchResults
from main.classes.SearchResultClass import SearchResultClass
def run():
    myParams ={
        "zws-id":"X1-ZWz17jvxcowwln_7lwvq",
        "citystatezip": "60611",
        "address": "420 E Ohio St"
    }

    searchResult = SearchResultClass("X1-ZWz17jvxcowwln_7lwvq","60611","420 E Ohio St")
    searchResult.getSearchResultsHelper()
    print("done")
