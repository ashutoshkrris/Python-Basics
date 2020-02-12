def HCF(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if(x%i==0 and y%i==0):
            hcf = i
    return hcf

x,y = map(int,input("Enter the two numbers : ").split())
print("H.C.F. of",x,"and",y,"is",HCF(x,y))



'''                             Output
                    Enter the two numbers : 4 15
                    H.C.F. of 4 and 15 is 1
'''