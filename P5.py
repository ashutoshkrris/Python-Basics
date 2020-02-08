st = input("What do you want to swap : number or character ? \n")
st = list(st)
if(st[0]=='n' or st[0]=='N'):
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    num1 = num1+num2
    num2 = num1-num2
    num1 = num1-num2
    print("The first number is now "+str(num1))
    print("The second number is now "+str(num2))
elif(st[0]=='c' or st[0]=='C'):
    ch1 = input("Enter the first character : ")
    ch2 = input("Enter the second character : ")
    ch3 = ch2
    ch2 = ch1
    ch1 = ch3
    print("The first character is now "+ch1)
    print("The second character is now "+ch2)


'''                                          Output
                        What do you want to swap : number or character ? 
                        number
                        Enter the first number : 49 
                        Enter the second number : 91
                        The first number is now 91
                        The second number is now 49

                                            OR
                        What do you want to swap : number or character ? 
                        character
                        Enter the first character : A
                        Enter the second character : Z
                        The first character is now Z
                        The second character is now A
'''