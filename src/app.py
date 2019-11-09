from main.services.zillow.GetSearchResults import getSearchResults
from main.classes.SearchResultClass import SearchResultClass
def run():
    
    searchResult = SearchResultClass("X1-ZWz17jvxcowwln_7lwvq","60611","420 E Ohio St")
    searchResult.getSearchResultsHelper()
    print("done")
