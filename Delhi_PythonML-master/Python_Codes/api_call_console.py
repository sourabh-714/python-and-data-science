Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import urllib.request as url
>>> import json
>>> res = url.urlopen("https://api.covid19india.org/states_daily.json")
>>> res
<http.client.HTTPResponse object at 0x000001BAF51D9160>
>>> json.loads(res)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    json.loads(res)
  File "C:\Python37\lib\json\__init__.py", line 341, in loads
    raise TypeError(f'the JSON object must be str, bytes or bytearray, '
TypeError: the JSON object must be str, bytes or bytearray, not HTTPResponse
>>> data = json.load(res)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    data = json.load(res)
  File "C:\Python37\lib\json\__init__.py", line 293, in load
    return loads(fp.read(),
  File "C:\Python37\lib\http\client.py", line 460, in read
    s = self._safe_read(self.length)
  File "C:\Python37\lib\http\client.py", line 610, in _safe_read
    chunk = self.fp.read(min(amt, MAXAMOUNT))
  File "C:\Python37\lib\socket.py", line 589, in readinto
    return self._sock.recv_into(b)
  File "C:\Python37\lib\ssl.py", line 1052, in recv_into
    return self.read(nbytes, buffer)
  File "C:\Python37\lib\ssl.py", line 911, in read
    return self._sslobj.read(len, buffer)
ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host
>>> res = url.urlopen("https://api.covid19india.org/states_daily.json")
>>> data = json.load(res)
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['states_daily'])
>>> states = data['states_daily']
>>> type(states)
<class 'list'>
>>> len(states)
594
>>> states[0]
{'an': '0', 'ap': '1', 'ar': '0', 'as': '0', 'br': '0', 'ch': '0', 'ct': '0', 'date': '14-Mar-20', 'dd': '0', 'dl': '7', 'dn': '0', 'ga': '0', 'gj': '0', 'hp': '0', 'hr': '14', 'jh': '0', 'jk': '2', 'ka': '6', 'kl': '19', 'la': '0', 'ld': '0', 'mh': '14', 'ml': '0', 'mn': '0', 'mp': '0', 'mz': '0', 'nl': '0', 'or': '0', 'pb': '1', 'py': '0', 'rj': '3', 'sk': '0', 'status': 'Confirmed', 'tg': '1', 'tn': '1', 'tr': '0', 'tt': '81', 'un': '0', 'up': '12', 'ut': '0', 'wb': '0'}
>>> states[-1]
{'an': '0', 'ap': '45', 'ar': '0', 'as': '0', 'br': '2', 'ch': '2', 'ct': '31', 'date': '27-Sep-20', 'dd': '0', 'dl': '0', 'dn': '0', 'ga': '0', 'gj': '10', 'hp': '0', 'hr': '16', 'jh': '9', 'jk': '7', 'ka': '79', 'kl': '2', 'la': '0', 'ld': '0', 'mh': '380', 'ml': '0', 'mn': '0', 'mp': '26', 'mz': '0', 'nl': '0', 'or': '14', 'pb': '50', 'py': '13', 'rj': '15', 'sk': '0', 'status': 'Deceased', 'tg': '9', 'tn': '80', 'tr': '2', 'tt': '937', 'un': '0', 'up': '77', 'ut': '8', 'wb': '60'}
>>> states[-3]
{'an': '0', 'ap': '6923', 'ar': '135', 'as': '0', 'br': '1527', 'ch': '173', 'ct': '2272', 'date': '27-Sep-20', 'dd': '0', 'dl': '0', 'dn': '3', 'ga': '0', 'gj': '1411', 'hp': '0', 'hr': '1515', 'jh': '974', 'jk': '1141', 'ka': '9543', 'kl': '7445', 'la': '0', 'ld': '0', 'mh': '18056', 'ml': '0', 'mn': '0', 'mp': '2310', 'mz': '30', 'nl': '0', 'or': '3922', 'pb': '1422', 'py': '368', 'rj': '2084', 'sk': '0', 'status': 'Confirmed', 'tg': '1967', 'tn': '5791', 'tr': '320', 'tt': '77531', 'un': '0', 'up': '4250', 'ut': '764', 'wb': '3185'}
>>> import pandas as pd
>>> df = pd.DataFrame(states)
>>> df.head()
  an ap ar as br ch ct       date dd dl  ... sk     status tg tn tr  tt un  up ut wb
0  0  1  0  0  0  0  0  14-Mar-20  0  7  ...  0  Confirmed  1  1  0  81  0  12  0  0
1  0  0  0  0  0  0  0  14-Mar-20  0  1  ...  0  Recovered  0  0  0   9  0   4  0  0
2  0  0  0  0  0  0  0  14-Mar-20  0  1  ...  0   Deceased  0  0  0   2  0   0  0  0
3  0  0  0  0  0  0  0  15-Mar-20  0  0  ...  0  Confirmed  2  0  0  27  0   1  0  0
4  0  0  0  0  0  0  0  15-Mar-20  0  1  ...  0  Recovered  1  0  0   4  0   0  0  0

[5 rows x 41 columns]
>>> df.tail()
     an    ap   ar    as    br   ch  ...   tr     tt un    up    ut    wb
589  23  9125  167  1595  1622  260  ...  505  92359  0  6546  1007  2955
590   0    57    0    13     5    0  ...    3   1124  0    67    11    56
591   0  6923  135     0  1527  173  ...  320  77531  0  4250   764  3185
592   0  7796   98     0  1405  166  ...  400  67437  0  5656   813  2946
593   0    45    0     0     2    2  ...    2    937  0    77     8    60

[5 rows x 41 columns]
>>> 
