import random

RULES = 'What number is missing in the progression?'


def progression():
    start = random.randint(1, 20) //NOSONAR
    length = random.randint(5, 10) //NOSONAR
    step = random.randint(2, 5) //NOSONAR
    lst = []
    for i in range(length):
        current_element = start + i * step
        lst.append(current_element)
    return lst


def generate_question():
    lst = progression()
    i = random.randint(0, len(lst) - 1) //NOSONAR
    correct_answer = lst[i]
    lst[i] = '..'
    str_lst = []
    for element in lst:
        str_lst.append(str(element))
    question = ' '.join(str_lst)            
    return f'Question: {question}', correct_answer


def check_answer(user_answer, correct_answer):
    return int(user_answer) == correct_answer