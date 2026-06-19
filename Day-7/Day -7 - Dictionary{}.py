Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

##  ----------DICTIONARY-----------

d = {1:2, 33:2, 12: 43, 533:122}
d
{1: 2, 33: 2, 12: 43, 533: 122}

d = {}
d[1] = 'int'
d[12.0] = 'flo'
d
{1: 'int', 12.0: 'flo'}
d["String"] = 'str'
d[[1,2,3,4]] = 'list'
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d[[1,2,3,4]] = 'list'
TypeError: unhashable type: 'list'
d[2+3j] = 'com'
d[False] = 'bool'
d
{1: 'int', 12.0: 'flo', 'String': 'str', (2+3j): 'com', False: 'bool'}

d[1]='integer'
d
{1: 'integer', 12.0: 'flo', 'String': 'str', (2+3j): 'com', False: 'bool'}
## It is used to replace the VALUES.

d[1] = 1
d[2] = 'str'
d[3] = 12.3
d[4] = [1,2,3]
d[5] = (1,2,3)
d[6] = {1,2,3}
d[7] = {1:2, 2:1}
d[8] = (2+3j)
d[9] = True
d[10] = None
SyntaxError: multiple statements found while compiling a single statement
d[1] = 1
d[2] = 'str'
d[3] = 12.3
d[4] = [1,2,3]
d[5] = (1,2,3)
d[6] = {1,23}
d[7] = {1:2, 2:1}
d[8] = (2+3j)
d[9] = True
d[10] = None
SyntaxError: multiple statements found while compiling a single statement
d[1] = 1
d
{1: 1, 12.0: 'flo', 'String': 'str', (2+3j): 'com', False: 'bool', 2: 'str', 3: 12.3, 4: [1, 2, 3], 5: (1, 2, 3)}
d[2] = 'str'
d
{1: 1, 12.0: 'flo', 'String': 'str', (2+3j): 'com', False: 'bool', 2: 'str', 3: 12.3, 4: [1, 2, 3], 5: (1, 2, 3)}
d[3] = 12.3
d[4] = [1,2,3]
SyntaxError: multiple statements found while compiling a single statement
d[8] = (2+3j)
d
{1: 1, 12.0: 'flo', 'String': 'str', (2+3j): 'com', False: 'bool', 2: 'str', 3: 12.3, 4: [1, 2, 3], 5: (1, 2, 3), 8: (2+3j)}
d[9] = True

d[6] = {1,23}

d[10] = None
d
{1: 1, 12.0: 'flo', 'String': 'str', (2+3j): 'com', False: 'bool', 2: 'str', 3: 12.3, 4: [1, 2, 3], 5: (1, 2, 3), 8: (2+3j), 9: True, 6: {1, 23}, 10: None}


d.pop(0)
'bool'
d.pop(4)
[1, 2, 3]
d
{1: 1, 12.0: 'flo', 'String': 'str', (2+3j): 'com', 2: 'str', 3: 12.3, 5: (1, 2, 3), 8: (2+3j), 9: True, 6: {1, 23}, 10: None}
