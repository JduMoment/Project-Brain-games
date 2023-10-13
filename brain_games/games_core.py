from brain_games.cli import welcome_user
from brain_games.games.even_game import even_odd_game


import prompt


from random import randint


def core_game(game):
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    sum_correct_answers = 0
    while sum_correct_answers != 3:
        random_number = randint(1, 50)
        print('Question: ' + str(random_number))
        answer = prompt.string('Your answer: ')
        is_right = game(answer, random_number)
        if is_right is True:
            print('Correct!')
            sum_correct_answers += 1
        else:
            return print(f"'{answer}' is wrong answer ;(."
                         f"Correct answer was '{is_right}'.\n"
                         f"Let's try again, {user_name}!")
    return print('Congratulations, ' + user_name + '!')