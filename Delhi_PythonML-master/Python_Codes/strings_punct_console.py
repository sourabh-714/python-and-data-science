Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import string
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> text = "Hello world, this is python. Python is a general purpose language..!!!"
>>> table = str.maketrans('', '', string.punctuation)
>>> table
{33: None, 34: None, 35: None, 36: None, 37: None, 38: None, 39: None, 40: None, 41: None, 42: None, 43: None, 44: None, 45: None, 46: None, 47: None, 58: None, 59: None, 60: None, 61: None, 62: None, 63: None, 64: None, 91: None, 92: None, 93: None, 94: None, 95: None, 96: None, 123: None, 124: None, 125: None, 126: None}
>>> text.translate(table)
'Hello world this is python Python is a general purpose language'
>>> ord
<built-in function ord>
>>> chr
<built-in function chr>
>>> chr(65)
'A'
>>> chr(97)
'a'
>>> chr(33)
'!'
>>> ord('a')
97
>>> str.maketrans('', '', 'abcd')
{97: None, 98: None, 99: None, 100: None}
>>> text.maketrans('', '', 'abcd')
{97: None, 98: None, 99: None, 100: None}
>>> str.maketrans(text)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    str.maketrans(text)
TypeError: if you give only one argument to maketrans it must be a dict
>>> str.maketrans({97: None, 98: None, 99: None, 100: None})
{97: None, 98: None, 99: None, 100: None}
>>> str.maketrans({1:'a',2:'b'})
{1: 'a', 2: 'b'}
>>> str.maketrans('','','abcdef')
{97: None, 98: None, 99: None, 100: None, 101: None, 102: None}
>>> 
