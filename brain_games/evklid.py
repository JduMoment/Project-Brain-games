def nod_evklid(num1, num2):
    if num1 > num2:
        while num1 > 0 and num2 > 0:
            num1 = num1 % num2
            if num1 != 0:
                num2 = num2 % num1
        if num1 > num2:
            return num1
        else:
            return num2
    elif num2 > num1:
        while num2 > 0 and num1 > 0:
            num2 = num2 % num1
            if num2 != 0:
                num1 = num1 % num2
        if num2 > num1:
            return num2
        else:
            return num1
