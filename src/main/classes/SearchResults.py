class SearchResults:
    def __init__(self, zpid, homeDetailsLink, mapThisHomeLink,comparablesLink,streetAddress,zipcodeAddress, cityAddress, stateAddress, latitudeAddress, longitudeAddress, amount, lastUpdated, valueChange, lowValuationRange, highValuationRange, regionName, regionId, regionType, zIndexValue, localRealEstateOverviewLinks, localRealEstateForSaleByOwnerLinks, localRealEstateForSaleLinks):
        self.zpid = zpid
        self.homeDetailsLink=homeDetailsLink
        self.mapThisHomeLink=mapThisHomeLink
        self.comparablesLink=comparablesLink
        self.streetAddress=streetAddress
        self.zipcodeAddress=zipcodeAddress
        self.cityAddress=cityAddress
        self.stateAddress=stateAddress
        self.latitudeAddress=latitudeAddress
        self.longitudeAddress=longitudeAddress
        self.amount=amount
        self.lastUpdated=lastUpdated
        self.valueChange=valueChange
        self.lowValuationRange=lowValuationRange
        self.highValuationRange=highValuationRange
        self.regionName=regionName
        self.regionId=regionId
        self.regionType=regionType
        self.zIndexValue=zIndexValue
        self.localRealEstateOverviewLinks=localRealEstateOverviewLinks
        self.localRealEstateForSaleByOwnerLinks=localRealEstateForSaleByOwnerLinks
        self.localRealEstateForSaleLinks=localRealEstateForSaleLinks

    def printResults(self):
        result = {}
        result['zpid'] = self.zpid
        result['lastUpdated'] = self.lastUpdated
        print(result)
