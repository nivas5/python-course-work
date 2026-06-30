'''
-----------------------------LIST COMPRAHENSIONS----------------------------

        >>>>>>> [EXPRESSION FOR value in iterable IF condition] <<<<<<<
        
-----------------LIST - FOR LOOP IN ONE LINE-----------------

l = [1,2,3,4,5]
res1 = []

for i in l:
    res1.append(i*i)
    
res2 = [ i*i for i in l] ### We can write the above FOR LOOP in ONE LINE LIKE THIS.

print(res1, "--", res2)

-----------------STR - FOR LOOP IN ONE LINE-----------------

s = 'Python Programming'

res = [i for i in s if i in 'aeiouAEIOU']

print(res)

-----------------IF ODD - 0 EVEN - THAT NUM - FOR LOOP IN ONE LINE-----------------

s = [2, 4, 7, 12, 53, 56, 34, 23, 67, 23, 90, 79, 35]

res = []
for i in s:
    if i%2 == 0:
        res.append(i)
    else:
        res.append(0)

res2 = [i if i%2 == 0 else 0 for i in s] ### FOR LOOP in ONE LINE.

print(res,res2)

-----------------[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3] - FOR LOOP IN ONE LINE-----------------

x = []
for i in range(5):
    for j in range(1,4):
        x.append(j)
        
res = [j for i in range(5) for j in range(1,4)] ### FOR LOOP in ONE LINE.

print(x,res)

-----------------[[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]] - FOR LOOP IN ONE LINE-----------------

res = []
for i in range(5):
    temp = []
    for j in range(1, 4):
        temp.append(j)
    res.append(temp)

res2 = [[j for j in range(1,4)] for i in range(5)] ### FOR LOOP in ONE LINE.

print(res,"-", res2)

-----------------DICTIONARY - FOR LOOP IN ONE LINE-----------------
'''
res = {i:i**2 for i in range(1, 11)}

print(res)
