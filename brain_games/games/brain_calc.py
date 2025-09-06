import random

RULES = 'What is the result of the expression?'


def generate_question():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    operators = ['+', '-', '*']
    random_operator = random.choice(operators)
    match random_operator:
        case '+': 
            correct_answer = num1 + num2
        case '-': 
            correct_answer = num1 - num2
        case '*': 
            correct_answer = num1 * num2
    question = f'Question: {num1} {random_operator} {num2}'
    return question, correct_answer
    

def check_answer(user_answer, correct_answer):
    return correct_answer == int(user_answer)