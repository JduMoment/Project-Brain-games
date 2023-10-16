from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer():
    smallest_number = 0
    biggest_number = 100
    random_number = randint(smallest_number, biggest_number)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    elif random_number % 2 != 0:
        correct_answer = 'no'
    question = f"Question: {random_number}"
    return question, correct_answer
