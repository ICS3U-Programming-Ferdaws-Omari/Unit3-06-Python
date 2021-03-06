#!/usr/bin/env python3
# Created By: Ferdaws
# Date: April 3, 2022
# This program guesses a number between 1 and 10.
import random


def main():
    hidden = random.randint(1, 9)
    # a number between 1 and 9
    # print hidden

    # Compare the randome number to the guess and display the output
    try:
        guess = int(input("Guess a number between 1 and 9 :"))
        integer_as_number = int(guess)
    # check the numbers is equal to hidden
        if guess == hidden:

            print("you guessed right")

    # check the numbers is not equal to hidden
        else:
            print("you guessed wrong")
            print("The correct answer is")
            print(hidden)
    except Exception:
        print("This was not an integer, please enter an integer")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
