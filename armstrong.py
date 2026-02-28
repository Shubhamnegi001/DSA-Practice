def is_armstrong(num):
    n = num
    power = len(str(num))
    sum = 0
    while  n > 0:
        ld = n % 10
        sum += ld**power
        n = n // 10
    return sum == num
print(is_armstrong())