
import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer


def generate_question():
    num = random.randint(0, 100)  # NOSONAR
    question = f'Question: {num}'
    if is_even(num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer