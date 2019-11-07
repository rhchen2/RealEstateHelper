from services.zillow.GetSearchResults import getSearchResults

class SearchResultClass:
    def __init__(self, zwsid, citystatezip, address):
        self.zwsid = zwsid
        self.citystatezip = citystatezip
        self.address = address
        self.results = []

    def getSearchResults(self):
        print("SEARCHRESULTS")
