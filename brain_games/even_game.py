from random import randint
import prompt
from .cli import welcome_user


def even_odd_game():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    sum_correct_answers = 0
    while sum_correct_answers != 3:
        random_number = randint(1, 50)
        print('Question: ' + str(random_number))
        answer = prompt.string('Your answer: ')
        if answer == 'yes' and random_number % 2 == 0:
            print('Correct!')
            sum_correct_answers += 1
        elif answer == 'no' and random_number % 2 != 0:
            print('Correct!')
            sum_correct_answers += 1
        else:
            return print("'yes' is wrong answer ;(. Correct answer was 'no'.\n"
                         "Let's try again, " + user_name + "!")
    return print('Congratulations, ' + user_name + '!')
