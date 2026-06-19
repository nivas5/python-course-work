Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

### ----------TUPLE---------

t = ()
t = tuple()
type(t)
<class 'tuple'>
t = (1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t(1)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    t(1)
TypeError: 'tuple' object is not callable
t = (1)
t
1
t = (1,)
t
(1,)
t =()
type(t)
<class 'tuple'>
t = (1,2,3,4)
t = t+(4,5)
t
(1, 2, 3, 4, 4, 5)

(1, 2, 3)*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)

t = (1,2,3,4,5,6,7,8,9,0)
t[0]
1
t[1]
2
t[-1]
0
t[-5]
6
t[:4]
(1, 2, 3, 4)
t[1:-1]
(2, 3, 4, 5, 6, 7, 8, 9)
t[-1:-5:-1]
(0, 9, 8, 7)
t
(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
2 in t
True
3 in t
True
10 in t
False
1990 not in t
True
t
(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

t.index(3)
2
t.index(10)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    t.index(10)
ValueError: tuple.index(x): x not in tuple
t.index(-1)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    t.index(-1)
ValueError: tuple.index(x): x not in tuple
t.index(5)
4
t.count(2)
1
t.count(00)
1
t.count(10)
0
min(t)
0
max(t)
9
len(t)
10

any((1,0))
True
any((0,False))
False
any((False,1,0,0.00,12,144))
True
all((1,0))
False
all((1,23))
True
all((0,''))
False

a = (1,2,3,4,5)
a
(1, 2, 3, 4, 5)
w,x,y,z = a
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    w,x,y,z = a
ValueError: too many values to unpack (expected 4)
w,x,y,z,o = a
w
1
x
2
y
3
o
5
a
(1, 2, 3, 4, 5)
## We can assign the values to other variables from the one which have multiple  values of variables.

t = (1, 2, 3,[2,4,0,55],"NIVAS",(92,4,554,33), False, None,12.3,{1,3,2}, {1:2, 3:4}, 4, 5, 6, 7, 8, 9, 0)
t
(1, 2, 3, [2, 4, 0, 55], 'NIVAS', (92, 4, 554, 33), False, None, 12.3, {1, 2, 3}, {1: 2, 3: 4}, 4, 5, 6, 7, 8, 9, 0)
t[3]
[2, 4, 0, 55]
t[0]
1
t[3]=12
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    t[3]=12
TypeError: 'tuple' object does not support item assignment
t[3].12
SyntaxError: invalid syntax
t[3].append(12)
t
(1, 2, 3, [2, 4, 0, 55, 12], 'NIVAS', (92, 4, 554, 33), False, None, 12.3, {1, 2, 3}, {1: 2, 3: 4}, 4, 5, 6, 7, 8, 9, 0)

##  We can't append or add the values to TUPLE cause it is IMMUTABLE.