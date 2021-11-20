"""
4.16 (Computer-Assisted Instruction: Difficulty Levels) Modify the previous exercise to
allow the user to enter a difficulty level. At a difficulty level of 1, the program should use
only single-digit numbers in the problems and at a difficulty level of 2, numbers as large
as two digits.
"""

#4.16
import random

def level1():
    num1 = random.randrange(1,10)
    num2 = random.randrange(1,10)
    return(num1, num2)

def level2():
    num1 = random.randrange(1,100)
    num2 = random.randrange(1,100)
    return(num1, num2)

def multiply(numbers):
    num1, num2 = numbers
    product = num1 * num2
    print(f'How much is {num1} times {num2}? (enter: "99" to exit)')
    return product

def correct_answer():
    x = random.randrange(1,4)
    if x == 1:
        print('Correct, very good!')
    elif x == 2:
        print('Nice work!')
    elif x == 3:
        print('Keep up the good work!')

def wrong_answer():
    x = random.randrange(1,4)
    if x == 1:
        print('No. Please try again.')
    elif x == 2:
        print('Wrong. Try once more.')
    elif x == 3:
        print('No. Keep trying')


def difficulty():
    level = int(input('Enter difficulty level (1 or 2): '))
    return level

level = difficulty()

answer = 0

if level == 1:
    values = level1()
    product = multiply(values)
    answer = int(input('Answer: '))
    while answer != 99:
        if int(answer) == product:
            correct_answer()
            values = level1()
            product = multiply(values)
            answer = int(input('Answer: '))
        else:
            wrong_answer()
            answer = int(input('Answer: '))
elif level == 2:
    values = level2()
    product = multiply(values)
    answer = int(input('Answer: '))
    while answer != 99:
        if int(answer) == product:
            correct_answer()
            values = level2()
            product = multiply(values)
            answer = int(input('Answer: '))
        else:
            wrong_answer()
            answer = int(input('Answer: '))


