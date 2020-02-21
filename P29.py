num = int(input("Enter the number of rows : "))
n = int(input("Enter 0 or 1 : "))
b = bool(n)
if b==True:
    for i in range(num):
        for j in range(0,i+1):
            print("*",end="")
        print("")
elif b==False:
    for i in range(num,0,-1):
        for j in range(i):
            print("*",end="")
        print("")





'''                                             OUTPUT
                                    Enter the number of rows : 5
                                    Enter 0 or 1 : 1
                                    *
                                    **
                                    ***
                                    ****
                                    *****
'''