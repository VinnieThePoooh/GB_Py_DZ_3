# найти в массиве A[1..N] самый близкий по величине элемент к 
# заданному числу X

import random
n = int(input('Введите кличество членов в массиве: '))
x = int(input('Введите базовое значение: '))

list_1 = []
min_index = 0
difference = 0
min_difference = 10
for i in range (n):
    list_1.append(random.randint(0, 10))
    difference = x - list_1[i]
    if difference < 0:
        difference = -difference
    if difference < min_difference:
        min_difference = difference
        min_index = i

print('Сгенерированный массив: ', list_1)
print('Значение, наиболее близкое к базовому: ', list_1[min_index])