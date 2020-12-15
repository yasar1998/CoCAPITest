import requests
import json


def requestSummonerData(tagLine, APItoken):
	URL = "https://api.clashofclans.com/v1/players/%23"+tagLine

	headers= {
	'Accept':"application/json", 
	'authorization':"Bearer " + APItoken
	}


	response = requests.get(URL, headers = headers)
	return response.json()

def main():
	tagL = input("Tag Line of Player without hashtag: ") #Tag Line of Player
	APIt = input("API token: ") #API token generated in website


	responseJson = requestSummonerData(tagL, APIt)
	
	print()
	print("Username for Clash of Clans: " + responseJson["name"])
	print("War Stars: " + str(responseJson["warStars"]))
	print("Best Trophies: " + str(responseJson["bestTrophies"]))

if __name__=="__main__":
	main()
