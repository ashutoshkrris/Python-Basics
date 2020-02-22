import datetime
def getTime():
    return datetime.datetime.now()

def lock(l):
    if l == 1:
        y = int(input("Press 1 for Exercise or 2 for Diet : "))
        if y == 1:
            value = input("Enter the exercise here : ")
            with open("rohan-ex.txt","a") as op:
                op.write(str([str(getTime())])+" : "+value+"\n")
                print("Successfully written!!")
        elif y == 2:
            value = input("Enter the diet here : ")
            with open("rohan-f.txt","a") as op:
                op.write(str([str(getTime())])+" : "+value+"\n")
                print("Successfully written!!")
        else:
            print("Wrong Input!!!")
            lock(1)

    elif l == 2:
        y = int(input("Press 1 for Exercise or 2 for Diet : "))
        if y == 1:
            value = input("Enter the exercise here : ")
            with open("rahul-ex.txt","a") as op:
                op.write(str([str(getTime())])+" : "+value+"\n")
                print("Successfully written!!")
        elif y == 2:
            value = input("Enter the diet here : ")
            with open("rahul-f.txt","a") as op:
                op.write(str([str(getTime())])+" : "+value+"\n")
                print("Successfully written!!")
        else:
            print("Wrong Input!!!")
            lock(2)

    elif l == 3:
        y = int(input("Press 1 for Exercise or 2 for Diet : "))
        if y == 1:
            value = input("Enter the exercise here : ")
            with open("ravi-ex.txt","a") as op:
                op.write(str([str(getTime())])+" : "+value+"\n")
                print("Successfully written!!")
        elif y == 2:
            value = input("Enter the diet here : ")
            with open("ravi-f.txt","a") as op:
                op.write(str([str(getTime())])+" : "+value+"\n")
                print("Successfully written!!")
        else:
            print("Wrong Input!!!")
            lock(3)

    else:
        print("Wrong Choice!!!")
        l = int(input("You have three clients as of now : \n1. Rohan\n2. Rahul\n3. Ravi\nChoose your client : "))
        lock(l)


def retrieve(r):
    if r == 1:
        z = int(input("Press 1 for Exercise or 2 for Diet : "))
        if z == 1:
            with open("rohan-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif z == 2:
            with open("rohan-f.txt") as op:
                for i in op:
                    print(i,end="")
        else:
            print("Wrong Input!!!")
            retrieve(1)
    
    elif r == 2:
        z = int(input("Press 1 for Exercise or 2 for Diet : "))
        if z == 1:
            with open("rahul-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif z == 2:
            with open("rahul-f.txt") as op:
                for i in op:
                    print(i,end="")
        else:
            print("Wrong Input!!!")
            retrieve(2)

    elif r == 3:
        z = int(input("Press 1 for Exercise or 2 for Diet : "))
        if z == 1:
            with open("ravi-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif z == 2:
            with open("ravi-f.txt") as op:
                for i in op:
                    print(i,end="")
        else:
            print("Wrong Input!!!")
            retrieve(3)

    else:
        print("Wrong Choice!!!")
        r = int(input("You have three clients as of now : \n1. Rohan\n2. Rahul\n3. Ravi\nChoose your client : "))
        retrieve(r)


print("\t\t\t\tHEALTH MANAGEMENT SYSTEM\n")
x = int(input("Enter 1 to lock a value or 2 to retrieve a value : "))
if x==1:
    l = int(input("You have three clients as of now : \n1. Rohan\n2. Rahul\n3. Ravi\nChoose your client : "))
    lock(l)
elif x==2:
    r = int(input("You have three clients as of now : \n1. Rohan\n2. Rahul\n3. Ravi\nChoose your client : "))
    retrieve(r)
else:
    print("Wrong Input!!!")