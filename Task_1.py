# Вычислить число pi c заданной точностью d
# при d = 0.001 pi = 3.141. 10^(-1) <= d <= 10^(-10)

d = float(input('Введите точность числа pi: '))
pi = 3.1415926535

def roundPI(x):
    count = 0
    while (x < 1):
        x = x * 10
        count = count + 1
    return round(pi, count)

print(roundPI(d))