#python 3.7.1 by Ashutosh Krishna

def perfect(n):
  sum=0
  for i in range(1,n):
    if n%i==0:
      sum += i
  if n==sum:
    return True

n = int(input("Enter the number : "))
if perfect(n):
  print(f"{n} is a perfect number.")
else:
  print(f"{n} is not a perfect number.")
  
  

"""
OUTPUT

Enter the number : 6
6 is a perfect number.


"""
