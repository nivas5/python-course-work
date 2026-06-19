'''
-------------------------------------------
### 1, 2, 3, 4, 5
    Row

### 0, 1, 2, 3, 4
    Row - 1

### 5, 4, 3, 2, 1
    n - Row + 1

### 4, 3, 2, 1, 0
    n - Row

-------------------------------------------
n = int(input("Enter the Size:"))

for row in range(n):
    for col in range(n]):
        print(col%2, end = ' ')
    print()
---------------
n = int(input("Enter the Size:"))

for row in range(n):
    for col in range(n):
        print((row+col)%2, end = ' ')
    print()

--------------------
n = int(input("Enter the Size:"))

for row in range(n):
    for col in range(n):
        print(int(row+col<=n-1), end = ' ')
    print()

o/p:-
Enter the Size:5
1 1 1 1 1 
1 1 1 1 0 
1 1 1 0 0 
1 1 0 0 0 
1 0 0 0 0 

---------------------

n = int(input("Enter the Size:"))

for row in range(n):
    for col in range(n):
        print(int(row+col>=n-1), end = ' ')
    print()

o/p:-
Enter the Size:5
0 0 0 0 1 
0 0 0 1 1 
0 0 1 1 1 
0 1 1 1 1 
1 1 1 1 1 
------------------

n = int(input("Enter the Size:"))
c = 1

for row in range(n):
    for col in range(n):
        print(str(c).zfill(2),end = ' ')
        c += 1
    print()
------------------

n = int(input("Enter the Size:"))
c = 1

for row in range(n):
    for col in range(n):
        print(str(c).zfill(3),end = ' ')
        c += 1
    print()

o/p:-
Enter the Size:5
001 002 003 004 005 
006 007 008 009 010 
011 012 013 014 015 
016 017 018 019 020 
021 022 023 024 025 
------------------------

n = int(input("Enter the Size:"))
c = 1

for row in range(n):
    for col in range(row + 1):
        print(str(c).zfill(3),end = ' ')
        c += 1
    print()

o/p:-
Enter the Size:5
001 
002 003 
004 005 006 
007 008 009 010 
011 012 013 014 015 

---------------------
n = int(input("Enter the Size:"))

for row in range(n):
    for col in range(row + 1):
        print('*',end = ' ')
        
    print()
    
o/p:-
Enter the Size:5
* 
* * 
* * * 
* * * * 
* * * * *

---------------------
n = int(input("Enter the Size:"))


for row in range(n):
    for col in range(n - row):
        print('*',end = ' ')
        
    print()
    
o/p:-
Enter the Size:5
* * * * * 
* * * * 
* * * 
* * 
*

------------------
n = int(input("Enter the Size:"))

for row in range(n):
    for sp in range(n - row - 1):
        print(' ',end = ' ')
        
    for col in range(row + 1):
        print("*", end = " ")
        
    print()
    
o/p:-
Enter the Size:6
          * 
        * * 
      * * * 
    * * * * 
  * * * * * 
* * * * * *

--------------------
n = int(input("Enter the Size:"))

for row in range(n):
    for sp in range(row):
        print(' ',end = ' ')
        
    for col in range(n - row):
        print("*", end = " ")
        
    print()

o/p:-
Enter the Size:5
* * * * * 
  * * * * 
    * * * 
      * * 
        * 

----------------------------
n = int(input("Enter the Size:"))
m = n//2

for row in range(n):
    if row <= m:
        for col in range(row + 1):
            print('*',end = ' ')
    else:   
        for col in range(n - row):
            print("*", end = " ")
        
    print()

o/p:-
Enter the Size:10
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * 
* * * 
* * 
*

-----------------------OWN ONE-----------------------

n = int(input())

for i in range(1,n+1):
    print(" " * (n-i) + "*" * i)
for i in range(n, 1, -1):
    print(' ' * (n - i + 1) + "*" * (i-1))

### But issue is the input we are giving is only for half not for full.
### If we give input 5 it comes in 9 lines not in 5 lines.

o/p:-
5
    *
   **
  ***
 ****
*****
 ****
  ***
   **
    *

-------------------------OWN----------------------------

n = int(input())
m = n//2

for i in range(1, n+1):
    if i <= m:
        print('*' * i)
    else:
        print('*' * (n - i + 1))

o/p:-
9
*
**
***
****
*****
****
***
**
*

---------------------------------------------------------

n = int(input())

for i in range(1, n+1):
    print('*' * (n - i + 1))
for i in range(2, n+1):
    print('*' * i)

o/p:-
5
*****
****
***
**
*
**
***
****
*****

--------------------------------------------
'''

n = int(input())
m = n//2

for i in range(m+1):
    print(" " * i + "*" * (n - 2 * i))

for i in range(m - 1, -1, -1):
    print(" " * i + "*" * (n - 2 * i))
















