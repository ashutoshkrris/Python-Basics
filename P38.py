#python 3.7.1 by Ashutosh Krishna

#Finding factorial of each digit
def fact(n):
  f = 1
  for i in range(1,n+1):
    f *= i
  return f

  
num = int(input("Enter the number : "))
number = num     #storing num into another variable number
sum = 0          #initialising sum with 0
while(num):
  r = num%10     #finding the last digit
  y = fact(r)    #finding factorial of last digit
  sum += y       #adding the factorial of each last digit
  num //= 10

if sum == number:
  print(f"{number} is a Strong Number.")
else:
  print(f"{number} is not a Strong Number.")
  
  
  
'''
OUTPUT

Enter the number : 145
145 is a Strong Number.

'''
