s = input("Do you know the base and height of the triangle?\nYes or No? ")
s=list(s)
if(s[0]=='y' or s[0]=='Y'):
    base = int(input("Enter the base of the triangle : "))
    height = int(input("Enter the height of the triangle : "))
    area = 0.5*base*height
    print("Area : "+str(area))
elif(s[0]=='n' or s[0]=='N'):
    a = int(input("Enter the first side of the triangle : "))
    b = int(input("Enter the second side of the triangle : "))
    c = int(input("Enter the third side of the triangle : "))
    st = (a+b+c)*0.5
    area = (st*(st-a)*(st-b)*(st-c))**0.5
    print("Area : "+str(area))



'''                                     Output
                        Do you know the base and height of the triangle?
                        Yes or No? Yes
                        Enter the base of the triangle : 7
                        Enter the height of the triangle : 14
                        Area : 49.0
                                        OR
                        Do you know the base and height of the triangle?
                        Yes or No? No
                        Enter the first side of the triangle : 3
                        Enter the second side of the triangle : 4
                        Enter the third side of the triangle : 5
                        Area : 6.0
'''
