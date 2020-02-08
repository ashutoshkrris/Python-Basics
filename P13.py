num = int(input("Enter the number : "))
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            print(num,"is not a prime number.")
            break
    else:
        print(num,"is a prime number.")
else:
    print("Enter number greater than",num)


'''                                     Output
                                Enter the number : 1
                                Enter number greater than  1
                                        OR
                                Enter the number : 13
                                13 is a prime number.        
'''
