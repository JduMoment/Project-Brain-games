from random import randint, choice


RULES = 'What number is missing in the progression?'


def generate_question_and_answer():
    random_arithm_progress = list(range(randint(1, 95), randint(100, 1000),
                                  randint(2, 7)))
    random_arithm_progress = random_arithm_progress[0:randint(5, 15)]
    correct_answer = choice(random_arithm_progress)
    for index, element in enumerate(random_arithm_progress):
        if element == correct_answer:
            random_arithm_progress[index] = '..'
    random_arithm_progress = ' '.join(map(str, random_arithm_progress))
    question = f"Question: {random_arithm_progress}"
    return question, str(correct_answer)
