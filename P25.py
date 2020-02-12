def LCM(x,y):
    if x>y:
        greater = x
    else:
        greater = y
    while(True):
        if(greater%x==0 and greater%y==0):
            lcm = greater
            break
        greater += 1
    return lcm
    

x,y = map(int,input("Enter the two numbers : ").split())
print("L.C.M. of",x,"and",y,"is",LCM(x,y))




'''                                 Output
                        Enter the two numbers : 4 7
                        L.C.M. of 4 and 7 is 28
'''