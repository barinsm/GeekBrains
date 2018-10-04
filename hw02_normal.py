# ������-1:
# ��� ������, ����������� ������������� ������ �������, �������� ����� ������,
# ���������� �������� ����� ���������� ����� ��������� ��������� ������,
# �� ������ ���� ���������� ���������� ����� �� ����� ���������� ����� �
# ���� ����� ������ ������ ����� �������
# ������: ����: [2, -5, 8, 9, -25, 25, 4]   ���������: [3, 5, 2]

import math
list1 = [2, -5, 8, 9, -25, 25, 4]
list2 = []
for element1 in list1:
    if element1 >= 0:
        element2 = math.sqrt(element1)
        element2_int = int(element2)
        if element2_int == element2:
            list2.append(element2_int)
print(list2)


# ������-2: ���� ���� � ������� dd.mm.yyyy, ��������: 02.11.2013.
# ���� ������ ������� ���� � ��������� ����, ��������: ������ ������ 2013 ����.
# ���������� ���������� (2000 ����, 2010 ����)

date = '02.11.2013'
day = int(date[0:2])
month = int(date[3:5])
year = int(date[6:])
day_str = ['������','������','������','���������','�����','������','�������','�������','�������','�������',
           '������������','�����������','�����������','�������������','�����������',
           '������������','�����������','�������������','�������������','���������',
           '�������� ������','�������� ������','�������� ������','�������� ���������','�������� �����',
           '�������� ������','�������� �������','�������� �������','�������� �������','��������� ',
           '�������� ������']
month_str = ['������','�������','�����','������','���','����',
             '����','�������','��������','�������','������','�������']
print(day_str[day-1], month_str[month-1], year, '����.')


# ������-3: �������� ��������, ����������� ������ ������������� ������ �������
# � ��������� �� -100 �� 100. � ������ ������ ���� n - ���������.
# ���������:
# ��� ��������� ���������� ����� ����������� ������� randint() ������ random

import random
n = 100
list = []
for idx in range(n):
    list.append(random.randint(-100, 100))
print(list)


# ������-4: ��� ������, ����������� ������������� ������ �������.
# �������� ����� ������, ���������� �������� �����: 
# �) ��������������� �������� ��������� ������:
# ��������, lst = [1, 2, 4, 5, 6, 2, 5, 2], ����� �������� lst2 = [1, 2, 4, 5, 6]
# �) �������� ��������� ������, ������� �� ����� ����������:
# ��������, lst = [1 , 2, 4, 5, 6, 2, 5, 2], ����� �������� lst2 = [1, 4, 6]

list1 = [1, 2, 4, 5, 6, 2, 5, 2]
list1_set = set(list1)
list2 = []
for element1 in list1_set:
    list2.append(element1)
print(list2)

list1 = [1, 2, 4, 5, 6, 2, 5, 2]
list1_set = set(list1)
list2 = []
for element1 in list1_set:
    if list1.count(element1) == 1:
        list2.append(element1)
print(list2)

