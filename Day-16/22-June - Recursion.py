'''
----------------------------RECURSION--------------------

def display(num):
    if num>10:
        return
    print(num)

    display(num+1)

display(1)

---------------IT PRINTS THE ABOVE O/P IN REVERSE--------------
def display(num):
    if num>10:
        return
    display(num+1)  ### Cause it acts as else if isntead of this print is here then it executes.
    
    print(num)

display(1)

---------------         --------------
'''
def display(s, ind):
    
    if ind == len(s):
        return
    print(s[ind], end=' ')
    
    display(s,ind+1)  
    
    print(s[ind],end=' ')

display(input("Enter a String: "), 0)
