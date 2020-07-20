print("--------------------------------------")
print("WELCOME TO THE GUESS THAT NUMBER GAME")
print("--------------------------------------")
import random

the_num = random.randint(0, 100)
user_guess = -1
more = 0

while user_guess != the_num:

    user_guess = int(input("guess a number between 0 to 100"))

    more = more+1
    while more >5:
        print(f"enter {the_num} and you will win")
        break


    if user_guess < the_num:

            print(f"your guess {user_guess} is to low \n")
    elif user_guess > the_num:
            print(f"your guess {user_guess} guess is to high")


    else:
            print("HEY you win")

        # print(f" enter {the_num} and you win")
