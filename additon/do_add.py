from random import randint

play = input("Do you want to play a game of addition? y/n ")
if play == 'n':
    print(" well don't play then I don't even care")

while play == 'y' :
    dif = input("Please Pick a difficulty (Easy, Medium or Hard) ")
    while dif == 'Easy':
        No1 = randint(0,100)
        No2 = randint(0,100)
        ans = (No1 + No2)
        print(No1, "+", No2)
        est = input("what is the sum of the above numbers? ")
        if ans != est:
            print("You are Incorrect The Correct Answer was: ", ans)
        if ans == est:
            print('You are correct good job')
        play = input("Do You Want To Play Again? (To Change Difficulties select no and start again) y/n ")
        if play == 'n':
            print("Thank You For Playing!")
            break
    while dif == 'Medium':
        No1 = randint(0,500)
        No2 = randint(0,500)
        ans = (No1 + No2)
        print(No1, "+", No2)
        est = input("what is the sum of the above numbers? ")
        if ans != est:
            print("You are Incorrect The Correct Answer was: ", ans)
        if ans == est:
            print('You are correct good job')
        play = input("Do You Want To Play Again? (To Change Difficulties select no and start again) y/n ")
        if play == 'n':
            print("Thank You For Playing!")
            break
    while dif == 'Hard':
        No1 = randint(20,2500)
        No2 = randint(20,2500)
        ans = (No1 + No2)
        print(No1, "+", No2)
        est = input("what is the sum of the above numbers? ")
        if ans != est:
            print("You are Incorrect The Correct Answer was: ", ans)
        if ans == est:
            print('You are correct good job')
        play = input("Do You Want To Play Again (To Change Difficulties select no and start again)? y/n ")
        if play == 'n':
            print("Thank You For Playing!")