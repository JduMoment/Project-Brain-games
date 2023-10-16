from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    i = 2
    while num > i:
        is_prime = num % i
        i += 1
        if is_prime == 0:
            return False
    return True


def generate_question_and_answer():
    RANDOM_NUM = randint(1, 1000)
    question = print(f"Question: {RANDOM_NUM}")
    prime = is_prime(RANDOM_NUM)
    if prime is True:
        correct_answer = 'yes'
    elif prime is False:
        correct_answer = 'no'
    return question, correct_answer
