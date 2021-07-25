Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = {'name':'Ram','company':'TCS','dept':'IT'}
>>> data.keys()
dict_keys(['name', 'company', 'dept'])
>>> data.values()
dict_values(['Ram', 'TCS', 'IT'])
>>> data.items()
dict_items([('name', 'Ram'), ('company', 'TCS'), ('dept', 'IT')])
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    data[0]
KeyError: 0
>>> data['name']
'Ram'
>>> data['company']
'TCS'
>>> data['name'] = 'Raman'
>>> data
{'name': 'Raman', 'company': 'TCS', 'dept': 'IT'}
>>> data['sal'] = 45000
>>> data
{'name': 'Raman', 'company': 'TCS', 'dept': 'IT', 'sal': 45000}
>>> for item in data:
	print(item)

	
name
company
dept
sal
>>> for item in data:
	print(data[item])

	
Raman
TCS
IT
45000
>>> for item in data.values():
	print(item)

	
Raman
TCS
IT
45000
>>> for item in data:
	print(item,data[item])

	
name Raman
company TCS
dept IT
sal 45000
>>> data = {"names":["Ram",'Shyam','Naman'],"sal":[32000,18000,19000],"company":['TCS','IBM','TPDDL']}
>>> data
{'names': ['Ram', 'Shyam', 'Naman'], 'sal': [32000, 18000, 19000], 'company': ['TCS', 'IBM', 'TPDDL']}
>>> data['names']
['Ram', 'Shyam', 'Naman']
>>> data['company']
['TCS', 'IBM', 'TPDDL']
>>> data['sal']
[32000, 18000, 19000]
>>> data = [{'name': 'Raman', 'company': 'TCS', 'dept': 'IT', 'sal': 45000},{'name': 'Aman', 'company': 'TCS', 'dept': 'IT', 'sal': 15000},{'name': 'Anu', 'company': 'TCS', 'dept': 'HR', 'sal': 40000}]
>>> data
[{'name': 'Raman', 'company': 'TCS', 'dept': 'IT', 'sal': 45000}, {'name': 'Aman', 'company': 'TCS', 'dept': 'IT', 'sal': 15000}, {'name': 'Anu', 'company': 'TCS', 'dept': 'HR', 'sal': 40000}]
>>> data[0]
{'name': 'Raman', 'company': 'TCS', 'dept': 'IT', 'sal': 45000}
>>> data[1]
{'name': 'Aman', 'company': 'TCS', 'dept': 'IT', 'sal': 15000}
>>> data[2]
{'name': 'Anu', 'company': 'TCS', 'dept': 'HR', 'sal': 40000}
>>> data[2]['company']
'TCS'
>>> 
 RESTART: C:/Users/asus/Desktop/Corporate/TPDDL_PythonML/Python_Codes/exercise_1.py 
Enter your search : apple
>>> 
 RESTART: C:/Users/asus/Desktop/Corporate/TPDDL_PythonML/Python_Codes/exercise_1.py 
Enter your search : tv
>>> 
 RESTART: C:/Users/asus/Desktop/Corporate/TPDDL_PythonML/Python_Codes/exercise_1.py 
Enter your search : laptop
>>> 
 RESTART: C:/Users/asus/Desktop/Corporate/TPDDL_PythonML/Python_Codes/exercise_1.py 
Enter your search : iphone 10
>>> 
