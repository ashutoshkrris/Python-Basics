num = int(input("Enter the number : "))
s = str(num)
n = len(s)
temp = num
sum = 0
while temp>0:
    digit = temp%10
    temp = temp//10
    sum = sum+(digit**n)
if(num==sum):
    print(num,"is an Armstrong number.")



'''                                     Output
                                Enter the number : 371
                                371 is an Armstrong number.
'''