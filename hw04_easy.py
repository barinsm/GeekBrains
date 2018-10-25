# Все задачи текущего блока решите с помощью генераторов списков!

import random


# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

list_start = [random.randint(-100, 100) for _ in range(10)]
print(list_start)
list_end = [item**2 for item in list_start]
print(list_end)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

list_fruits_all = ['яблоко','груша','апельсин','банан','гранат','лайм','лимон','грейпфрукт','абрикос','персик']
list_fruits_1 = [list_fruits_all[random.randint(0, 9)] for _ in range(5)]
print(list_fruits_1)
list_fruits_2 = [list_fruits_all[random.randint(0, 9)] for _ in range(5)]
print(list_fruits_2)
# вариант решения 1 (не идеален, т.к. НЕ убирает дубли в исходных списках и, что важнее, в конечном списке)
list_fruits_1_2 = [item for item in list_fruits_2 if item in list_fruits_1]
print(list_fruits_1_2)
# вариант решения 2 (предпочтителен, т.к. убирает дубли во всех списках)
list_fruits_1_2 = set(list_fruits_1) & set(list_fruits_2)
print(list_fruits_1_2)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

list_start = [random.randint(-100, 100) for _ in range(100)]
print(list_start)
list_end = [item for item in list_start if item%3 == 0 and item >=0 and item%4 != 0]
print(list_end)

