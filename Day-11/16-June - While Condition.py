'''
####----------------------------WHILELOOP------------------------------

####-----SYNTAX-----

Int
While condition:
    statement
    upd

---------------
i = 1
while i <= 10:
    print(i)
    i += 1
---------------

i = 30

while i <= 60:
    print(i)
    i += 3
---------------

i = 50

while i <= 105:
    print(i)
    i += 5

print("YOU HAVE REACHED TO 105")

####------For reverse------

i = 29 
while i>=1:
    print(i)
    i -= 2
---------------

s = (1,2,3,4,3,55,32,44,34,213,23,87)
i = 0
while i < len(s):
    print(i,'-',s[i])
    i += 1
---------------

i = 0

while i <= 10:
    i += 1
    if i == 5:
        continue  ##Skips the VALUE.
    print(i)
---------------

i = 0

while i <= 10:
    i += 1
    if i == 5:
        break  ##It BREAKS the CODE there.
    print(i)
---------------

x = 10
y = 20
z = None

assert x!= None and y!= None and z!= None, "You need to UPDATE the XYZ Values."

### ASSERT is used for the ERROR ALERT. Intentional ERROR ALERT.

api = 'hi hello'
assert api != '', 'UPDATE the apis'


### -------SHOPPING CART PROGRAM-------

l = []

while True:
    product = input("Enter the product: ")
    price = float(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))
    l.append([product, price, quantity])
    status = input('[D]onr or [N]ext: ').upper()
    if status == 'D':
        bill = 0
        for i in l:
            print(f'{i[0]}: {i[1]} * {i[2]} = {i[1]*i[2]}')
            bill += i[1]*i[2]
        print(f"Total Bill: ${bill}")
        print("Thanks for shopping")
        break

### --------- GUESS THE NUMBER GAME ---------

number = 5

while True:
    n = int(input("Guess the Number: "))
    if number == n:
        print("Your guess is correct!!!")
        break

    else:
        print("Incorrect, Try Again")
---------------

l = [9,0,0,6,0,5,0,2,45,87,12,4,90,23,0,0,0,0,0,0,3,5]
while 0 in l:
    l.remove(0)
print(l)

'''
