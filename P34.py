def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)


terms = int(input("Enter the number of terms : "))
if terms<=0:
    print("Please enter a positive number!!!")
else:
    print("Fibonacci series : ",end="")
    for i in range(terms):
        if i<(terms-1):
            print(fibo(i),end=",")
        else:
            print(fibo(i),end="")
