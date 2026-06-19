Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
##         String Functions

s = 'python language'
s
'python language'

s.stratswith('py')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s.stratswith('py')
AttributeError: 'str' object has no attribute 'stratswith'. Did you mean: 'startswith'?
s.startswith('py')
True
s.endswith('uage')
True

'abc'.isalpha()
True
'7897'.isalpha()
False
'asdfsfge'.isalnum()
True
'1425'.isalnum()
True
'ssdcshg56567'.isalnum()
True
'bdvch _+756564'.isalnum()
False
## .isalnum() accepts the all numbers and alphabets, But not the SPECIAL CHAR.

'nbvcc'.isupper()
False
'JKHFGDFG'.isupper()
True
'Ngusgdudcc'.isupper()
False
'6354'.isupper()
False
'jgb'.islower()
True
'CCHG'.islower()
False
'    wgbebge   '.isspace()
False
'    '.isspace()
True
'Acv Bjjhgjg Chgbub'.istitle()
True
'CDD GFGVF jhGBG'.istitle()
False

'my_var'.isidentifier()
True
'my@var'.isidentifier()
False
'654676'.isdigit()
True
'ghfchgdd'.isdigit()
False
'76756.86'.isdigit()
False
'6576'.isdecimal()
True
'786.87678'.isdecimal()
False
'fgf'.isdecimal()
False
'_sbdcc12'.isidentifier()
True
