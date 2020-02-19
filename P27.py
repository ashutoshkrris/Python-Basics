def add(x,y):
    print("Sum of",x,"and",y,"is",x+y)
    return

def sub(x,y):
    print("Difference of",x,"and",y,"is",x-y)

def mul(x,y):
    print("Product of",x,"and",y,"is",x*y)

def div(x,y):
    print("Division of",x,"and",y,"is",x/y)
    

print("This is a basic Calculator.")
while(True):
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    ch = int(input("Choose an operation(1/2/3/4/5) to perform : "))
    if(ch==1):
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        add(num1,num2)
    elif(ch==2):
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        sub(num1,num2)
    elif(ch==3):
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        mul(num1,num2)
    elif(ch==4):
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        div(num1,num2)
    elif(ch==5):
        print("Exiting the program!!!")
        break
    else:
        print("Invalid Choice!!!")



'''                                OUTPUT
                        This is a basic Calculator.
                        1. Addition
                        2. Subtraction
                        3. Multiplication
                        4. Division
                        5. Exit
                        Choose an operation(1/2/3/4/5) to perform : 3
                        Enter the first number : 4
                        Enter the second number : 5
                        Product of 4 and 5 is 20
                        1. Addition
                        2. Subtraction      
                        3. Multiplication
                        4. Division
                        5. Exit
                        Choose an operation(1/2/3/4/5) to perform : 5
                        Exiting the program!!!
'''