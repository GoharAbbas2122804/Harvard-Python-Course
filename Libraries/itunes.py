import requests
import sys
import json #this comes with python already no need to install it 

if len(sys.argv) != 2:
    print("FUCK OFF!")
    sys.exit()

# if we have the exact two argvs then we call the server to get a specific response and display it 
# lets call the api
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1] ) 
# print(json.dumps(response.json() , indent=2))
resJson = response.json()
# print(resJson["resultCount"])
for songs in resJson["results"]:
    print(songs["trackName"])
 