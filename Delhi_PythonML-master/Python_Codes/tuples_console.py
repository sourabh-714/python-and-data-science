Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 3,4,5,7,1,2,4,6
>>> type(x)
<class 'tuple'>
>>> x = (3,4,5,7,1,2,4,6)
>>> x[0:5]
(3, 4, 5, 7, 1)
>>> x[-1:-5:-1]
(6, 4, 2, 1)
>>> x[0]
3
>>> x[0] = 30
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x[0] = 30
TypeError: 'tuple' object does not support item assignment
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> x = 10
>>> x = 10,
>>> type(x)
<class 'tuple'>
>>> x
(10,)
>>> 
