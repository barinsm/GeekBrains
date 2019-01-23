# Урок 3. Массивы. Кортежи. Множества. Списки.

# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
numbers1 = [i for i in range(2, 100)]
numbers2 = [j for j in range(2, 10)]
multiples2 = 0
for i in numbers1:
    multiples1 = 0
    for j in numbers2:
        if i % j == 0:
            multiples1 += 1
    if multiples1 > 0:
        multiples2 += 1
print('В диапазоне натуральных чисел от 2 до 99: {} чисел кратны хотя бы одному числу от 2 до 9'.format(multiples2))

# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
import random
source = [random.randint(1,100) for _ in range(10)]
result = []
for key, item in enumerate(source):
    if item % 2 == 0:
        result.append(key)
print('Исходный массив: ', source)
print('Результирующий массив: ', result)
# в результирующем массиве указаны индексы с началом нумерации от 0 

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
array = [random.randint(0, 100) for _ in range(10)]
print('Исходный массив: ', array)
minimum = min(array)
maximum = max(array)
ind_min = array.index(minimum)
ind_max = array.index(maximum)
array[ind_min], array[ind_max] = maximum, minimum
print('Результирующий массив: ', array)
print('Поменяны местами минимальный {} и максимальный элементы {} в позициях {} и {}'.format(minimum, maximum, ind_min, ind_max))
# в результирующем массиве поменяны местами минимальный и максимальный элементы, указаны индексы с началом нумерации от 0

# 4. Определить, какое число в массиве встречается чаще всего.
import random
array = [random.randint(1, 100) for _ in range(100)]
num_often = max(array, key=array.count)
print('Исходный массив: ', array)
print('В массиве чаще всего встречается число: {}, в количестве раз: {}.'.format(num_often, array.count(num_often)))

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random
array = [random.randint(-100, 100) for i in range(100)]
result = max([i for i in array if i < 0])
print('Исходный массив: ', array)
print('Максимальный отрицательный элемент в массиве: {}, его позиция в массиве: {}'.format(result, array.index(result)))

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
import random
array = [random.randint(-100, 100) for _ in range(100)]
print('Исходный массив: ', array)
minimum = min(array)
maximum = max(array)
ind_min = array.index(minimum)
ind_max = array.index(maximum)
total = 0
if ind_min < ind_max:
    for i in range(ind_min + 1, ind_max):
        total += array[i]
else:
    for i in range(ind_max + 1, ind_min):
        total += array[i]
print('Сумма элементов, находящихся между минимальным {} и максимальным {} элементами, равна: {}'.format(minimum, maximum, total))

# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.


# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.


# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

