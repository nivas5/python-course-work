
'''
-------------------------------FUNCTIONS------------------------------
----------------------------------------------------------------------

def iseven(num):
    if num % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

print(iseven(0))
print(iseven(99))
print(iseven(8))
print(iseven(19))

------------------PRIME NUMBERS------------------

def isprime(num):
    for i in range(2,num):
        if num % i == 0:
            return f"{num} - Not a Prime Number"
    else:
        return f"{num} - Prime Number"

for i in range(1,100): ### Or just use "print(isprime(19))".

    print(isprime(i))

------------------FACTORIAL------------------

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(f"Factorial of {n}: {fact}")
        
for i in range(10):
    factorial(i)

------------------POSITIONAL ARGUMENTS------------------

def display(name,email):
    print("Name", name)
    print("Email", email)

display('Arjun', 'arjun@gmail.com')
display('ram@gmail.com', 'Ram')

------------------DEFAULT ARGUMENTS------------------
 ### Here we can't default the first argument. Only the next ARGUMENTS can be default.

def display(name,email='',password=''):
    print("Name", name)
    print("Email", email)
    print("Password", password)

display('Arjun', 'arjun@gmail.com')
display('ram@gmail.com', 'Ram', 'Ram321')

------------------KEYWORD ARGUMENTS------------------

def display(name,email):
    print("Name:", name)
    print("Email:", email)

display(name= 'Arjun',email= 'arjun@gmail.com')
display(email= 'ram@gmail.com',name= 'Ram')

------------------TO TUPLES--------------------------

def display(*num):
    print("nums:", num)

display(1)
display(1,2,3,4,5)
display(1,4,6,7)
display(1,4)

------------------TO DICTIONNARY---------------------
'''
def display(**num):
    print("nums:", num)

display(k1 = 1)
display(k1 = 1,k2 = 2,k3 = 3,k4 = 4)
display(k1 = 1,k2 = 2)
