import urllib.request as url
import json

response = url.urlopen("https://cricapi.com/api/playerStats?apikey=b7CYzlyYOrUCIIdbSlU753oGKN12&pid=35320")
data = json.load(response)

print(data["name"])
print(data["profile"])

data = data['data']
bat = data['batting']
odi = bat['tests']
print(odi)
