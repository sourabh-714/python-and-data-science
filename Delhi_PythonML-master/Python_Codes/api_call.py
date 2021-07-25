import urllib.request as url
import json

res = url.urlopen('https://api.covid19india.org/states_daily.json')
data = json.load(res)

states = data['states_daily']
