'''
------------------------------RECURSION OPERATIONS----------------------------------
------------------- + -----------------
def sumofn(n):
    if n == 0:
         return 0
    return n + sumofn(n-1)

n = int(input("Enter the n: "))
print(sumofn(n))

------------------ * ------------------

def factorial(n):
    if n == 1:
         return 1
    return n * factorial(n-1)

n = int(input("Enter the n: "))
print(factorial(n))

------------------ SUM OF 1234 = 10 ------------------

def sumofdigits(n):
    if n == 0:
         return 0
    return n%10 + sumofdigits(n//10)

n = int(input("Enter the n: "))
print(sumofdigits(n))

------------------- BASE AND POWER -----------------

def power(base, pow):
    if pow == 0:
         return 1
    return base * power(base, pow-1)


print(power(2,5))
print(power(5,2))
print(power(100,10))

------------------- ABCD - A AB ABC ABCD -----------------

def display(s,ind):
    
    if len(s)+1 == ind:
        return
    print(s[:ind])
    display(s,ind+1)

display("abcdef MEE THATHA G LO TAPPP", 1)

------------------- ABCDE - ABC BCD CDE -----------------
'''
def display(s,ind,wid):
    
    if ind == len(s)-wid+1:
        return
    print(s[ind:ind+wid])
    display(s,ind+1,wid)

display("NAAHEROPEDDISIR!!!",0 ,3)
