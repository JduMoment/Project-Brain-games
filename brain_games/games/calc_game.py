from random import randint
from random import choice

RULES = "What is the result of the expression?"


def generate_question_and_answer():
    first_num = randint(0, 100)
    last_num = randint(0, 100)
    operand = choice(['+', '-', '*'])
    question = print(f"Question: {first_num} {operand} {last_num}")
    if operand == '+':
        correct_answer = first_num + last_num
    elif operand == '-':
        correct_answer = first_num - last_num
    elif operand == '*':
        correct_answer = first_num * last_num
    return question, str(correct_answer)
