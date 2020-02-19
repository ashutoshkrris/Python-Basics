def factor(x):
    print("Factors of",x,"are ",end="")
    for i in range(1,x+1):
        if x%i==0:
            if i<x:
                print(i,end=',')
            else:
                print("and",i,end='.')

num = int(input("Enter the number : "))
factor(num)



'''                                     OUTPUT
                                Enter the number : 32
                                Factors of 32 are 1,2,4,8,16,and 32.
'''