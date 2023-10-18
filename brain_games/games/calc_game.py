from random import randint, choice

RULES = "What is the result of the expression?"

SMALLEST_NUMBER = 0
BIGGEST_NUMBER = 100


def evaluate_expression(num1, operand, num2):
    if operand == '+':
        return num1 + num2
    elif operand == '-':
        return num1 - num2
    elif operand == '*':
        return num1 * num2


def generate_question_and_answer():
    first_num = randint(SMALLEST_NUMBER, BIGGEST_NUMBER)
    last_num = randint(SMALLEST_NUMBER, BIGGEST_NUMBER)
    random_operand = choice(['+', '-', '*'])
    correct_answer = evaluate_expression(first_num, random_operand, last_num)
    question = f"{first_num} {random_operand} {last_num}"
    return question, correct_answer
