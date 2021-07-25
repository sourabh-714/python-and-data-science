Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = []
>>> type(x)
<class 'list'>
>>> x[0] = 10
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x[0] = 10
IndexError: list assignment index out of range
>>> x = [10,20,30,11,21,34,27,1,9]
>>> x[0]
10
>>> x[0:4]
[10, 20, 30, 11]
>>> x[4:0:-1]
[21, 11, 30, 20]
>>> x = [10,20,30,11,21,34,27,1,9,'hi','hey',120.54]
>>> x = []
>>> x.append(5)
>>> x
[5]
>>> x.append(10)
>>> x
[5, 10]
>>> x.append(11)
>>> x.append(10\)
	 
SyntaxError: unexpected character after line continuation character
>>> x.append(10)
>>> x.append(20)
>>> x.append(7)
>>> x
[5, 10, 11, 10, 20, 7]
>>> x.pop()
7
>>> x
[5, 10, 11, 10, 20]
>>> x.pop()
20
>>> x.pop()
10
>>> x
[5, 10, 11]
>>> x.insert(3,45)
>>> x
[5, 10, 11, 45]
>>> x.insert(1,4)
>>> x
[5, 4, 10, 11, 45]
>>> x.pop(2)
10
>>> x
[5, 4, 11, 45]
>>> x[2] = 10
>>> x
[5, 4, 10, 45]
>>> x.append(21,22,56,1,3,43,19)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    x.append(21,22,56,1,3,43,19)
TypeError: append() takes exactly one argument (7 given)
>>> x.append([21,22,56,1,3,43,19])
>>> x
[5, 4, 10, 45, [21, 22, 56, 1, 3, 43, 19]]
>>> x.pop()
[21, 22, 56, 1, 3, 43, 19]
>>> x
[5, 4, 10, 45]
>>> x.extend([21,22,56,1,3,43,19])
>>> x
[5, 4, 10, 45, 21, 22, 56, 1, 3, 43, 19]
>>> x.insert(3, [45,22,23,15])
>>> x
[5, 4, 10, [45, 22, 23, 15], 45, 21, 22, 56, 1, 3, 43, 19]
>>> x.pop(3)
[45, 22, 23, 15]
>>> x
[5, 4, 10, 45, 21, 22, 56, 1, 3, 43, 19]
>>> x.remove(11)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    x.remove(11)
ValueError: list.remove(x): x not in list
>>> x.remove(10)
>>> x
[5, 4, 45, 21, 22, 56, 1, 3, 43, 19]
>>> x.index(22)
4
>>> sorted(x)
[1, 3, 4, 5, 19, 21, 22, 43, 45, 56]
>>> x
[5, 4, 45, 21, 22, 56, 1, 3, 43, 19]
>>> x.sort()
>>> x
[1, 3, 4, 5, 19, 21, 22, 43, 45, 56]
>>> x.sort(reverse=True)
>>> x
[56, 45, 43, 22, 21, 19, 5, 4, 3, 1]
>>> x = [56, 45, 43, 22, 21, 19, 5, 4, 3, 1,'hi']
>>> sorted(x)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    sorted(x)
TypeError: '<' not supported between instances of 'str' and 'int'
>>> x = [['Ram',45000],['Aman',23000],['Kunal',41000],['Vijay',19000]]
>>> sorted(x)
[['Aman', 23000], ['Kunal', 41000], ['Ram', 45000], ['Vijay', 19000]]
>>> sorted(x, key = lambda i : i[1])
[['Vijay', 19000], ['Aman', 23000], ['Kunal', 41000], ['Ram', 45000]]
>>> sorted(x, key = lambda i : i[1], reverse=True)
[['Ram', 45000], ['Kunal', 41000], ['Aman', 23000], ['Vijay', 19000]]
>>> max([3,4,1,2,3,6,7,8,89,54,4])
89
>>> max(x)
['Vijay', 19000]
>>> max(x, key = lambda i : i[1])
['Ram', 45000]
>>> x = [['Ram','Shyam','Kunal','Vijay'],[23000,34000,15000,21000]]
>>> sorted(x)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    sorted(x)
TypeError: '<' not supported between instances of 'int' and 'str'
>>> x[1]
[23000, 34000, 15000, 21000]
>>> sorted(x[1])
[15000, 21000, 23000, 34000]
>>> x = []
>>> for i in range(1,1000):
	if i % 2 == 0:
		x.append(i)

		
>>> x = []
>>> for i in range(1,50):
	if i % 2 == 0:
		x.append(i)

		
>>> x
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> for i in range(1,50):
	if i % 2 != 0:
		x.append(i)

		
>>> x
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
>>> x = []
>>> for i in range(1,50):
	if i % 2 != 0:
		x.append(i)

		
>>> x
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
>>> x = [i for i in range(1,50)]
>>> 
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> x = [i for i in range(1,50) if i % 2 != 0]
>>> x
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
>>> x = [i**2 for i in range(1,10)]
>>> x
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> x.append([i**3 for i in range(1,10)])
>>> x
[1, 4, 9, 16, 25, 36, 49, 64, 81, [1, 8, 27, 64, 125, 216, 343, 512, 729]]
>>> x = [['Ram','Shyam','Kunal','Vijay'],[23000,34000,15000,21000]]
>>> for i in range(len(x))"
SyntaxError: EOL while scanning string literal
>>> for i in range(len(x)):
	print(x[0][i], x[1][i])

	
Ram 23000
Shyam 34000
>>> for i in range(len(x[0])):
	print(x[0][i], x[1][i])

	
Ram 23000
Shyam 34000
Kunal 15000
Vijay 21000
>>> x = [4,5,3,5,6]
>>> x.insert(7,10)
>>> x
[4, 5, 3, 5, 6, 10]
>>> 
