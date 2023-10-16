from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer():
    RANDOM_NUMBER = randint(1, 100)
    question = print(f"Question: {RANDOM_NUMBER}")
    if RANDOM_NUMBER % 2 == 0:
        correct_answer = 'yes'
    elif RANDOM_NUMBER % 2 != 0:
        correct_answer = 'no'
    return question, correct_answer
