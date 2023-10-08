from random import randint
from random import choice
import prompt
from brain_games.cli import welcome_user


def arithm_progress():
    user_name = welcome_user()
    print('What number is missing in the progression?')
    sum_correct_answers = 0
    while sum_correct_answers != 3:
        arithm_progress = list(range(randint(1, 100), randint(1, 1000), randint(2, 7)))
        arithm_progress = arithm_progress[0:randint(5, 15)]
        random_number = choice(arithm_progress)
        for index, element in enumerate(arithm_progress):
            if element == random_number:
                arithm_progress[index] = '..'
        print('Question: ' + " ".join(map(str, arithm_progress)))
        answer = prompt.string('Your answer: ')
        if int(answer) == int(random_number):
            print('Correct!')
            sum_correct_answers += 1
        else:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was '{random_number}'.\nLet's try again, {user_name}!")
    return print('Congratulations, ' + user_name + '!')
