#Урок 4. Эмпирическая оценка алгоритмов на Python

#1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
#Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
На примере Задания 4 в уроке 2:
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""
import timeit

# цикл
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

n = int(input("Введите количество элементов: "))
# print(loop(n))
# print(recursion(n))
print(timeit.timeit('loop(n)', setup='from __main__ import n,loop', number= 1000))
print(timeit.timeit('recursion(n)', setup='from __main__ import n,recursion', number= 1000))

"""
При небольшом N<=100 обе реализации алгоритма считают примерно одинаково
(например, при N=100 и 1000 повторных расчетов длятся 0,023 и 0,024 секунды),
но уже при N>=200 регресия отстает и может считать до 2 раз дольше чем цикл,
видимо, связано с дополнительными вызовами вложенных функций
(например, при N=1000 и 1000 повторных расчетов длятся 0,16 и 0,30 секунды).
Сложность алгоритма в обоих случаях линейная O(n)
"""

#2. Написать два алгоритма нахождения i-го по счёту простого числа.
#Без использования «Решета Эратосфена»;
#Используя алгоритм «Решето Эратосфена»
import timeit

# Вариант 1 (простой)
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
# print(simple(i))
# print(eratosfen(i))
print(timeit.timeit("simple(i)", setup="from __main__ import simple,i", number=100))
print(timeit.timeit("eratosfen(i)", setup="from __main__ import eratosfen,i", number=100))

"""
Время работы алгоритмов для поиска 10-го простого числа 100 раз:
- простой - 0.002
- решето - 0.391
Время работы алгоритмов для поиска 100-го простого числа 100 раз:
- простой - 0.257
- решето - 0.384
Время работы алгоритмов для поиска 1000-го простого числа 100 раз:
- простой - 43.141
- решето - 0.430
Алгоритм решета Эратосфена эффективен для поиска простого числа с большим порядковым номером.
Сложность простого алгоритма O(n^2)
Сложность решета Эратосфена O(n log(log n))
"""

#Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.

