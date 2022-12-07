# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

myList = []
noRepeatList = []

for i in range(20):
    myList.append(random.randrange(1, 25))
print(myList)

for j in range(len(myList)):
    if (myList[j] not in noRepeatList):
        noRepeatList.append(myList[j])

print(noRepeatList)