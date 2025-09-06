import random

RULES = 'What is the result of the expression?'


def generate_question():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    operators = ['+', '-', '*']
    random_operator = random.choice(operators)
    match random_operator:
        case '+': 
            result = num1 + num2
        case '-': 
            result = num1 - num2
        case '*': 
            result = num1 * num2
    return f'Question: {num1} {random_operator} {num2}', result
    

def check_answer(user_answer, correct_answer):
    return correct_answer == int(user_answer)