import requests


def getSearchResults(myParams):

    response = requests.post("https://ZillowdimashirokovV1.p.rapidapi.com/GetSearchResults.htm",
            headers={
                "X-RapidAPI-Host": "ZillowdimashirokovV1.p.rapidapi.com",
                "X-RapidAPI-Key": "daf9f60f03msh49a0d1e46d6d48ep1d0e44jsna979f9857123",
                "Content-Type": "application/x-www-form-urlencoded"
                },
            params=myParams
            )

    return response.content
