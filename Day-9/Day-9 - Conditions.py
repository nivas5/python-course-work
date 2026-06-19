a = input("Enter the AGE: ")
b = input("Enter the Name: ")

while a.isdigit() and b.isalpha():
        print(f"Hello '{b}' and Your AGE is: {a}")
        x = input("Enter the City: ")
        y = input("Enter the State: ")
        if x.isalpha() and y.isaplha():
            print(f"And you are from: {x}")
            print(f"And your State is: {x}")
    
        else:
            print('Please Enter the VALID INFO.!!')
            a = input("Enter the AGE: ")
            b = input("Enter the Name: ")

