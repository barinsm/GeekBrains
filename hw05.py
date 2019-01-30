#Урок 5. Коллекции. Список. Очередь. Словарь.

#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
import collections
companies_number = int(input('Введите количество компаний: '))
companies_dict = collections.defaultdict(list)
for i in range(companies_number):
    companie_name = input('Введите наименование {}-й компании: '.format(i+1))
    companies_profit = [float(input('Введите прибыль за {} квартал: '.format(j+1))) for j in range(4)]
    companies_dict[companie_name] = sum(companies_profit)
# print(companies_dict)
companies_avg = sum(companies_dict.values())/companies_number
print('Средняя прибыль всех компаний за год: ', companies_avg)
print('Компании с прибылью выше средней: ')
for i in companies_dict:
    if companies_dict[i] > companies_avg:
        print(i, companies_dict[i])
print('Компании с прибылью ниже средней: ')
for i in companies_dict:
    if companies_dict[i] < companies_avg:
        print(i, companies_dict[i])

#2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

#Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections
