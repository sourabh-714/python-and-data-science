Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'C:\\Python38'
>>> os.chdir("F:\DIT_DSA\Group_4\Songs")
>>> os.chdir("C:\Users\ASUS PC\Music")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> os.chdir("F:\some folder")
>>> os.chdir("C:\Program Files")
>>> os.chdir("C:\Users")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> os.chdir("F:")
>>> os.chdir("F:\new folder")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    os.chdir("F:\new folder")
OSError: [WinError 123] The filename, directory name, or volume label syntax is incorrect: 'F:\new folder'
>>> path = "F:\new folder"
>>> path
'F:\new folder'
>>> print(path)
F:
ew folder
>>> path = r"F:\new folder"
>>> print(path)
F:\new folder
>>> path
'F:\\new folder'
>>> os.chdir(r"F:\DIT_DSA\Group_4\Songs")
>>> os.listdir()
['bang-bang.mp3', 'exception_hierarchy.png', 'Faded.mp3', 'fifa world cup.mp3', 'read_write_1.png', 'song_1.mp3', 'song_2.mp3']
>>> import random
>>> random.choice(os.listdir())
'exception_hierarchy.png'
>>> random.choice(os.listdir())
'fifa world cup.mp3'
>>> random.choice(os.listdir())
'song_1.mp3'
>>> random.choice(os.listdir())
'song_1.mp3'
>>> random.choice(os.listdir())
'exception_hierarchy.png'
>>> random.choice(os.listdir())
'Faded.mp3'
>>> random.choice(os.listdir())
'bang-bang.mp3'
>>> song = random.choice(os.listdir())
>>> song
'song_2.mp3'
>>> os.startfile(song)
>>> import glob
>>> mp3_files = glob.glob("*.mp3")
>>> mp3_files
['bang-bang.mp3', 'Faded.mp3', 'fifa world cup.mp3', 'song_1.mp3', 'song_2.mp3']
>>> song = random.choice(mp3_files)
>>> os.startfile(song)
>>> x = [1,3,4,6,7,4,]
>>> random.choice(x)
7
>>> random.choice(x)
1
>>> random.randint(1,10)
7
>>> random.randint(1,10)
2
>>> random.randint(1,10)
9
>>> range(0,10)
range(0, 10)
>>> range(0,10,-1)
range(0, 10, -1)
>>> for i in range(0,10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(10,1):
	print(i)

	
>>> for i in range(10,1,-1):
	print(i)

	
10
9
8
7
6
5
4
3
2
>>> 