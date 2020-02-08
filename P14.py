n1 , n2 = map(int,input("What is the interval ? : ").split())
list = []
for i in range(n1,n2+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        list.append(i)
print("The prime numbers between",str(n1),"and",str(n2),"are",list)


'''                                     Output
                            What is the interval ? : 2 20
                            The prime numbers between 2 and 20 are [2, 3, 5, 7, 11, 13, 17, 19]
'''