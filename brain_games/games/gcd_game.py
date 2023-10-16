from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(num1, num2):
    while num1 > 0 and num2 > 0:
        num1 = num1 % num2
        if num1 != 0:
            num2 = num2 % num1
    return max(num1, num2)


def find_gcd(numeric1, numeric2):
    if numeric1 == numeric2:
        return numeric1
    elif numeric1 == 1 or numeric2 == 1:
        return 1
    elif numeric1 > numeric2:
        return calculate_gcd(numeric1, numeric2)
    return calculate_gcd(numeric2, numeric1)


def generate_question_and_answer():
    smallest_number = 0
    biggest_number = 100
    random_first_num = randint(smallest_number, biggest_number)
    random_last_num = randint(smallest_number, biggest_number)
    correct_answer = find_gcd(random_first_num, random_last_num)
    question = f"Question: {random_first_num} {random_last_num}"
    return question, str(correct_answer)
