# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random
k = int(input('Введите степень многочлена: '))
polinomial = ''
while (k >= 0):
    y = random.randrange(0, 9)
    if (y != 0):
        if (polinomial == ''):
            polinomial += f'{y}*x^{k}'
            k -= 1
            continue
        if (k == 1):
            polinomial += f' + {y}*x'
            k -= 1
            continue
        if (k == 0):
            polinomial += ' + ' + str(y)
            break
        polinomial += f' + {y}*x^{k}'
        k -= 1
    else:
        k -= 1
polinomial += ' = 0'
print(polinomial)
with open("file.txt", "w") as text_file:
    text_file.write(f'{polinomial}\n')