from random import randint
from random import choice


RULES = 'What number is missing in the progression?'


def generate_question_and_answer():
    arithm_progress = list(range(randint(1, 100), randint(1, 1000),
                                 randint(2, 7)))
    arithm_progress = arithm_progress[0:randint(5, 15)]
    correct_answer = choice(arithm_progress)
    for index, element in enumerate(arithm_progress):
        if element == correct_answer:
            arithm_progress[index] = '..'
    arithm_progress = ' '.join(map(str, arithm_progress))
    question = print(f"Question: {arithm_progress}")
    return question, str(correct_answer)
