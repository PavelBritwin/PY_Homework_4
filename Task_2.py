# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число: '))

listSM = []
x = 2
while (n >= x):
    while (n % x == 0):
        n = n / x
        if (x not in listSM):
            listSM.append(x)
    x += 1
print(listSM)