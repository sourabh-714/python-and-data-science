Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello world, this is python programming..."
>>> len(text)
42
>>> text.capitalize()
'Hello world, this is python programming...'
>>> text.lower()
'hello world, this is python programming...'
>>> text.upper()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING...'
>>> text.title()
'Hello World, This Is Python Programming...'
>>> text.swapcase()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING...'
>>> text.count('o')
4
>>> text.count('o', 1,10)
2
>>> text.index('o')
4
>>> text.index('o',5)
7
>>> text.index('o',8)
25
>>> text.index('o',26)
30
>>> 'HeLLo'.swapcase()
'hEllO'
>>> text.find('o')
4
>>> text.find('o',5)
7
>>> text.find('o',8)
25
>>> text.find('o',6)
7
>>> text.find('o',26)
30
>>> text.index('z')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    text.index('z')
ValueError: substring not found
>>> text.find('z')
-1
>>> text.startswith('h')
True
>>> text.endswith('?')
False
>>> text.endswith('.')
True
>>> text.isdigit()
False
>>> text.isalpha()
False
>>> text.isprintable()
True
>>> text.islower()
True
>>> text.index('o')
4
>>> text.rindex('o')
30
>>> text.rfind('o')
30
>>> text.split()
['hello', 'world,', 'this', 'is', 'python', 'programming...']
>>> text.split(',')
['hello world', ' this is python programming...']
>>> text
'hello world, this is python programming...'
>>> wordsList = ['hello', 'world,', 'this', 'is', 'python', 'programming...']
>>> ' '.join(wordsList)
'hello world, this is python programming...'
>>> ','.join(wordsList)
'hello,world,,this,is,python,programming...'
>>> '-'.join(wordsList)
'hello-world,-this-is-python-programming...'
>>> text.center(len(text))
'hello world, this is python programming...'
>>> len(text)
42
>>> text.center(43)
' hello world, this is python programming...'
>>> text.center(44)
' hello world, this is python programming... '
>>> text.center(50)
'    hello world, this is python programming...    '
>>> text.center(80)
'                   hello world, this is python programming...                   '
>>> text.center(60)
'         hello world, this is python programming...         '
>>> text = text.center(60)
>>> text
'         hello world, this is python programming...         '
>>> text.strip()
'hello world, this is python programming...'
>>> text.lstrip()
'hello world, this is python programming...         '
>>> text.rstrip()
'         hello world, this is python programming...'
>>> text.strip()
'hello world, this is python programming...'
>>> text = text.strip()
>>> text
'hello world, this is python programming...'
>>> text.strip('.')
'hello world, this is python programming'
>>> text.strip('p')
'hello world, this is python programming...'
>>> text = text.strip('.')
>>> text
'hello world, this is python programming'
>>> text.strip('g')
'hello world, this is python programmin'
>>> text.encode()
b'hello world, this is python programming'
>>> text.replace('o','x')
'hellx wxrld, this is pythxn prxgramming'
>>> text
'hello world, this is python programming'
>>> del text[0]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    del text[0]
TypeError: 'str' object doesn't support item deletion
>>> text[0] = 'i'
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    text[0] = 'i'
TypeError: 'str' object does not support item assignment
>>> text = text.replace('o','x')
>>> text
'hellx wxrld, this is pythxn prxgramming'
>>> 
