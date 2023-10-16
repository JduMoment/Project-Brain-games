from random import randint
from random import choice

RULES = "What is the result of the expression?"


def generate_question_and_answer():
    FIRST_NUM = randint(0, 100)
    LAST_NUM = randint(0, 100)
    random_operand = choice(['+', '-', '*'])
    question = print(f"Question: {FIRST_NUM} {random_operand} {LAST_NUM}")
    if random_operand == '+':
        correct_answer = FIRST_NUM + LAST_NUM
    elif random_operand == '-':
        correct_answer = FIRST_NUM - LAST_NUM
    elif random_operand == '*':
        correct_answer = FIRST_NUM * LAST_NUM
    return question, str(correct_answer)
