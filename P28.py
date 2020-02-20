def gtn(x,y,z):
    if y>x:
        print("Sorry,your number is greater than our secret number.")
        z -= 1
        if z==1:
            print("Try Again!!\nYou have only",z,"guess left.")
        elif z==0:
            print("You have no more guesses left.\nBetter luck..Next time\nOur secret number was",x)
            sys.exit()
        else:
            print("Try Again!!\nYou have only",z,"guesses left.")
        return
    elif y==x:
        z -= 1
        if z==1:
            print("Yaay!! Our secret number is just as you thought.\nYou guessed it right with",z,"guess left.")
        else:
            print("Yaay!! Our secret number is just as you thought.\nYou guessed it right with",z,"guesses left.")
            sys.exit()
    else:
        print("Sorry,your number is less than our secret number.")
        z -= 1
        if z==1:
            print("Try Again!!\nYou have only",z,"guess left.")
        elif z==0:
            print("You have no more guesses left.\nBetter luck..Next time\nOur secret number was",x)
            sys.exit()
        else:
            print("Try Again!!\nYou have only",z,"guesses left.")
        return


import sys
import random
n = random.randint(1,20)

guess = 6
name = input("What is your name? : ")
print("Hello",name,", Welcome to Guess The Number game.\nWe have got a secret number for you and you have to guess it for us.")
while(True):
    guess -= 1
    num = int(input("Guess the number : "))
    gtn(n,num,guess)





'''                                                 OUTPUT
                                        What is your name? : Ashutosh
                                        Hello Ashutosh , Welcome to Guess The Number game.
                                        We have got a secret number for you and you have to guess it for us.
                                        Guess the number : 13
                                        Sorry,your number is greater than our secret number.
                                        Try Again!!
                                        You have only 4 guesses left.
                                        Guess the number : 10
                                        Sorry,your number is greater than our secret number.
                                        Try Again!!
                                        You have only 3 guesses left.
                                        Guess the number : 7
                                        Sorry,your number is less than our secret number.
                                        Try Again!!
                                        You have only 2 guesses left.
                                        Guess the number : 8
                                        Sorry,your number is less than our secret number.
                                        Try Again!!
                                        You have only 1 guess left.
                                        Guess the number : 9
                                        Yaay!! Our secret number is just as you thought.
                                        You guessed it right with 0 guesses left.
'''