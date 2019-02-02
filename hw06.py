#Урок 6. Работа с динамической памятью

#1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.

"""
На примере Задания 4 в уроке 2:
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""
from memory_profiler import profile

# цикл
@profile
def loop(n):
    a = 1
    i = 0
    summ = 0
    while i < n:
        summ += a
        a = a / 2 * -1
        i += 1
    return summ

# рекурсия
def recursion(n, i=0, num=1, summ=0):
    if i == n:
        return summ
    elif i < n:
        return recursion(n, i+1, num/(-2), summ+num)

@profile
def recursion_2(n):
    return recursion(n)

n = int(input("Введите количество элементов: "))
print(loop(n))
print(recursion_2(n))
"""
При любом N обе реализации алгоритма занимают памяти одинаково
(например, при N=1000 объем занятой памяти 53.4 МиБ),
видимо, связано с тем, что не используются для хранения большие объемы. 
Версия Python 3.7 и разрядность ОС 64-бита.
"""



"""
На примере поиска i-го простого числа разными алгоритмами 
Количество элементов (i) вводится с клавиатуры.
"""
from memory_profiler import profile

# Вариант 1 (простой)
@profile
def simple(i):
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n

# Вариант 2 (решето Эратосфена)
@profile
def eratosfen(i):
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n*2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i-1]

i = int(input('Введите порядковый номер искомого простого числа:'))    
print(simple(i))
print(eratosfen(i))
"""
Объемы занимаемой памяти алгоритмами для поиска 1000-го простого числа:
- простой - 53.5 МиБ
- решето - 54.1 Миб
Алгоритм решета Эратосфена занимает чуть больше памяти для поиска простого числа с большим порядковым номером.
Версия Python 3.7 и разрядность ОС 64-бита.
"""
