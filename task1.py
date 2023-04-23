# Требуется вычислить, сколько раз встречается некоторое число X в 
# массиве A[1..N]
import random
n = int(input('Введите кличество членов в массиве: '))
x = int(input('Введите искомое значение: '))

list_1 = []
count_x = 0

for i in range (n):
    list_1.append(random.randint(0, 10))
    if list_1[i] == x:
        count_x += 1

print('Сгенерированный массив: ',list_1)

print('Колличество ',x ,' в массиве: ', count_x)
