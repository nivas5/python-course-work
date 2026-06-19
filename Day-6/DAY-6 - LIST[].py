Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
##           -------LIST-----

l = []
l = list()
l
[]
l = [1,2,3,4,5]
l
[1, 2, 3, 4, 5]
type(l)
<class 'list'>
id(l)
2336812197312
l.append(1991)
l
[1, 2, 3, 4, 5, 1991]
id(l)
2336812197312
##   .append() is used for adding new things to the list.

l = [1,32,3,'dfhjwh', [1122,423,1122], (122,3,44), {32,12,21},{1:2,2:1}, False]
l
[1, 32, 3, 'dfhjwh', [1122, 423, 1122], (122, 3, 44), {32, 12, 21}, {1: 2, 2: 1}, False]

## So, here in LIST we can use any thing like STRING, INTEGERS, TUPLES, SETS, DICTS, BOOLEAN, LIST.
## COMPLEX also can be inculdable in the LIST.

a = ['rama', 'krishna', 'arjuna']
b = ['parvathi', 'lakshmi', 'durga']

a+b
['rama', 'krishna', 'arjuna', 'parvathi', 'lakshmi', 'durga']
a[-1:-3]
[]
a[-1:]
['arjuna']

a[-1:0]
[]
a[-1:-3:-1]
['arjuna', 'krishna']
a[-1::-1]
['arjuna', 'krishna', 'rama']
b*3
['parvathi', 'lakshmi', 'durga', 'parvathi', 'lakshmi', 'durga', 'parvathi', 'lakshmi', 'durga']
b+a
['parvathi', 'lakshmi', 'durga', 'rama', 'krishna', 'arjuna']


a[0]
'rama'
a[-1]
'arjuna'
a[-3]
'rama'
a = ['rama', 'krishna', 'arjuna', 'parvathi', 'lakshmi', 'durga']
a
['rama', 'krishna', 'arjuna', 'parvathi', 'lakshmi', 'durga']
a[1::-1]
['krishna', 'rama']
a[1::2]
['krishna', 'parvathi', 'durga']
a[0::3]
['rama', 'parvathi']
a[3::-1]
['parvathi', 'arjuna', 'krishna', 'rama']
a[-2:-5:-1]
['lakshmi', 'parvathi', 'arjuna']
'lakshmi' in a
True
'nivas' in a
False
'karthikeya' not in a
True
a
['rama', 'krishna', 'arjuna', 'parvathi', 'lakshmi', 'durga']

sorted(a)
['arjuna', 'durga', 'krishna', 'lakshmi', 'parvathi', 'rama']
sorted(a,reverse=True)
['rama', 'parvathi', 'lakshmi', 'krishna', 'durga', 'arjuna']
a
['rama', 'krishna', 'arjuna', 'parvathi', 'lakshmi', 'durga']
max(a)
'rama'
min(a)
'arjuna'

a
['rama', 'krishna', 'arjuna', 'parvathi', 'lakshmi', 'durga']
a[1]
'krishna'
a[1]='radha krishna'
a
['rama', 'radha krishna', 'arjuna', 'parvathi', 'lakshmi', 'durga']
a.append('NIVAS')
a
['rama', 'radha krishna', 'arjuna', 'parvathi', 'lakshmi', 'durga', 'NIVAS']
a.insert(1,'sitaram')
a
['rama', 'sitaram', 'radha krishna', 'arjuna', 'parvathi', 'lakshmi', 'durga', 'NIVAS']

a.extend(['nnnnn', 'ggggg', 'dddddd'])
a
['rama', 'sitaram', 'radha krishna', 'arjuna', 'parvathi', 'lakshmi', 'durga', 'NIVAS', 'nnnnn', 'ggggg', 'dddddd']
a.pop()
'dddddd'
a
['rama', 'sitaram', 'radha krishna', 'arjuna', 'parvathi', 'lakshmi', 'durga', 'NIVAS', 'nnnnn', 'ggggg']
a.pop()
'ggggg'
a
['rama', 'sitaram', 'radha krishna', 'arjuna', 'parvathi', 'lakshmi', 'durga', 'NIVAS', 'nnnnn']
a.pop(-2)
'NIVAS'
a
['rama', 'sitaram', 'radha krishna', 'arjuna', 'parvathi', 'lakshmi', 'durga', 'nnnnn']
a.pop(1)
'sitaram'
a.remove('nnnnn')
a
['rama', 'radha krishna', 'arjuna', 'parvathi', 'lakshmi', 'durga']
a.remove('arjuna')
a
['rama', 'radha krishna', 'parvathi', 'lakshmi', 'durga']


del a[1]
a
['rama', 'parvathi', 'lakshmi', 'durga']
del a[]
SyntaxError: invalid syntax
## Diff btw POP and DEL is the del DELETES the data PERMANENTLY, But POP deletes TEMPORARILY.

l= [1,2,3,4,5,6,7,8,9]
l
[1, 2, 3, 4, 5, 6, 7, 8, 9]
m=l
m
[1, 2, 3, 4, 5, 6, 7, 8, 9]
m.append(1)
m
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
m.append(1991)
m
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1991]
l
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1991]
l.index(1)
0
l.index(0)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    l.index(0)
ValueError: 0 is not in list
l.index(1991)
10
l.count(2)
1
l.count(1)
2
l
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1991]
m
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1991]

n = l.copy()
n
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1991]
l
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1991]
n.append(9009)
n
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1991, 9009]
l
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1991]
n[10]='NIVAS'
n
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 'NIVAS', 9009]
n.insert(10,'nivas')
n
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 'nivas', 'NIVAS', 9009]


sum(n)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    sum(n)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
sum(l)
2037
sum(m)
2037
## SUM is used to add the integers.


## 0  0.0    ''   []   ()    set()   {}    False

any([1,2,1,0,0,0,0,0.0,0.00)]
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
any([1,2,1,0,0,0,0,0.0,0.00])
True
any([1,2,22,0,0.0,0.00,[],(),{}])
True
any([0,0.0,0.00,[],(),{}])
False
