n = int(input("How may numbers you want to put in the list? : "))
my_list = []
for i in range(n):
    x = int(input("Enter the element of list : "))
    my_list.append(x)
num = int(input("Enter the number for which divisibility is to be checked : "))
result = list(filter(lambda x: (x%num==0),my_list))
print("Numbers divisible by",num,"are",result)



'''                                     Output
                    How may numbers you want to put in the list? : 5
                    Enter the element of list : 11
                    Enter the element of list : 12
                    Enter the element of list : 13
                    Enter the element of list : 14
                    Enter the element of list : 15
                    Enter the number for which divisibility is to be checked : 2
                    Numbers divisible by 2 are [12, 14]
'''
