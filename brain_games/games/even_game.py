from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

SMALLEST_NUMBER = 0
BIGGEST_NUMBER = 100


def generate_question_and_answer():
    random_number = randint(SMALLEST_NUMBER, BIGGEST_NUMBER)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    elif random_number % 2 != 0:
        correct_answer = 'no'
    question = f"{random_number}"
    return question, correct_answer
