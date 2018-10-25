# ��� ������ �������� ����� ������ � ������� ����������� �������!

import random


# �������-1:
# ��� ������, ����������� ������������� ������ �������. 
# �������� ����� ������, �������� �������� �����
# ���������� ��������� ��������� ������
# [1, 2, 4, 0] --> [1, 4, 16, 0]

list_start = [random.randint(-100, 100) for _ in range(10)]
print(list_start)
list_end = [item**2 for item in list_start]
print(list_end)


# �������-2:
# ���� ��� ������ �������.
# �������� ������ �������, �������������� � ����� �������� �������.

list_fruits_all = ['������','�����','��������','�����','������','����','�����','����������','�������','������']
list_fruits_1 = [list_fruits_all[random.randint(0, 9)] for _ in range(5)]
print(list_fruits_1)
list_fruits_2 = [list_fruits_all[random.randint(0, 9)] for _ in range(5)]
print(list_fruits_2)
# ������� ������� 1 (�� �������, �.�. �� ������� ����� � �������� ������� �, ��� ������, � �������� ������)
list_fruits_1_2 = [item for item in list_fruits_2 if item in list_fruits_1]
print(list_fruits_1_2)
# ������� ������� 2 (��������������, �.�. ������� ����� �� ���� �������)
list_fruits_1_2 = set(list_fruits_1) & set(list_fruits_2)
print(list_fruits_1_2)


# �������-3:
# ��� ������, ����������� ������������� �������.
# �������� ������ �� ��������� ���������, ��������������� ��������� ��������:
# + ������� ������ 3
# + ������� �������������
# + ������� �� ������ 4

list_start = [random.randint(-100, 100) for _ in range(100)]
print(list_start)
list_end = [item for item in list_start if item%3 == 0 and item >=0 and item%4 != 0]
print(list_end)

