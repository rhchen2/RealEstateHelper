import requests


def getRentEstimates(myParams):

    url = "https://realtymole-rental-estimate-v1.p.rapidapi.com/rentalPrice"

    headers = {
        'x-rapidapi-host': "realtymole-rental-estimate-v1.p.rapidapi.com",
        'x-rapidapi-key': "daf9f60f03msh49a0d1e46d6d48ep1d0e44jsna979f9857123"
    }

    response = requests.request("GET", url, headers=headers, params=myParams)

    return response.content
