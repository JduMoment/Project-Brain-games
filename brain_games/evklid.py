def theory_of_evklid(num1, num2):
    while num1 > 0 and num2 > 0:
        num1 = num1 % num2
        if num1 != 0:
            num2 = num2 % num1
    return max(num1, num2)


def nod_evklid(numeric1, numeric2):
    if numeric1 > numeric2:
        return theory_of_evklid(numeric1, numeric2)
    elif numeric2 > numeric1:
        return theory_of_evklid(numeric2, numeric1)
