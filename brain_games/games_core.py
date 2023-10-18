import prompt

from brain_games.cli import welcome_user

COORECT_ANSWERS_FOR_WIN = 3


def play(game):
    user_name = welcome_user()
    print(game.RULES)
    sum_correct_answers = 0
    while sum_correct_answers != COORECT_ANSWERS_FOR_WIN:
        question, correct_answer = game.generate_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if str(correct_answer) == str(user_answer):
            print('Correct!')
            sum_correct_answers += 1
        else:
            return print(f"'{user_answer}' is wrong answer ;(."
                         f"Correct answer was '{correct_answer}'.\n"
                         f"Let's try again, {user_name}!")
    return print(f"Congratulations, {user_name}!")
