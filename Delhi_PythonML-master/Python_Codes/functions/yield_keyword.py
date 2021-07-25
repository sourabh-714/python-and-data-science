Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sayHello():
	print("Hello User")

	
>>> sayHello()
Hello User
>>> msg = sayHello()
Hello User
>>> print(msg)
None
>>> def sayHello():
	print("Hello User")
	return None

>>> sayHello()
Hello User
>>> msg = sayHello()
Hello User
>>> print(msg)
None
>>> def sayHello():
	print("Hello User")

	
>>> def sayHello():
	return "Hello User"

>>> sayHello()
'Hello User'
>>> msg = sayHello()
>>> msg
'Hello User'
>>> a,b = 10,12
>>> a
10
>>> b
12
>>> data = name,age,sal = 'Ram',34,45000
>>> data
('Ram', 34, 45000)
>>> name
'Ram'
>>> age
34
>>> sal
45000
>>> data
('Ram', 34, 45000)
>>> a,b,c = data
>>> a
'Ram'
>>> b
34
>>> c
45000
>>> def counter():
	x = 0
	return x + 1

>>> counter()
1
>>> counter()
1
>>> def counter():
	x = 0
	while True:
		x += 1
		return x

	
>>> counter()
1
>>> x = 0
>>> def counter():
	return x += 1
SyntaxError: invalid syntax
>>> def counter():
	x = x + 1
	return x

>>> x = 0
>>> def counter():
	x = x + 1
	return x

>>> counter()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    counter()
  File "<pyshell#50>", line 2, in counter
    x = x + 1
UnboundLocalError: local variable 'x' referenced before assignment
>>> def counter():
	x = 0
	while True:
		x += 1
		yield x

		
>>> counter()
<generator object counter at 0x000001D9EC257B88>
>>> my_counter = counter()
>>> my_counter
<generator object counter at 0x000001D9EC289A20>
>>> next(my_counter)
1
>>> next(my_counter)
2
>>> next(my_counter)
3
>>> next(my_counter)
4
>>> next(my_counter)
5
>>> for i in range(10):
	print(next(my_counter))

	
6
7
8
9
10
11
12
13
14
15
>>> def counter():
	x = 0
	x += 1
	yield x

	
>>> my_counter = counter()
>>> my_counter
<generator object counter at 0x000001D9EC257B88>
>>> next(my_counter)
1
>>> next(my_counter)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    next(my_counter)
StopIteration
>>> def counter():
	x = 0
	yield x
	
KeyboardInterrupt
>>> yield x
SyntaxError: 'yield' outside function
>>> def counter():
	x = 0
	yield x
	x += 1

	
>>> my_counter = counter()
>>> next(my_counter)
0
>>> next(my_counter)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    next(my_counter)
StopIteration
>>> def counter():
	x = 0
	for i in range(5):
		x += 1
		print(x)

		
>>> counter()
1
2
3
4
5
>>> def counter():
	x = 0
	for i in range(5):
		x += 1
		yield x

		
>>> my_counter = counter()
>>> next(my_counter)
1
>>> next(my_counter)
2
>>> next(my_counter)
3
>>> next(my_counter)
4
>>> next(my_counter)
5
>>> next(my_counter)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    next(my_counter)
StopIteration
>>> my_counter
<generator object counter at 0x000001D9EC257B88>
>>> def counter():
	x = 0
	for i in range(5):
		x += 1
		yield x

		
>>> my_counter = counter()
>>> for i in my_counter:
	print(i)

	
1
2
3
4
5
>>> def counter():
	x = 0
	for i in range(5):
		x += 2
		yield x

		
>>> my_counter = counter()
>>> for i in my_counter:
	print(i)

	
2
4
6
8
10
>>> numbers = [i for i in range(4,10)]
>>> numbers
[4, 5, 6, 7, 8, 9]
>>> numbers = [i for i in range(4,41) if i % 2 == 0]
>>> numbers
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
>>> 
