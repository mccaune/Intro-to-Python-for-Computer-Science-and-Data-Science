"""
4.14 (Computer-Assisted Instruction) Computer-assisted instruction (CAI) refers to the
use of computers in education. Write a script to help an elementary school student learn
multiplication. Create a function that randomly generates and returns a tuple of two positive one-digit integers. Use that function’s result in your script to prompt the user with a
question, such as

"How much is 6 times 7?"

For a correct answer, display the message "Very good!" and ask another multiplication
question. For an incorrect answer, display the message "No. Please try again." and let
the student try the same question repeatedly until the student finally gets it right.
"""

#4.14
import random

def multiply():
    num1 = random.randrange(1,10)
    num2 = random.randrange(1,10)
    return(num1, num2)

def display(numbers):
    num1, num2 = numbers
    product = num1 * num2
    print(f'How much is {num1} times {num2}? (enter: "99" to exit)')
    return product

answer = 0
values = multiply()
product = display(values)
answer = int(input('Answer: '))

while answer != 99:
    if int(answer) == product:
        print('Correct, very good!')
        values = multiply()
        product = display(values)
        answer = int(input('Answer: '))
    else:
        print('No. Please try again.')
        answer = int(input('Answer: '))

