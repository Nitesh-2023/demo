ans = 'y'
while ans=='y' or ans=='Y':
    import random
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_-+=|][{};:/?1234567890"
    length = int(input("Enter the length of password: "))
    print("Here is your Password: ",end = "")
    password = ""
    for ch in range(length):
        password += random.choice(chars)
    print(password)
    ans = input("\nDo you want to generate more password (y/n)? ")
    if ans == 'n' or ans == 'N':
        break