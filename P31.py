import random
def cchoice():
    l = ["Snake","Water","Gun"]
    ch = random.choice(l)
    return ch

def choice():
    s = input("\nEnter your choice out of Snake , Water or Gun : ")
    return s

def game(x,y,score):
    if(x == "Gun" and y == "Snake"):
        print("Yeahh!!",x,"wins over",y)
        score += 1
        print("So,your current score is",score)
    elif(x == "Gun" and y == "Water"):
        print("Sorry,",y,"wins over",x)
        print("So,your current score is",score)
    elif(x == "Water" and y == "Snake"):
        print("Sorry,",y,"wins over",x)
        print("So,your current score is",score)
    elif(x == "Water" and y == "Gun"):
        print("Yeahh!!",x,"wins over",y)
        score += 1
        print("So,your current score is",score)
    elif(x == "Snake" and y == "Water"):
        print("Yeahh!!",x,"wins over",y)
        score += 1
        print("So,your current score is",score)
    elif(x == "Snake" and y == "Gun"):
        print("Sorry,",y,"wins over",x)
        print("So,your current score is",score)
    elif(x == "Snake" and y == "Snake"):
        print("Oops , we both chose the same.\nNo score for both of us.")
    elif(x == "Water" and y == "Water"):
        print("Oops , we both chose the same.\nNo score for both of us.")
    elif(x == "Gun" and y == "Gun"):
        print("Oops , we both chose the same.\nNo score for both of us.")
    
    return score
    
print("\t\t\t\t\tSNAKE WATER GUN\n")
name = input("Hello dear, may I know your name ? : ")
print("Hello",name,", Welcome to Snake Water Gun\nIn this game,you have to choose one of the three - Snake , Water or Gun.\nRules of the game are : \n\n1. Snake drinks the Water , So Snake wins over Water.\n2. Gun sinks in the Water , So Water wins over Gun\n3. Gun kills the Snake , So Gun wins over Snake.")
print("Let's see if you can win over me or not!!!")
sc = 0
for i in range(10):
    userChoice = choice()
    computerChoice = cchoice()
    sc = game(userChoice,computerChoice,sc)
print("You scored",sc,"out of 10.")
if sc>5:
    print("So , You Won..Huhhh")
elif sc==5:
    print("Match is a tie..")
else:
    print("Lol!! You Lost..Try Harder")