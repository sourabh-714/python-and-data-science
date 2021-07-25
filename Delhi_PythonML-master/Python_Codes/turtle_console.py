Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> user_1 = {'batman','kgf','bala','thor','kahani','lucy','raw','uri'}
>>> user_2 = {'matrix','batman','kgf','thor','raw','batla house','the ring','golmaal'}
>>> user_1.intersection(user_2)
{'raw', 'thor', 'kgf', 'batman'}
>>> user_2.union(user_1)
{'the ring', 'batla house', 'golmaal', 'thor', 'batman', 'matrix', 'kgf', 'bala', 'uri', 'kahani', 'raw', 'lucy'}
>>> user_1.difference(user_2)
{'kahani', 'lucy', 'uri', 'bala'}
>>> import turtle
>>> t = turtle.Pen()
>>> t.shape('turtle')
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.reset()
>>> for i in range(4)"
SyntaxError: EOL while scanning string literal
>>> for i in range(4):
	t.forward(100)
	t.left(90)

	
>>> t.reset()
>>> for i in range(30):
	t.forward(2*i)
	t.left(90)

	
>>> t.reset()
>>> for i in range(50):
	t.circle(4*i)
	t.left(90)

	
>>> t.reset()
>>> for i in range(50):
	if i % 2 == 0:
		t.circle(4*i)
		t.left(90)

		
Traceback (most recent call last):
  File "<pyshell#30>", line 3, in <module>
    t.circle(4*i)
  File "C:\Python37\lib\turtle.py", line 1990, in circle
    self.speed(speed)
  File "C:\Python37\lib\turtle.py", line 2174, in speed
    self.pen(speed=speed)
  File "C:\Python37\lib\turtle.py", line 2459, in pen
    self._update()
  File "C:\Python37\lib\turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python37\lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python37\lib\tkinter\__init__.py", line 744, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> t.reset()
>>> turtle.RawPen()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    turtle.RawPen()
  File "C:\Python37\lib\turtle.py", line 2538, in __init__
    raise TurtleGraphicsError("bad canvas argument %s" % canvas)
turtle.TurtleGraphicsError: bad canvas argument None
>>> import turtle
>>> turtle.RawPen()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    turtle.RawPen()
  File "C:\Python37\lib\turtle.py", line 2538, in __init__
    raise TurtleGraphicsError("bad canvas argument %s" % canvas)
turtle.TurtleGraphicsError: bad canvas argument None
>>> 
