Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
###      --------------------SET------------------------

s = set()
s = {1,2,3,4,5}
s
{1, 2, 3, 4, 5}
s = {0,9,12,4,56,422,11}
s
{0, 4, 422, 56, 9, 11, 12}
34 in s
False
33 in s
False
4 in s
True
0  in s
True
422 not in s
False

s = set
s = set()
s.add(1)
s
{1}
s.add(2)
s
{1, 2}
s.add(3,4,5,6)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s.add(3,4,5,6)
TypeError: set.add() takes exactly one argument (4 given)
########################

s.add(12.3)
s.add('str')
s.add(2+3j)
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
## Cause we can't add the list in SET.TypeError: unhashable type: 'list'File "<pyshell#25>", line 1, in <module>

##    Cause we can't add the list and SET in SET.

s
{1, 2, 'str', (2+3j), 12.3}
s.add(False)
s
{False, 1, 2, 'str', (2+3j), 12.3}

hash(s)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    hash(s)
TypeError: unhashable type: 'set'
hash(1)
1
hash(0)
0

girls = {'kavitha', 'anuhya', 'chandini', 'alekya'}
boys = {'sairam', 'madhav', 'bharath', 'ravi', 'vamsi'}
toppers = {'madhav', 'sairam', 'adarsh'}

girls | boys
{'madhav', 'kavitha', 'ravi', 'anuhya', 'bharath', 'chandini', 'sairam', 'alekya', 'vamsi'}
girls & boys
set()
boys & toppers
{'madhav', 'sairam'}
boys - toppers
{'vamsi', 'ravi', 'bharath'}
boys - toppers
{'vamsi', 'ravi', 'bharath'}
boys ^ toppers
{'adarsh', 'vamsi', 'ravi', 'bharath'}
boys
{'madhav', 'sairam', 'vamsi', 'ravi', 'bharath'}


{madhav}>= boys
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    {madhav}>= boys
NameError: name 'madhav' is not defined
{'madhav'}>=boys
False

a = {1,2,3,4,5,6}
a
{1, 2, 3, 4, 5, 6}
{1,2}<=a
True
(1,10,12,12}<=a
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
{1,10,12,12}<=a
False
{1, 2, 3, 4, 5, 6,7,8,9}>=a
True
girls
{'alekya', 'chandini', 'kavitha', 'anuhya'}
boys
{'madhav', 'sairam', 'vamsi', 'ravi', 'bharath'}

girls.isjoint(boys)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    girls.isjoint(boys)
AttributeError: 'set' object has no attribute 'isjoint'. Did you mean: 'isdisjoint'?
girls.isdisjoint(boys)
True
girls.isjoint(toppers)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    girls.isjoint(toppers)
AttributeError: 'set' object has no attribute 'isjoint'. Did you mean: 'isdisjoint'?
girls.isdisjoint(toppers)
True
girls.union(boys)
{'madhav', 'kavitha', 'ravi', 'anuhya', 'bharath', 'chandini', 'sairam', 'alekya', 'vamsi'}

boys
{'madhav', 'sairam', 'vamsi', 'ravi', 'bharath'}
boys.add('karthik')
boys
{'madhav', 'karthik', 'sairam', 'vamsi', 'ravi', 'bharath'}
boys.update('Nivas', 'madhu', 'rohit')
boys
{'m', 'h', 't', 'bharath', 'N', 'r', 'o', 'sairam', 'i', 'v', 'madhav', 's', 'a', 'u', 'ravi', 'd', 'karthik', 'vamsi'}
boys.update({'Nivas', 'madhu', 'rohit'})
boys
{'m', 'h', 'madhu', 'rohit', 't', 'bharath', 'N', 'r', 'o', 'sairam', 'i', 'v', 'madhav', 'Nivas', 's', 'a', 'u', 'ravi', 'd', 'karthik', 'vamsi'}
boys.pop(N)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    boys.pop(N)
NameError: name 'N' is not defined
boys.remove(N)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    boys.remove(N)
NameError: name 'N' is not defined
boys.remove('N')
boys
{'m', 'h', 'madhu', 'rohit', 't', 'bharath', 'r', 'o', 'sairam', 'i', 'v', 'madhav', 'Nivas', 's', 'a', 'u', 'ravi', 'd', 'karthik', 'vamsi'}
boys.pop('N')
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    boys.pop('N')
TypeError: set.pop() takes no arguments (1 given)
boys.pop()
'm'
boys.pop()
'h'
boys.pop()
'madhu'
boys.remove('bharath')
boys
{'rohit', 't', 'r', 'o', 'sairam', 'i', 'v', 'madhav', 'Nivas', 's', 'a', 'u', 'ravi', 'd', 'karthik', 'vamsi'}
boys.remove('bharath')
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    boys.remove('bharath')
KeyError: 'bharath'
## Because the 'bharath is already  removed so we can't remove the 'bharath' any more.

boys.discard('bharath')
boys.discard('vamsi')
boys
{'rohit', 't', 'r', 'o', 'sairam', 'i', 'v', 'madhav', 'Nivas', 's', 'a', 'u', 'ravi', 'd', 'karthik'}
boys.clear()
boys
set()
## The CLEAR deletes the whole data in the SET.

s = {'madhav', 'karthik', 'sairam', 'vamsi', 'ravi', 'bharath'}

sorted(boys)
[]
sorted(s)
['bharath', 'karthik', 'madhav', 'ravi', 'sairam', 'vamsi']
max(s)
'vamsi'
min(s)
'bharath'
s = {'madhav', 'karthik', 'sairam', 'vamsi', 'ravi', 'bharath', 'anil'}
min(s)
'anil'
max(s)
'vamsi'
len(s)
7
id(s)
2007633168640
count(s)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    count(s)
NameError: name 'count' is not defined. Did you mean: 'round'?
s.count(a)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    s.count(a)
AttributeError: 'set' object has no attribute 'count'
## In SET we can't attribute.

f = frozen({1,2,3,4,5})
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    f = frozen({1,2,3,4,5})
NameError: name 'frozen' is not defined. Did you mean: 'frozenset'?
f
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    f
NameError: name 'f' is not defined
f = frozenset({1,2,3,4,5})

f
frozenset({1, 2, 3, 4, 5})
len(f)
5
max(f)
5
min(f)
1
sum(f)
15
### The FROZENSET is a SET which is FROZED. So, we can't add or delete this SET.
