from random import randint, choice


RULES = 'What number is missing in the progression?'

MIN_PROGRESSION_START_VALUE = 1
MAX_PROGRESSION_START_VALUE = 95

MIN_PROGRESSION_FINISH_VALUE = 105
MAX_PROGRESSION_FINISH_VALUE = 1000

MIN_PROGRESSION_STEP = 2
MAX_PROGRESSION_STEP = 7

MIN_PROGRESSION_LENGHT = 5
MAX_PROGRESSION_LENGHT = 15


def generate_question_and_answer():
    lower_progress_limit = randint(MIN_PROGRESSION_START_VALUE,
                                   MAX_PROGRESSION_START_VALUE)
    highest_progress_limit = randint(MIN_PROGRESSION_FINISH_VALUE,
                                     MAX_PROGRESSION_FINISH_VALUE)
    progress_step = randint(MIN_PROGRESSION_STEP,
                            MAX_PROGRESSION_STEP)
    random_arithm_progress = list(range(lower_progress_limit,
                                        highest_progress_limit,
                                        progress_step))
    limit_lenght_progression = randint(MIN_PROGRESSION_LENGHT,
                                       MAX_PROGRESSION_LENGHT)
    random_arithm_progress = random_arithm_progress[0:limit_lenght_progression]
    correct_answer = choice(random_arithm_progress)
    for index, element in enumerate(random_arithm_progress):
        if element == correct_answer:
            random_arithm_progress[index] = '..'
    random_arithm_progress = ' '.join(map(str, random_arithm_progress))
    question = f"{random_arithm_progress}"
    return question, correct_answer
