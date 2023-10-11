import prompt


from brain_games.cli import welcome_user


from random import randint


def is_prime(num):
    i = 2
    while num > i:
        is_prime = num % i
        i += 1
        if is_prime == 0:
            return False
    return True


def prime_number():
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    sum_correct_answers = 0
    while sum_correct_answers != 3:
        num = randint(1, 1000)
        print(f"Question: {num}")
        answer = prompt.string('Your answer: ')
        prime = is_prime(num)
        if prime is True and answer == 'yes':
            print('Correct!')
            sum_correct_answers += 1
        elif prime is False and answer == 'no':
            print('Correct!')
            sum_correct_answers += 1
        else:
            return print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\n"
                         f"Let's try again, {user_name}!")
    return print('Congratulations, ' + user_name + '!')
