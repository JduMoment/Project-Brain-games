from random import randint


import prompt


from brain_games.cli import welcome_user


def theory_of_evklid(num1, num2): #Вычисляем dd
    while num1 > 0 and num2 > 0:
        num1 = num1 % num2
        if num1 != 0:
            num2 = num2 % num1
    return max(num1, num2)


def what_is_gcd(numeric1, numeric2):
    if numeric1 > numeric2:
        return theory_of_evklid(numeric1, numeric2)
    elif numeric2 > numeric1:
        return theory_of_evklid(numeric2, numeric1)


def gcd_game():
    user_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    sum_correct_answers = 0
    while sum_correct_answers != 3:
        first_num = randint(1, 75)
        last_num = randint(1, 75)
        print(f"Question: {first_num} {last_num}")
        answer = prompt.string('Your answer: ')
        if first_num == last_num:
            nod = first_num
        elif first_num == 1 or last_num == 1:
            nod = 1
        else:
            nod = what_is_gcd(first_num, last_num)
        if int(answer) == int(nod):
            print('Correct!')
            sum_correct_answers += 1
        else:
            return print(f"'{answer}' is wrong answer ;(."
                         f"Correct answer was '{nod}'.\n"
                         f"Let's try again, {user_name}!")
    return print('Congratulations, ' + user_name + '!')
