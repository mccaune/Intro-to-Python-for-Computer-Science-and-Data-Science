"""
4.11 (Guess-the-Number Modification) Modify the previous exercise to count the num-
ber of guesses the player makes. If the number is 10 or fewer, display "Either you know the
secret or you got lucky!" If the player makes more than 10 guesses, display "You should
be able to do better!" Why should it take no more than 10 guesses? Well, with each “good
guess,” the player should be able to eliminate half of the numbers, then half of the remaining
numbers, and so on. Doing this 10 times narrows down the possibilities to a single number.
This kind of “halving” appears in many computer science applications. For example, in the
“Computer Science Thinking: Recursion, Searching, Sorting and Big O” chapter, we’ll pres-
ent the high-speed binary search and merge sort algorithms, and you’ll attempt the quicksort
exercise—each of these cleverly uses halving to achieve high performance.
"""

#4.11
import random

def guess2():
    x = random.randrange(1,1000)
    count = 0
    print('Game - guess the number between 1 to 1000 with the fewest guesses')
    while True:
        try:
            a = int(input('Enter your guess: '))
            if a == x and count <= 10:
                print(f'You guessed the number! it was {x} \nIt took you {count} guesses. You got lucky!')
                break
            elif a == x and count > 10:
                print(f'You guessed the number! it was {x} \nIt took you {count} guesses. You can do better!')
                break
            elif a < x:
                print('Too low, try again!')
                count += 1
                continue
            elif a > x:
                print('Too high, try again!')
                count += 1
                continue
        except:
            print('Please enter valid number')
