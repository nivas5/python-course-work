'''
import random

#random.seed(10)
print(random.random())
print(random.randint(12, 20))
print(random.uniform(12, 20))

l = ['java', 'c++', 'c', 'python', 'html']

print(random.choices(l))
print(random.choices(l, k=3))

print(l)
random.shuffle(l)
print(l)

---------------------------------------------
'''
## PASSWORD
'''
import random

name = input("Enter the Name: ")
spe_char = ['!','@', '#', '$','^', '&', '*']
sample1 = random.choices(name,k=4)+random.choices(spe_char,k=2)
sample2 = (''.join(sample1)).title()

print(sample2+str(random.randint(1111,9999)))

---------------------------------------------
'''
## DATES WEEKS DAYS YEARS
'''
from datetime import date, time, datetime, timedelta

d = date.today()  ## For PRESENT DATE
print(d)
print(d.day)
print(d.month)
print(d.year)
print(d.weekday())
print(d.isoweekday())

d = date(2026,12,28) ## For DATE
print(d)

d = time(23,54,20)  ## For TIME
print(d)

d = datetime.now()  ## For both PRESENT TIME and DATE
print(d)
print(d.day)
print(d.month)
print(d.year)
print(d.weekday())
print(d.isoweekday())

print(d.hour)
print(d.minute)
print(d.second)
'''

## For FORMATTING.
'''
d = datetime.now()
print(d.strftime('%d/%m/%y'))
print(d.strftime('%d/%m/%y  %H:%M:%S'))
print(d.strftime('%d/%m/%y  %I:%M:%S %p'))
print(d.strftime('%d %b %y  %I:%M:%S %p')) 
print(d.strftime('%d %B %y  %I:%M:%S %p')) 
print(d.strftime('%a, %d %B %y  %I:%M:%S %p'))
print(d.strftime('%A, %d %B %y  %I:%M:%S %p'))

O/P:-
27/06/26
27/06/26  15:25:57
27/06/26  03:25:57 PM
27 Jun 26  03:25:57 PM
27 June 26  03:25:57 PM
Sat, 27 June 26  03:25:57 PM
Saturday, 27 June 26  03:25:57 PM
'''

## No YEARS MONTHS are work in TIMEDELTA.
'''
d = datetime.now()

d7 = d + timedelta(days=60)
print(d7)
h2 = d + timedelta(hours=2)
print(h2)
m15 = d + timedelta(minutes=15)
print(m15)
s15 = d + timedelta(seconds=15)
print(s15)

O/P:-
2026-08-26 15:32:32.461463
2026-06-27 17:32:32.461463
2026-06-27 15:47:32.461463
2026-06-27 15:32:47.461463

-----------------------------------------
'''
'''
from itertools import combinations,permutations

res1 = list(combinations('abc',2))
res2 = list(permutations('abc',2))

print([''.join(i) for i in res1])
print([''.join(i) for i in res2])

#O/P:-
#['ab', 'ac', 'bc']
#['ab', 'ac', 'ba', 'bc', 'ca', 'cb']
'''
'''
--------------------------------------------
from collections import Counter,defaultdict,deque

s = 'python programming'
l = [1,1,2,2,3,4,2,22,4,3,2,1,2,4,4,3,2,2,2]
print(Counter(s))
print(Counter(l))

#O/P:-
#Counter({'p': 2, 'o': 2, 'n': 2, 'r': 2, 'g': 2, 'm': 2, 'y': 1, 't': 1, 'h': 1, ' ': 1, 'a': 1, 'i': 1})
#Counter({2: 8, 4: 4, 1: 3, 3: 3, 22: 1})
#{'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, ' ': 1, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1}

## Counter will do the work of this whole code.
d = {}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)

d = defaultdict(int)
for i in s:
    d[i]+=1
print(d)

#O/P:-
#defaultdict(<class 'int'>, {'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, ' ': 1, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1})
------------------
d = deque([])

d.append(10)
d.append(20)
d.append(30)
d.append(40)
d.popleft()
d.popleft()
d.append(50)
d.append(60)
d.append(70)
d.popleft()
print(d)
#O/P:-
#deque([40, 50, 60, 70])
'''
