# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
for idx, fruit in enumerate(fruits):
    print('{}.\t{}'.format(idx+1, fruit))
print()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list1 = [6, 1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
for element in list2:
    while element in list1:
        list1.remove(element)
print(list1)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list1 = [1, 2, 3, 4, 5, 6]
list2 = []
for element in list1:
    list2.append(element/4 if element % 2 == 0 else element * 2)
print(list2)

