# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    int_prt = number // 1
    dec_prt = number % 1
    unrnd_prt = dec_prt * 10**ndigits
    rnd_prt = unrnd_prt % 1 
    add = rnd_prt * 2 // 1
#     print (int_prt, dec_prt, unrnd_prt, rnd_prt, add)
    return int_prt + (unrnd_prt + add) // 1 / 10**ndigits 


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_str = str(ticket_number)
    if len(ticket_str) != 6:
        return 'Ошибка'
    left_prt = ticket_str[:3]
    right_prt = ticket_str[3:]
    summ = 0
    for idx in range(3):
        summ += int(left_prt[idx])
        summ -= int(right_prt[idx])
    if summ  == 0:
        return 'Счастливый билет'
    else:
        return 'Несчастливый билет'
    

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
