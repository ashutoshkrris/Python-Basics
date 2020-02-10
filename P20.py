num = int(input("Enter the number of natural numbers you want to add : "))
sum = 0
if num<0:
    print("Invalid Input!!!!")
else:
    for i in range(1,num+1):
        sum = sum+i
print("Sum of first",num,"numbers is",sum)



'''                                 Output
                Enter the number of natural numbers you want to add : 5
                Sum of first 5 numbers is 15
'''