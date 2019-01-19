# Урок 2. Циклы. Рекурсия. Функции.

# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
while True:
    numbers = input('Введите через запятую два числа: ').split(',')
    a = int(numbers[0])
    b = int(numbers[1])
    oper = input('Введите знак оперции ("+", "-", "*", "/") или "0" для выхода: ')
    if oper == '0': break
    elif oper == '+': print ('Сумма двух чисел: ', a + b)
    elif oper == '-': print ('Разность двух чисел: ', a - b)
    elif oper == '*': print ('Произведение двух чисел: ', a * b)
    elif oper == '/':
        if b != 0: print ('Частное двух чисел: ', a / b)
        else: print('Деление на ноль невозможно!')
    else: print('Неверная операция, повторите ввод!')

# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
number = input('Введите натуральное число: ')
even = 0
odd = 0
for i in number:
    if int(i) % 2 == 0: even += 1
    else: odd += 1
print('Четных цифр: ', even)
print('Нечетных цифр: ', odd)

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
number = input('Введите натуральное число: ')
number_backward = ''
for i in number:
    number_backward = i + number_backward
print('Число наоборот: ',number_backward)

# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
n = int(input('Введите количество элементов ряда чисел: '))
total = 1
number = 1
for i in range(1,n):
    number /= -2
    total += number
print('Сумма {} элементов ряда: {}'.format(n, total))

# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
start = 32
end = 127
for i in range(start, end+1):
    if i < 100: print(end = ' ')
    print(i, chr(i), end = ' ')
    if (i + 1 - start) % 10 == 0: print()

# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
import random
number = random.randint(0,100)
for i in range(10):
    guess = int(input('Введите ваше число: '))
    if guess > number: print('Ваше число больше загадонного')
    if guess < number: print('Ваше число меньше загадонного')
    if guess == number:
        print('Вы угадали число!')
        break
print('Загаданное число: ', number)

# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
