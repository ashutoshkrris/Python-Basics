n1 , n2 = map(int,input("What is the interval ? : ").split())
list = []
for i in range(n1,n2+1):
    s = str(i)
    n = len(s)
    temp = i
    sum = 0
    while temp>0:
        digit = temp%10
        temp = temp//10
        sum = sum+(digit**n)
    if(sum==i):
        list.append(i)
print("Armstrong numbers between",n1,"and",n2,"are :",list)



'''                                  Output
                        What is the interval ? : 100 2000
                        Armstrong numbers between 100 and 2000 are : [153, 370, 371, 407, 1634]
'''
