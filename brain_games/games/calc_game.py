from random import randint, choice

RULES = "What is the result of the expression?"


def generate_question_and_answer():
    smallest_number = 0
    biggest_number = 100
    first_num = randint(smallest_number, biggest_number)
    last_num = randint(smallest_number, biggest_number)
    random_operand = choice(['+', '-', '*'])
    if random_operand == '+':
        correct_answer = first_num + last_num
    elif random_operand == '-':
        correct_answer = first_num - last_num
    elif random_operand == '*':
        correct_answer = first_num * last_num
    question = f"Question: {first_num} {random_operand} {last_num}"
    return question, str(correct_answer)
