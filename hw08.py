# Урок 8. Деревья. Хэш-функция

# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
str_in = input('Введите строку, состоящую только из маленьких латинских букв: ')
substr = set()
for i in range(len(str_in)):
    if i == 0:
        n = len(str_in) - 1
    else:
        n = len(str_in)
    for j in range(n, i, -1):
        substr.add(hash(str_in[i:j]))
print('Количество различных подстрок в строке: ', len(substr))

# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
class Node(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def branch(self):
        return (self.left, self.right)

def tree(node, left=True, bin=''):
    if type(node) is str:
        return { node: bin }
    l, r = node.branch()
    dic = {}
    dic.update(tree(l, True, bin + '0'))
    dic.update(tree(r, False, bin + '1'))
    return dic

str_in = 'one more time!'
count = {}
for i in str_in:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
n = sorted(count.items(), key=lambda x: x[1], reverse=True)
while len(n) > 1:
    k1, c1 = n[-1]
    k2, c2 = n[-2]
    n = n[:-2]
    node = Node(k1, k2)
    n.append((node, c1 + c2))
    n = sorted(n, key=lambda x: x[1], reverse=True)
code = tree(n[0][0])
print('Исходная строка: ', str_in)
print('Закодированная строка:')
for i in str_in: print(code[i], '', end='')

