import prompt
from brain_games.cli import welcome_user
from random import randint
from brain_games.is_prime import is_prime


def prime_number():
    user_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    sum_correct_answers = 0
    while sum_correct_answers != 3:
        num = randint(1, 1000)
        print(f"Question: {num}")
        answer = prompt.string('Your answer: ')
        prime = is_prime(num)
        if prime == True and answer == 'yes':
            print('Correct!')
            sum_correct_answers += 1
        elif prime == False and answer == 'no':
            print('Correct!')
            sum_correct_answers += 1
        else:
            return print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {user_name}!")
    return print('Congratulations, ' + user_name + '!')
