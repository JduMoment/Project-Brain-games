import prompt


def even_odd_game(answer, random_number):
    if answer == 'yes' and random_number % 2 == 0 or answer == 'no' and random_number % 2 != 0:
        return True
    elif answer == 'yes' and random_number % 2 != 0:
        return 'no'
    else:
        return 'yes'
