from random import randint
cont = input("Do you wish to play my higher or lower game? y/n ")
if cont == 'n':
    print("I didn't want you to play anyway.")
while cont == 'y':
     
    sec = randint(1,100)
    true = int(input("first guess of the number? "))
    if true > sec:
        print("LOWER!")
    else:
        print("HIGHER!")
    if true == sec:
        print("You Got it correct!")
    while true != sec:
        true = int(input("your next guess? "))
        if true > sec:
            print("LOWER!")
        else:
            print("HIGHER!")
        if true == sec:
            print("You Got it correct!")
            cont = input("play again? y/n ")
            if cont == 'n':
                print("Thanks for Playing")