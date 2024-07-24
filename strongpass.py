ans = 'y'
while ans=='y' or ans=='Y':
    import random
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_-+=|][{};:/?1234567890"
    lett = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    symb = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    length = int(input("Enter the length of password: "))
    print("Password type:-\n1.Easy(only letter)\n2.Medium(letter and number)\n3.Strong(letter,number and special letter)\n")
    a=int(input("Enter your choice: "))
    if a==1:
        print("Here is your Password: ",end = "")
        password = ""
        for ch in range(length):
            password += random.choice(symb)
        print(password)
    elif a==2:
        print("Here is your Password: ",end = "")
        password = ""
        for ch in range(length):
            password += random.choice(lett)
        print(password)
    elif a==3:
        print("Here is your Password: ",end = "")
        password = ""
        for ch in range(length):
            password += random.choice(chars)
        print(password)
    else:
        print("Invalid choice!!!")
    ans = input("\nDo you want to generate more password (y/n)? ")
    if ans == 'n' or ans == 'N':
        break