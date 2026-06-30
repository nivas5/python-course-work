'''
----------------------------  LAMBDA  -------------------------

-------------------------

wish = lambda name: f'Welcome to the course, {name}'

print(wish('chandhini'))
print(wish('sarayu'))

------------- GREATEST NUMBER -------------

greater = lambda a, b: a if a>b else b

print(greater(10, 3))
print(greater(1, 34))

------------- AVERAGE -------------

avg = lambda a, b, c: (a+b+c)/3

print(avg(10, 3, 9))
print(avg(1, 34, 69))
print(avg(40, 50, 60))

-------------  LIST, SET, DICT, FILTER, MAP, REDUCE  -------------

from functools import reduce

l = [1,2,3,4,5] ### CAN USE () OR {} ALSO.
res1 = list(map(lambda i : i +10, l))   ### MAP
print(res1)

s = [23, 45, 12, 65, 4]
res2 = list(filter(lambda i: i%3 == 0, s)) ### FILTER
print(res2)

k = [10, 20, 30, 40]
res3 = reduce(lambda sum, i: sum+i, k)   ### REDUCE
print(res3)

a = {'laptop': 50000, 'phone': 100000, 'charger': 2000 , 'mouse': 800}  ### CAN USE () OR {} ALSO.
res4 = dict(map(lambda i : (i[0], i[1]+i[1]*0.18), a.items()))   ### MAP
print(res4)

b = {'laptop': 0, 'phone': 10, 'charger': 2 , 'mouse': 0} ### CAN USE () OR {} ALSO.
res5 = list(filter(lambda i : b[i] != 0, b))   ### FILTER
print(res5)

h2l = dict(sorted(a.items(),key = lambda i: i[1], reverse = True))
print(h2l)

l2h = dict(sorted(a.items(),key = lambda i: i[1]))
print(l2h)

----------------------------------------

def reels():
    l = ['1..50','51..100','101..150','151..200','201..250','251..300']
    for i in range(len(l)):
        yield l[i]
r = reels()

#print(next(r))
#print(next(r))
#print(next(r))
#print(next(r))
#print(next(r))
#print(next(r))   INSTEAD THESE WE USE WHILE LOOP.

while True:
    try:
        print(next(r))
    except StopIteration:
        print("End of the Reels")
        break
   
-------------- FACTORS - GENERATORS-------------

def factors(n):
    return [i for i in range(1,n+1) if n%i == 0]

def generators(res):
    for i in res:
        yield i.from_bytes

res = factors(50)
f = generators(res)

for i in range(len(res)):
    print(next(f))
    
-------------- FIBANOCCI - GENERATORS-------------
'''
def fib(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    elif n>2:
        res = [0,1]
        a,b = 0,1
        for i in range(n-2):
            c=a+b
            res.append(c)
            a,b=b,c
        return res

def generators(res):
    for i in res:
        yield i

res = fib(13)
f = generators(res)

