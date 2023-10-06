from random import randint
from random import choice
import prompt
from brain_games.cli import welcome_user
from brain_games.nod import nod


def calc_game():
    user_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    sum_correct_answers = 0
    while sum_correct_answers != 3:
        first_num = randint(1, 75)
        last_num = randint(1, 75)
        multipliers_first_num = list(set(nod(first_num)))
        multipliers_last_num = list(set(nod(last_num)))
        print(f"Question: {first_num} {last_num}")
        answer = prompt.string('Your answer: ')
        i = 0
        result = 1
        while i != len(multipliers_first_num) - 1 or i != len(multipliers_last_num) - 1:
            if multipliers_first_num[i] == multipliers_first_num[i]:
                result *= multipliers_first_num[i]
                i += 1
            else:
                i += 1
        if int(answer) == int(result):
            print('Correct!')
            sum_correct_answers += 1
        else:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {user_name}!")
    return print('Congratulations, ' + user_name + '!')


calc_game()