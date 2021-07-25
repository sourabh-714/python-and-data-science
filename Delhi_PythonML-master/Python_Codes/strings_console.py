Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = "hello world"
>>> x = 'hello world'
>>> x = """hello world"""
>>> x = "hello world"
>>> print(x)
hello world
>>> x = "hello "world""
SyntaxError: invalid syntax
>>> x = 'hello "world"'
>>> print(x)
hello "world"
>>> x = "hello \"world""
SyntaxError: EOL while scanning string literal
>>> x = "hello \"world\""
>>> print(x)
hello "world"
>>> x = "hello \nworld"
>>> print(x)
hello 
world
>>> x = "hello \\n world"
>>> print(x)
hello \n world
>>> "C:\\Users\\new\\songs"
'C:\\Users\\new\\songs'
>>> r"C:\Users\new\songs"
'C:\\Users\\new\\songs'
>>> x = r"hello \n world"
>>> print(x)
hello \n world
>>> "C:\\Users\\new\\songs"
'C:\\Users\\new\\songs'
>>> x = "hello \"world\""
>>> x
'hello "world"'
>>> print(x)
hello "world"
>>> x = "hello world"
>>> x
'hello world'
>>> text = "hello world, this is python programming...!!!"
>>> len(text)
45
>>> dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> __add__  = 'hello'
>>> text[0]
'h'
>>> text[7]
'o'
>>> text[40]
'.'
>>> text[38]
'g'
>>> text[0:5]
'hello'
>>> text[0:4]
'hell'
>>> text[-10]
'm'
>>> text[-1]
'!'
>>> text[0:40:2]
'hlowrd hsi yhnpormig'
>>> text
'hello world, this is python programming...!!!'
>>> text[0:40:3]
'hlwl iiph oai.'
>>> text[:]
'hello world, this is python programming...!!!'
>>> text[0:]
'hello world, this is python programming...!!!'
>>> text[:10]
'hello worl'
>>> text[10:1]
''
>>> text[10:1:-1]
'dlrow oll'
>>> text[10:0:-1]
'dlrow olle'
>>> text[10::-1]
'dlrow olleh'
>>> text[::-1]
'!!!...gnimmargorp nohtyp si siht ,dlrow olleh'
>>> text[20:]
' python programming...!!!'
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'!!!...gni'
>>> text
'hello world, this is python programming...!!!'
>>> 
