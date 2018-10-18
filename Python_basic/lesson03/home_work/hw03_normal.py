# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    febon_list = [1,1]
    for idx in range(2,m):
        febon_list.append(febon_list[idx-2] + febon_list[idx-1])
    return febon_list[n-1:m]

print(fibonacci(6,10))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    result_list = origin_list.copy()
    list_len = len(origin_list)
    if (list_len == 0):
        return ();
    swap_cnt = 0
    idx = 0
    while idx < list_len:
        if (idx + 1) != list_len and result_list[idx] > result_list[idx + 1]:
            result_list[idx], result_list[idx + 1] = result_list[idx+1], result_list[idx]
            swap_cnt = 1
        idx += 1
        if idx == list_len and swap_cnt == 1:
            swap_cnt = 0
            idx = 0
    return result_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def user_filter(function, iterator):
    result_iterator = []
    for item in iterator:
        if function(item):
            result_iterator.append(item)
    return result_iterator

print(user_filter((lambda x: x%2), [1,2,3,4,5,6,7,8,9,10]))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def parallelogram(a1, a2, a3, a4):
    if a1[1] - a3[1] == a2[1] - a4[1]:
        if a1[0] - a2[0] == a3[0] - a4[0]:
            return True

print(parallelogram((0,2),(2,2),(0, 0),(2,0)))
