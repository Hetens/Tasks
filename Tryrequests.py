
import requests

url = "https://spotify23.p.rapidapi.com/search/"

querystring = {"q":"Never gonna give you up","type":"multi","offset":"0","limit":"10","numberOfTopResults":"5"}

headers = {
	"X-RapidAPI-Key": "3064e93a75msh4290adb8a28fe61p1a8456jsn4ac87731a7a1",
	"X-RapidAPI-Host": "spotify23.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())