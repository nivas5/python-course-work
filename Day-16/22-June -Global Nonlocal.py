'''
----------------------------        --------------------------
-------------------------GLOBAL-------------------
### n = 10 It is GLOBAL KEYWORD which is outside of a FUNCTION.

def display():
    global n  ### Because of this even though the Variable is inside the FUNCTION it is globally used.
    n += 10   ### Using the += with 'GLOBAL' it adds with the n variable which is outside Cause their name is same.
    print("Inside Function: ", n)


n = 5
display()

print("Outside Function: ", n)

-------------------------NON LOCAL-------------------
def display():
    n = 10
                    ### NONLOCAL changes the outer variable.
    def inner(n):
        #nonlocal n ### NONLOCAL is used for function inside function. So, using it n = 20 is for both outer and inner funtions.
        n += 10
        print("Inside Function: ", n)
    inner(n)
    print("Outside Function: ", n)


display()

-------------------------NON LOCAL-------------------
def display():
    course = 'Java FullStack'
    print('Starting:', course)
                    
    def change():
        nonlocal course     ### NONLOCAL used in inner function that changes the outer variable.
        course = 'Python FullStack'
        print('Starting:', course)
        
    change()
    
    print("Outside Function: ", course)

display()

-------------------------NON LOCAL-------------------
s = 'Python'

print(len(s))  ### Here it works as a built-in function.

len = 10    ### If we use a built-in function as a variable it looses its character and converts as a VARIABLE.
print(len)

-------------------------NON LOCAL-------------------
'''
### int, float, complex, str, tuple, bool - THE INSIDE VARIABLE DONT CHANGE THE OUTSIDE ONE.

### list, set, dict  - THE INSIDE CHANGES OUTSIDE.

def update(n):
    n += 1
    print("Inside: ",n)

n = 10.4 + 3j
update(n)
print("Outside: ",n)
