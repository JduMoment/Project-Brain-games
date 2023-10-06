def nod(num):
    prime_factors_num = []
    d = 2
    while d * d <= num:
        if num % d == 0:
            prime_factors_num.append(d)
            num //= d
        else:
            d += 1
    if num > 1:
        prime_factors_num.append(num)
    return prime_factors_num
