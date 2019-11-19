from bs4 import BeautifulSoup

def xmlToClass(self, xmlResult):
    contents = BeautifulSoup(xmlResult ,'xml')
    findAllResults = contents.find_all("results")
    results = []
    for result in findAllResults:
        results.append(self.instaniateSearchResult(result))
    return results