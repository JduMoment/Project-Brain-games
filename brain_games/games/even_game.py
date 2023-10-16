from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer():
    random_number = randint(1, 100)
    question = print(f"Question: {random_number}")
    if random_number % 2 == 0:
        correct_answer = 'yes'
    elif random_number % 2 != 0:
        correct_answer = 'no'
    return question, correct_answer
