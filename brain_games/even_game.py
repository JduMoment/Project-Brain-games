from random import randint
from brain_games.cli import welcome_user
import prompt

name = welcome_user()

def even_odd_game():
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
                         "Let's try again, " + name + '!') 
    return print('Congratulations, ' + name + '!')
