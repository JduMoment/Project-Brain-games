from random import randint
from random import choice


RULES = 'What number is missing in the progression?'


def generate_question_and_answer():
    RANDOM_ARITHM_PROGRESS = list(range(randint(1, 95), randint(100, 1000),
                                  randint(2, 7)))
    RANDOM_ARITHM_PROGRESS = RANDOM_ARITHM_PROGRESS[0:randint(5, 15)]
    correct_answer = choice(RANDOM_ARITHM_PROGRESS)
    for index, element in enumerate(RANDOM_ARITHM_PROGRESS):
        if element == correct_answer:
            RANDOM_ARITHM_PROGRESS[index] = '..'
    RANDOM_ARITHM_PROGRESS = ' '.join(map(str, RANDOM_ARITHM_PROGRESS))
    question = print(f"Question: {RANDOM_ARITHM_PROGRESS}")
    return question, str(correct_answer)
