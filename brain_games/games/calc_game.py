from random import randint, choice

RULES = "What is the result of the expression?"


def generate_question_and_answer():
    first_num = randint(0, 100)
    last_num = randint(0, 100)
    random_operand = choice(['+', '-', '*'])
    if random_operand == '+':
        correct_answer = first_num + last_num
    elif random_operand == '-':
        correct_answer = first_num - last_num
    elif random_operand == '*':
        correct_answer = first_num * last_num
    question = f"Question: {first_num} {random_operand} {last_num}"
    return question, str(correct_answer)
