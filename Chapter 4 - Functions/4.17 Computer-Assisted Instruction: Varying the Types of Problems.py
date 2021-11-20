"""
4.17 (Computer-Assisted Instruction: Varying the Types of Problems) Modify the previ-
ous exercise to allow the user to pick a type of arithmetic problem to study—1 means ad-
dition problems only, 2 means subtraction problems only, 3 means multiplication
problems only, 4 means division problems only (avoid dividing by 0) and 5 means a ran-
dom mixture of all these types.
"""

#4.17
import random

def level1():
    num1 = random.randrange(1,10)
    num2 = random.randrange(1,10)
    return(num1, num2)

def level2():
    num1 = random.randrange(1,100)
    num2 = random.randrange(1,100)
    return(num1, num2)

def multiplication(numbers):
    num1, num2 = numbers
    result = num1 * num2
    print(f'How much is {num1} times {num2}? (enter: "99" to exit)')
    return result

def addition(numbers):
    num1, num2 = numbers
    result = num1 + num2
    print(f'How much is {num1} plus {num2}? (enter: "99" to exit)')
    return result

def subtraction(numbers):
    num1, num2 = numbers
    result = num1 - num2
    print(f'How much is {num1} minus {num2}? (enter: "99" to exit)')
    return result

def division(numbers):
    num1, num2 = numbers
    result = num1 / num2
    print(f'How much is {num1} divided by {num2}? (enter: "99" to exit)')
    return result

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

def problem_type():
    problem_type = int(input('Enter problem type (1 - addition; 2 - subtraction, 3 - multiplication; 4 - division):  '))
    return problem_type

def values(level):
    if level == 1:
        values = level1()
    elif level == 2:
        values = level2()
    return values

level = difficulty()
problem_type = problem_type()

answer = 0

if problem_type == 1:
    result = addition(values(level))
    answer = int(input('Answer: '))
    while answer != 99:
        if int(answer) == result:
            correct_answer()
            result = addition(values(level))
            answer = int(input('Answer: '))
        else:
            wrong_answer()
            answer = int(input('Answer: '))
elif problem_type == 2:
    result = subtraction(values(level))
    answer = int(input('Answer: '))
    while answer != 99:
        if int(answer) == result:
            correct_answer()
            result = subtraction(values(level))
            answer = int(input('Answer: '))
        else:
            wrong_answer()
            answer = int(input('Answer: '))
elif problem_type == 3:
    result = multiplication(values(level))
    answer = int(input('Answer: '))
    while answer != 99:
        if int(answer) == result:
            correct_answer()
            result = multiplication(values(level))
            answer = int(input('Answer: '))
        else:
            wrong_answer()
            answer = int(input('Answer: '))
elif problem_type == 4:
    result = division(values(level))
    answer = float(input('Answer: '))
    while answer != 99:
        if float(answer) == result:
            correct_answer()
            result = division(values(level))
            answer = float(input('Answer: '))
        else:
            wrong_answer()
            answer = float(input('Answer: '))


