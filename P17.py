n = int(input("How many terms do you want to print? : "))
n1 = 0
n2 = 1
if(n<=0):
    print("Invalid Input!!!")
elif(n==1):
    print("Fibonacci Series : ",n1)
elif(n==2):
    print("Fibonacci Series : ",n1,",",n2)
else:
    print("Fibonacci Series : ")
    for i in range(n):
        if(i<n-1):
            print(n1,end=' , ')
        else:
            print(n1)
        n3 = n1+n2
        n1 = n2
        n2 = n3



'''                                     Output
                        How many terms do you want to print? : 1
                        Fibonacci Series :  0
                                        OR
                        How many terms do you want to print? : 2
                        Fibonacci Series :  0 , 1
                                        OR
                        How many terms do you want to print? : 10
                        Fibonacci Series : 
                        0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34
'''