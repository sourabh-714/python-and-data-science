Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 12
>>> b = 33
>>> c = a + b
>>> type(a)
<class 'int'>
>>> type(b)
<class 'int'>
>>> c
45
>>> a = "hello"
>>> type(a)
<class 'str'>
>>> a = 45
>>> a + b
78
>>> a - b
12
>>> a / b
1.3636363636363635
>>> a * b
1485
>>> a ** b
3597600662921626628600135655553196556866168975830078125
>>> a ** 2
2025
>>> a ** 3
91125
>>> 10 / 6
1.6666666666666667
>>> 10 // 6
1
>>> 100 // 6
16
>>> 100 / 6
16.666666666666668
>>> 10 % 6
4
>>> print(x := 10 + 20)
SyntaxError: invalid syntax
>>> a = 10
>>> id(a)
140717771613104
>>> id(20)
140717771613424
>>> a = 20
>>> b = a
>>> c = 20
>>> a is b
True
>>> b is c
True
>>> a is c
True
>>> y = 10 + 10
>>> y
20
>>> id(y)
140717771613424
>>> a is y
True
>>> b is y
True
>>> a = [2,4]
>>> b = a
>>> a
[2, 4]
>>> b
[2, 4]
>>> a == b
True
>>> a is b
True
>>> c = [2,4]
>>> a is c
False
>>> msg = "नमस्ते आप कैसे हैं ?"
>>> msg.encode()
b'\xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87 \xe0\xa4\x86\xe0\xa4\xaa \xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\x82 ?'
>>> x = msg.encode()
>>> x.decode()
'नमस्ते आप कैसे हैं ?'
>>> 
