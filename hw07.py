# Урок 7. Алгоритмы сортировки


# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100]. Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
import random
import timeit

# Вариант 1
def bubble_sort(orig_list):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        n += 1
    return orig_list

# Вариант 2 (доработанный)
def bubble_sort_2(orig_list):
    n = 1
    k = 0
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
                k = 1
        if k == 0:
            break
        n += 1
    return orig_list

orig_list = [random.randint(-100, 100) for _ in range(10)]

# Вариант 1
ordered_list = bubble_sort(orig_list[:])
print(orig_list)
print(ordered_list)
print(timeit.timeit('bubble_sort(orig_list[:])', setup = 'from __main__ import bubble_sort, orig_list', number = 1000000))

# Вариант 2
ordered_list = bubble_sort_2(orig_list[:])
print(orig_list)
print(ordered_list)
print(timeit.timeit('bubble_sort_2(orig_list[:])', setup = 'from __main__ import bubble_sort_2, orig_list', number = 1000000))

# Прирост скорости процентов 15-20% у варианта 2 по отношению к варианту 1


# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50]. Выведите на экран исходный и отсортированный массивы.
import random

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result

def merge_sort(sublist):
    if len(sublist) <= 1:
        return sublist
    else:
        middle = len(sublist) // 2
        left = sublist[:middle]
        right = sublist[middle:]
        left = merge_sort(left)
        right = merge_sort(right)
        result = merge(left, right)
        return result

orig_list = [random.random()*50 for _ in range(10)]
ordered_list = merge_sort(orig_list[:])
print(orig_list)
print(ordered_list)


# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
import random

def median(array, m : int):
    if len(array) == 1:
        return array[0]
    i = random.randrange(len(array))
    less = [x for x in array if x < array[i]]
    more = [x for x in array if x > array[i]]
    if m < len(less):
        return median(less, m)
    elif m >= len(array) - len(more):
        return median(more, m - (len(array) - len(more)))
    else:
        return array[i]

m = 5
size = 2 * m + 1
orig_list = [random.randint(0, 100) for _ in range(size)]
print(orig_list)
print(median(orig_list, m))

