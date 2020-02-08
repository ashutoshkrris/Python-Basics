st = input("In which unit you want to enter your temperature - Celsius or Fahrenheit ? : ")
st = list(st)
if(st[0]=='c' or st[0]=='C'):
    c = float(input("Enter the temperature : "))
    f = (c*1.8)+32
    print("The temperature in Fahrenheit is "+str(f))
elif(st[0]=='F' or st[0]=='f'):
    f = float(input("Enter the temperature : "))
    c = (f-32)/1.8
    print("The temperature in Celsius is :"+str(c))
else:
    print("Invalid Input!!!!")


'''                                     Output
                        In which unit you want to enter your temperature - Celsius or Fahrenheit ? : Celsius
                        Enter the temperature : 37.5
                        The temperature in Fahrenheit is 99.5
'''