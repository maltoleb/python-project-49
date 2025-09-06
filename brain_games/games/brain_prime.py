

import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for element in range(3, num - 1):
        if num % element == 0:
            return False
    return True


def generate_question():
    num = random.randint(1, 20)
    question = f'Question: {num}'
    if is_prime(num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer