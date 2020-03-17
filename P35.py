def rec_sum(n):
    if n<=1:
        return n
    else:
        return n+rec_sum(n-1)


num = int(input("Enter the number of terms : "))
if num<=0:
    print("Please enter a positive number!!!")
else:
    print("The sum of first",num, "natural numbers is ", rec_sum(num))
