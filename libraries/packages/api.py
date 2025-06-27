import requests
import json
response=requests.get("http://itunes.apple.com/search?entity=song&limit=5&term=weezer");

x=response.json();#x behaves as a dictionary
for i in x["results"]:
    print(i["trackName"]);