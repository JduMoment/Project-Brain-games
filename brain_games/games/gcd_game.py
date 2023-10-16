from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def theory_of_evklid(num1, num2):
    while num1 > 0 and num2 > 0:
        num1 = num1 % num2
        if num1 != 0:
            num2 = num2 % num1
    return max(num1, num2)


def what_is_gcd(numeric1, numeric2):
    if numeric1 > numeric2:
        return theory_of_evklid(numeric1, numeric2)
    elif numeric2 > numeric1:
        return theory_of_evklid(numeric2, numeric1)


def generate_question_and_answer():
    RANDOM_FIRST_NUM = randint(1, 75)
    RANDOM_LAST_NUM = randint(1, 75)
    question = print(f"Question: {RANDOM_FIRST_NUM} {RANDOM_LAST_NUM}")
    if RANDOM_FIRST_NUM == RANDOM_LAST_NUM:
        correct_answer = RANDOM_FIRST_NUM
    elif RANDOM_FIRST_NUM == 1 or RANDOM_LAST_NUM == 1:
        correct_answer = 1
    else:
        correct_answer = what_is_gcd(RANDOM_FIRST_NUM, RANDOM_LAST_NUM)
    return question, str(correct_answer)
