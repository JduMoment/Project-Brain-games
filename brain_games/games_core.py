from brain_games.cli import welcome_user


import prompt


def play(game):
    user_name = welcome_user()
    print(game.RULES)
    sum_correct_answers = 0
    correct_answers_for_win = 3
    while sum_correct_answers != correct_answers_for_win:
        question, correct_answer = game.generate_question_and_answer()
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            print('Correct!')
            sum_correct_answers += 1
        else:
            return print(f"'{user_answer}' is wrong answer ;(."
                         f"Correct answer was '{correct_answer}'.\n"
                         f"Let's try again, {user_name}!")
    return print(f"Congratulations, {user_name}!")
