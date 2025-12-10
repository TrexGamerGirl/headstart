from random import randint

def addition_and_answer_checking(least, most):
    No1 = randint(least, most)
    No2 = randint(least, most)
    ans = (No1 + No2)
    print(No1, "+", No2)
    est = int(input("what is the sum of the above numbers? "))
    if ans != est:
        print("You are Incorrect The Correct Answer was: ", ans)
    if ans == est:
        print('You are correct good job')
    play = input("Do You Want To Play Again? (To Change Difficulties select no and start again) y/n ")
    if play == 'n':
        print("Thank You For Playing!")
        return False
    else:
        return True

play = input("Do you want to play a game of addition? y/n ")
if play == 'n':
    print(" well don't play then I don't even care")
   
while play == 'y' :
    dif = input("Please Pick a difficulty (Easy, Medium or Hard) ")
    while dif == 'Easy':
        result = addition_and_answer_checking(0,100)
        if not result:
            play = "n"
            break
    while dif == 'Medium':
        result = addition_and_answer_checking(0,500)
        if not result:
            play = "n"
            break
    while dif == 'Hard':
        result = addition_and_answer_checking(20, 2500)
        if not result:
            play = "n"
            break