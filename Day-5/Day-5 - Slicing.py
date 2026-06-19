Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
fname = 'sai'
lanme = 'ram'
fname+lanme
'sairam'
s = 'kavya kavitha anil sairam rohit'
s[0]
'k'
s[1]
'a'
s[-1]
't'
s[-10]
'i'
s[0:2:-1]
''
s[::-1]
'tihor marias lina ahtivak ayvak'
s[:5:-1]
'tihor marias lina ahtivak'
s[:4:-1]
'tihor marias lina ahtivak '
s[:1:-2]
'thrmra iaatvkav'
s[::-2]
'thrmra iaatvkavk'
s[1::-2]
'a'
s[12:-6]
'a anil sairam'
s[-12:6]
''
s[12:6:-1]
'ahtiva'
s[::2]
'kvakvtaai armrht'
s[1::2]
'ay aih nlsia oi'
anil in s
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    anil in s
NameError: name 'anil' is not defined
'anil' in s
True
'kavya
SyntaxError: unterminated string literal (detected at line 1)
'kavya' in s
True
'kavya' not in s
False
s
'kavya kavitha anil sairam rohit'
len9s0
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    len9s0
NameError: name 'len9s0' is not defined
len(s)
31
type(s)
<class 'str'>
ord(s)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    ord(s)
TypeError: ord() expected a character, but string of length 31 found
ord(m)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    ord(m)
NameError: name 'm' is not defined
ord('s')
115
ord('n')
110
ord(22)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    ord(22)
TypeError: ord() expected string of length 1, but int found
chr(22)
'\x16'
chr(100)
'd'
chr(40)
'('
sorted(s)
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'h', 'h', 'i', 'i', 'i', 'i', 'k', 'k', 'l', 'm', 'n', 'o', 'r', 'r', 's', 't', 't', 'v', 'v', 'y']
min(s)
' '
mmax(s)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    mmax(s)
NameError: name 'mmax' is not defined. Did you mean: 'max'?
max(s)
'y'


#other operation
s.upper()
'KARTHIK MANISH SAI RAM ROHIT'
s.lower()
'karthik manish sai ram rohit'
s.swapcase()
'KARTHIK MANISH SAI RAM ROHIT'
s.swapcase
<built-in method swapcase of str object at 0x00000288189DC210>
s.swapcase()
'KARTHIK MANISH SAI RAM ROHIT'
s.upper()
'KARTHIK MANISH SAI RAM ROHIT'
s.swapcase()
'KARTHIK MANISH SAI RAM ROHIT'
s.capitalize()
'Karthik manish sai ram rohit'
s.title()
'Karthik Manish Sai Ram Rohit'
s.center(10,'*')
'karthik manish sai ram rohit'
s
'karthik manish sai ram rohit'
s.center(60,'*')
'*****karthik manish sai ram rohit*****'
 s.center(10,'*')
'karthik manish sai ram rohit'
 s.center(20,'*')
'karthik manish sai ram rohit'
 s.center(60,'9')
'9999999999999999karthik manish sai ram rohit9999999999999999'
 s.ljust(60,'_')
'karthik manish sai ram rohit____________'
 s.rjust(60,'_')
'____________karthik manish sai ram rohit'
 '65'.zfill(4)
'0065'
 s.rfind()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s.rfind()
TypeError: rfind() takes at least 1 argument (0 given)
 s.rfind('t')
27
 s.find('k')
0
 s.find('a')
1
 s.find('a')
1
 s.index('t')
3
 s.rindex('t')
27
 s.count('a')
4
 s.count('m')
2
 s='       hello     world     '
 s.rstrip()
'       hello     world'
 s='python programmig'
 s.replace('python','java')
'java programmig'
 s.maketrans('aeiou','***')
{97: 42, 101: 42, 105: 42, 111: 42, 117: 42}
 s.translate(s.maketrans('aeiou','***'))
'pyth*n pr*gr*mm*g'
 s='hello 😊'
 s.encode()
b'hello \xf0\x9f\x98\x8a'