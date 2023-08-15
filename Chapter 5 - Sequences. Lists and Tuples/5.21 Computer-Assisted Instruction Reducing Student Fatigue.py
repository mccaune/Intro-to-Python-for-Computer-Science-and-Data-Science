"""
5.21
Computer-Assisted Instruction: Reducing Student Fatigue) Re-implement
Exercise 4.15 to store the computer’s responses in lists. Use random-number generation
to select responses using random list indices.
"""

import random

def multiply():
    num1 = random.randrange(1, 10)
    num2 = random.randrange(1, 10)
    return num1, num2

def display(numbers):
    num1, num2 = numbers
    product = num1 * num2
    print(f'How much is {num1} times {num2}? (enter: "99" to exit)')
    return product

def correct_answer():
    responses = ['Correct, very good!', 'Nice work!', 'Keep up the good work!']
    print(random.choice(responses))

def wrong_answer():
    responses = ['No. Please try again.', 'Wrong. Try once more.', 'No. Keep trying.']
    print(random.choice(responses))

answer = 0
values = multiply()
product = display(values)
answer = int(input('Answer: '))

while answer != 99:
    if answer == product:
        correct_answer()
        values = multiply()
        product = display(values)
        answer = int(input('Answer: '))
    else:
        wrong_answer()
        answer = int(input('Answer: '))


