Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> even = []
>>> for i in range(1,51):
	if i % 2 == 0:
		even.append(i)

		
>>> even
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> numbers = [i for i in range(1,10)]
>>> numbers
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> numbers = [i for i in range(1,51) if i % 2 == 0]
>>> numbers
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> stopwords = ['is','am','are','the','that']
>>> text = ["hello","how","are","you","and","how","is","your","job","that","you","did"]
>>> text
['hello', 'how', 'are', 'you', 'and', 'how', 'is', 'your', 'job', 'that', 'you', 'did']
>>> removed = [item for item in text if item not in stopwords]
>>> removed
['hello', 'how', 'you', 'and', 'how', 'your', 'job', 'you', 'did']
>>> x = {x : [x**2 for x in range(1,10)]}
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    x = {x : [x**2 for x in range(1,10)]}
NameError: name 'x' is not defined
>>> x = {x : x**2 for x in range(1,10)}
>>> x
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> numbers = [i for i in range(1,10)]
>>> numbers
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> numbers = (i for i in range(1,10))
>>> numbers
<generator object <genexpr> at 0x0000027E8F717C00>
>>> for i in numbers:
	print(i)

	
1
2
3
4
5
6
7
8
9
>>> def add():
	x = 10
	y = 33
	print(x+y)

	
>>> add()
43
>>> add
<function add at 0x0000027E8F73C950>
>>> a = add
>>> a
<function add at 0x0000027E8F73C950>
>>> a()
43
>>> def add():
	x = 10
	y = 33
	return x + y

>>> def add():
	x = 10
	y = 33
	z = x + y
	return z

>>> value = add()
>>> v = add()
>>> 
>>> v
43
>>> z
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> v
43
>>> add
<function add at 0x0000027E8F73CA60>
>>> add()
43
>>> a = 43
>>> a.imag
0
>>> add().imag
0
>>> 
