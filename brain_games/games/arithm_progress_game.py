from random import randint, choice


RULES = 'What number is missing in the progression?'


def generate_question_and_answer():
    lower_progress_limit = randint(1, 95)
    highest_progress_limit = randint(100, 1000)
    progress_step = randint(2, 7)
    random_arithm_progress = list(range(lower_progress_limit, highest_progress_limit,
                                  progress_step))
    limit_lenght_progression = randint(5, 15)
    random_arithm_progress = random_arithm_progress[0:limit_lenght_progression]
    correct_answer = choice(random_arithm_progress)
    for index, element in enumerate(random_arithm_progress):
        if element == correct_answer:
            random_arithm_progress[index] = '..'
    random_arithm_progress = ' '.join(map(str, random_arithm_progress))
    question = f"Question: {random_arithm_progress}"
    return question, str(correct_answer)
