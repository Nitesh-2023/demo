# A basic calculator that can perform basic arithmetic operations
def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def mul(a,b):
    return (a*b)
def div(a,b):
    return (a/b)
def MenuSet():
    print("Select the operation")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
    ch=int(input("Enter your choice: "))
    if (ch == 1):
        n1=int(input("Enter the First number: "))
        n2=int(input("Enter the Second number: "))
        print("The Sum: ",add(n1,n2))
    elif (ch == 2):
        n1=int(input("Enter the First number: "))
        n2=int(input("Enter the Second number: "))
        print("The Differnce: ",sub(n1,n2))
    elif (ch == 3):
        n1=int(input("Enter the First number: "))
        n2=int(input("Enter the Second number: "))
        print("The Product: ",mul(n1,n2))
    elif (ch == 4):
        n1=int(input("Enter the First number: "))
        n2=int(input("Enter the Second number: "))
        if n2 == 0:
            print("Cannot divided by zero!!!")
        else:
            print("The Quotient: ",div(n1,n2))
    else:
            print("Invalid Choice!!!")
def run():
    while True:
        c = input("Do you want to continue(y/n): ")
        if c == 'y' or c =='Y':
           MenuSet()
        else:
            break
MenuSet()
run()           