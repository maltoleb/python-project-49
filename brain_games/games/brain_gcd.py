import random

RULES = 'Find the greatest common divisor of given numbers.'


def generate_question():
    a = random.randint(1, 30)  # NOSONAR
    b = random.randint(1, 30)  # NOSONAR
    if a >= b:
        x, y = a, b
    else:
        x, y = b, a
    while y != 0:
        x, y = y, x % y
    correct_answer = x
    return f'Question: {a} {b}', correct_answer


def check_answer(user_answer, correct_answer):
    return int(user_answer) == correct_answer