num = int(input("Enter the number : "))
fact = 1
if(num>1):
    for i in range(1,num+1):
        fact = fact*i
    print("Factorial of",num,"is",fact)


'''                                 Output
                            Enter the number : 5
                            Factorial of 5 is 120

'''