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
    smallest_number = 0
    biggest_number = 1000
    random_num = randint(smallest_number, biggest_number)
    correct_answer = "yes" if is_prime(random_num) else "no"
    question = f"Question: {random_num}"
    return question, correct_answer
