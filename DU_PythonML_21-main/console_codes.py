Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import urllib.request as url
>>> response = url.urlopen("https://cricapi.com/api/playerStats?apikey=b7CYzlyYOrUCIIdbSlU753oGKN12&pid=28081")
>>> import json
>>> data = json.load(response)
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['pid', 'country', 'profile', 'imageURL', 'battingStyle', 'bowlingStyle', 'majorTeams', 'currentAge', 'born', 'fullName', 'name', 'playingRole', 'v', 'data', 'ttl', 'provider', 'creditsLeft'])
>>> data['profile']
"\n\nBarring Sachin Tendulkar, MS Dhoni is arguably the most popular and definitely the most scrutinised cricketer from India. He has done so coming from the cricketing backwaters, the mining state of Jharkhand, and through a home-made batting and wicketkeeping technique, and a style of captaincy that scales the highs and lows of both conservatism and unorthodoxy. Under Dhoni's captaincy, India have won the top prize in all formats: the No.1 Test ranking for 18 months starting December 2009, the 50-over World Cup in 2011 and the World Twenty20 on his captaincy debut in 2007. \n\n"
>>> data = data['data']
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['bowling', 'batting'])
>>> bat = data['batting']
>>> type(bat)
<class 'dict'>
>>> bat.keys()
dict_keys(['listA', 'firstClass', 'T20Is', 'ODIs', 'tests'])
>>> odi = bat['ODIs']
>>> type(odi)
<class 'dict'>
>>> odi.keys()
dict_keys(['50', '100', 'St', 'Ct', '6s', '4s', 'SR', 'BF', 'Ave', 'HS', 'Runs', 'NO', 'Inns', 'Mat'])
>>> odi
{'50': '66', '100': '10', 'St': '103', 'Ct': '288', '6s': '213', '4s': '752', 'SR': '88.45', 'BF': '11080', 'Ave': '51.85', 'HS': '183*', 'Runs': '9801', 'NO': '76', 'Inns': '265', 'Mat': '308'}
>>> 
==================== RESTART: F:/DU_Python/cricapi_call.py ===================
{'50': '66', '100': '10', 'St': '103', 'Ct': '288', '6s': '213', '4s': '752', 'SR': '88.45', 'BF': '11080', 'Ave': '51.85', 'HS': '183*', 'Runs': '9801', 'NO': '76', 'Inns': '265', 'Mat': '308'}
>>> 
==================== RESTART: F:/DU_Python/cricapi_call.py ===================
{'50': '33', '100': '6', 'St': '38', 'Ct': '256', '6s': '78', '4s': '544', 'SR': '59.11', 'BF': '8249', 'Ave': '38.09', 'HS': '224', 'Runs': '4876', 'NO': '16', 'Inns': '144', 'Mat': '90'}
>>> 
==================== RESTART: F:/DU_Python/cricapi_call.py ===================
{'50': '68', '100': '51', 'St': '0', 'Ct': '115', '6s': '69', '4s': '', 'SR': '', 'BF': '', 'Ave': '53.78', 'HS': '248*', 'Runs': '15921', 'NO': '33', 'Inns': '329', 'Mat': '200'}
>>> 
==================== RESTART: F:/DU_Python/cricapi_call.py ===================
Sachin Tendulkar


Sachin Tendulkar has been the most complete batsman of his time, the most prolific runmaker of all time, and arguably the biggest cricket icon the game has ever known. His batting was based on the purest principles: perfect balance, economy of movement, precision in stroke-making, and that intangible quality given only to geniuses - anticipation. If he didn't have a signature stroke - the upright, back-foot punch comes close - it's because he was equally proficient at each of the full range of orthodox shots (and plenty of improvised ones as well) and can pull them out at will.  


{'50': '68', '100': '51', 'St': '0', 'Ct': '115', '6s': '69', '4s': '', 'SR': '', 'BF': '', 'Ave': '53.78', 'HS': '248*', 'Runs': '15921', 'NO': '33', 'Inns': '329', 'Mat': '200'}
>>> res = url.urlopen("https://api.covid19india.org/states_daily.json")
>>> data = json.load(res)
>>> states = data['states_daily']
>>> len(states)
1065
>>> len(states) / 3
355.0
>>> 