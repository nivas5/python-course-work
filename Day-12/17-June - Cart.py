'''

---------------

-------------BILL-------------

prices = list(map(int, input("Enter the Price: ").split()))

bill = 0
for i in prices:
    bill += i

print("Bill: ", bill)

-------------CHARACTERS IN INPUT-------------

pwd = input("Enter thr string: ")

uc = lc = dc = sc = 0

for i in pwd:
    if i.isalpha():
        if i.isupper():
            uc += 1
        else:
            lc += 1
    elif i.isdigit:
        dc += 1
    else:
        sc += 1

print("UpperCase: ",uc)
print("LowerCase: ",lc)
print("Digits: ",dc)
print("Special Characters: ",sc)
print("Lenght: ",len(pwd))

-------------INDEX AND MOVIES-------------

movies = input("Enter the movies: ").split()

for i in range(len(movies)):
    print(i+1,'-', movies[i])

-------------SALARY-------------

records = eval(input())

print("Highest Salary: ", max(records.values()))
print("Lowest Salary: ", min(records.values()))
print("Average Salary: ", sum(records.values)/len(records))

###Its not working LOOK INTO IT------

-------------SCORE CALCULATOR-------------

scores = list(map(int, input("Enter the SCORE: ").split()))

tr = bd = db = 0

for i in scores:
    if i == 4 or i == 6:
        bd += 1
    elif i == 0:
        db += 1
    tr += 1

print("Total Runs: ", tr)
print("Boundaries: ", bd)
print("Dot Balls: ", db)

-------------EMAIL-------------

emails = input("Enter the EMAIL: ").split()

for i in emails:
    print(i.split('@')[1])

-------------CARD PIN-------------

attempts = 0
pin = 1234

while attempts < 3:
    epin = int(input("Enter the pin: "))
    if epin  == pin:
        print("Access Granted")
        break
    attempts += 1

else:
    print("Card Blocked")

-------------NO.OF ITEMS-------------    

c = 0
while True:
    items = input("Enter the item or exit: ")

    if items == 'exit':
        print("Total no.of items: ",c)
        break
    c += 1

-------------   -------------

at = 3
correct = 'python'

while at > 0:
    ans = input("Enter the answer: ")
    if ans == correct:
        print("YOU WIN")
        print("Live Remaining:",at)
        break
    at -= 1
else:
    print("Game Over\nLives Remaining: 0")

-------------FIRST AND LAST LETTERS COMBINE-------------

a = input("Enter a STRING: ")

x = 0
y = len(a)-1

while x <= y:
    print(a[x],a[y])
    x += 1
    y -= 1

-------------   -------------
'''

