"""
4.15 (Computer-Assisted Instruction: Reducing Student Fatigue) Varying the comput-
er’s responses can help hold the student’s attention. Modify the previous exercise so that
various comments are displayed for each answer. Possible responses to a correct answer
should include 'Very good!', 'Nice work!' and 'Keep up the good work!' Possible re-
sponses to an incorrect answer should include 'No. Please try again.', 'Wrong. Try
once more.' and 'No. Keep trying.' Choose a number from 1 to 3, then use that value
to select one of the three appropriate responses to each correct or incorrect answer.
"""

#4.15
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


answer = 0
values = multiply()
product = display(values)
answer = int(input('Answer: '))

while answer != 99:
    if int(answer) == product:
        correct_answer()
        values = multiply()
        product = display(values)
        answer = int(input('Answer: '))
    else:
        wrong_answer()
        answer = int(input('Answer: '))

