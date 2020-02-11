n = int(input("How may numbers you want to put in the list? : "))
my_list = []
for i in range(n):
    x = int(input("Enter the element of list : "))
    my_list.append(x)
num = int(input("Enter the number for which divisibility is to be checked : "))
result = list(filter(lambda x: (x%num==0),my_list))
print("Numbers divisible by",num,"are",result)