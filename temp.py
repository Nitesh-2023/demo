'''Program that convert celcius into Franheit and vice-versa'''
def Menu():
    print("Choose one of the following: ")
    print("1.Celcius to Franheit\n2.Franheit to Celcius\n")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        c = float(input("Enter the celcius degree: "))
        f = (1.8 * c)+32
        print("Temperature in Franheit: ",f)
    elif ch == 2:
        f = float(input("Enter the Franheit degree: "))
        c = (f - 32)/1.8
        print("Temperature in Celcius: ",c)
    else:
        print("Invalid Choice!!")
def run():
    while True:
        c = input("Do you want to continue(y/n): ")
        if c == 'y' or c =='Y':
           Menu()
        else:
            break
Menu()
run()