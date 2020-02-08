num1 , num2, num3 = map(int,input("Enter the numbers : ").split())
max = num1
if(num2>max):
    max=num2
if(num3>max):
    max=num3
print("The largest number among "+str(num1)+" , "+str(num2)+" and "+str(num3)+" is "+str(max))



'''                         Output
                    Enter the numbers : 1 2 3
                The largest number among 1 , 2 and 3 is 3
'''