'''
n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == 0 or i == m:
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
----------------------------------------

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if j == 0 or i == 0 or (i==n-1 and j<=m) or (j==m and i>=m) or (i==m and j>=m) or (j==n-1 and i>=m):
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
-----------------FOR - J------------------

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if i == 0 or j == m or (i == n-1 and j <= m) or (j == 0 and i >= m):
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()                                               
--------------------Y----------------------

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if (i == j and i <= m) or i+j == n-1:
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
---------------------X----------------------

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if (i == j) or i+j == n-1:
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
----------------------K----------------------

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if j == 0 or (i == m and j <= m) or (i+j == n-1 and i<=m) or (i == j and i >= m):
            print("*", end=' ')

        else:
            print(' ',end = ' ')
    print()
----------------------L-----------------------


n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if j == 0 or i == n-1:
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
----------------------Z-----------------------

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or (i+j == n-1):
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
----------------------B-----------------------

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j == n-1 or i == n-1 or i == m:
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
----------------------C-----------------------

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1:
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
----------------------D----------------------

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print
----------------------E-----------------------

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or i == m:
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
-----------------------F-----------------------

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == m:
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
-----------------------H------------------------

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i ==m:
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
------------------------I------------------------ 

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == m:
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
------------------------M------------------------ 

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or (i == j and i <= m) or (i+j == n-1 and i <= m):
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
------------------------N------------------------ 

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == j:
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
------------------------O------------------------ 

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j == n-1 or i == n-1:
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
------------------------P------------------------ 

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or (j == n-1 and i <= m) or i == m:
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
------------------------R------------------------ 

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if j == 0 or (j == n-1 and i<=m) or i == 0 or i == m or (i==j and i>=m):
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
------------------------S------------------------ 

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or i==m or(j == 0 and i<=m)or(j == n-1 and i>=m):
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
-------------------------T----------------------- 

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if i == 0 or j == m:
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
------------------------U------------------------ 

n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == n-1:
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
------------------------V------------------------ 
'''
n = int(input("Enter the Size: "))
m = n//2

for i in range(n):
    for j in range(n):
        if (j == 0 and i<= m) or (j == n-1 and i<=m) or (i + j == n +1) or :
            print("*", end=' ')
        else:
            print(' ',end = ' ')
    print()
