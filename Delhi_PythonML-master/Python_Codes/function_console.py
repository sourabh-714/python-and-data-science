Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sayHello():
	print("Hello User")

	
>>> def sayBye():
	print("Bye User")

	
>>> greet = {1 : sayHello(), 2 : sayBye()}
Hello User
Bye User
>>> greet[1]
>>> greet = {1 : sayHello, 2 : sayBye}
>>> sayHello()
Hello User
>>> sayHello
<function sayHello at 0x000001C00C2C4598>
>>> greet
{1: <function sayHello at 0x000001C00C2C4598>, 2: <function sayBye at 0x000001C009CAC1E0>}
>>> greet[1]
<function sayHello at 0x000001C00C2C4598>
>>> greet[1]()
Hello User
>>> greet[2]()
Bye User
>>> def calc(x,y):
	z1 = x + y
	z2 = x - y
	return z1
	return z2

>>> calc(4,5)
9
>>> def calc(x,y):
	z1 = x + y
	z2 = x - y
	return z1,z2

>>> calc(4,5)
(9, -1)
>>> x = '10'
>>> y = '20'
>>> x + '+' + y
'10+20'
>>> x + '-' + y
'10-20'
>>> x + '/' + y
'10/20'
>>> x + '*' + y
'10*20'
>>> eval('10*20')
200
>>> eval('10*20+23/45/676*22-(34+54)')
112.01663379355688
>>> 
