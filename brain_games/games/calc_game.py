from random import randint
from random import choice


import prompt


from brain_games.cli import welcome_user


def calc_game():
    user_name = welcome_user()
    print('What is the result of the expression?')
    sum_correct_answers = 0
    while sum_correct_answers != 3:
        first_num = randint(0, 100)
        last_num = randint(0, 100)
        operand = choice(['+', '-', '*'])
        if operand == '+':
            summ = first_num + last_num
        elif operand == '-':
            summ = first_num - last_num
        elif operand == '*':
            summ = first_num * last_num
        print(f"Question: {first_num} {operand} {last_num}")
        answer = prompt.string('Your answer: ')
        if int(answer) == int(summ):
            print('Correct!')
            sum_correct_answers += 1
        else:
            return print(f"'{answer}' is wrong answer ;(."
                         f"Correct answer was '{summ}'.\n"
                         f"Let's try again, {user_name}!")
    return print('Congratulations, ' + user_name + '!')
