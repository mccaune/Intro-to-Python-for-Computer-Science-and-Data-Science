"""
4.10 (Guess the Number) Write a script that plays “guess the number.” Choose the
number to be guessed by selecting a random integer in the range 1 to 1000. Do not reveal
this number to the user. Display the prompt "Guess my number between 1 and 1000 with
the fewest guesses:". The player inputs a first guess. If the guess is incorrect, display
"Too high. Try again." or "Too low. Try again." as appropriate to help the player “zero
in” on the correct answer, then prompt the user for the next guess. When the user enters
the correct answer, display "Congratulations. You guessed the number!", and allow the
user to choose whether to play again.
"""

#4.10 
import random

def guess():
    x = random.randrange(1,1000)
    print('Game - guess the number between 1 to 1000 with the fewest guesses')
    while True:
        try:
            a = int(input('Enter your guess: '))
            if a == x:
                print(f'You guessed the number! it was {x} ')
                break
            elif a < x:
                print('Too low, try again!')
                continue
            elif a > x:
                print('Too high, try again!')
                continue
        except:
            print('Please enter valid number')
