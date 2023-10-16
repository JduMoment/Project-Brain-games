from random import randint
from random import choice

RULES = "What is the result of the expression?"


def generate_question_and_answer():
    RANDOM_FIRST_NUM = randint(0, 100)
    RANDOM_LAST_NUM = randint(0, 100)
    RANDOM_OPERAND = choice(['+', '-', '*'])
    question = print(f"Question: {RANDOM_FIRST_NUM} {RANDOM_OPERAND} {RANDOM_LAST_NUM}")
    if RANDOM_OPERAND == '+':
        correct_answer = RANDOM_FIRST_NUM + RANDOM_LAST_NUM
    elif RANDOM_OPERAND == '-':
        correct_answer = RANDOM_FIRST_NUM - RANDOM_LAST_NUM
    elif RANDOM_OPERAND == '*':
        correct_answer = RANDOM_FIRST_NUM * RANDOM_LAST_NUM
    return question, str(correct_answer)
