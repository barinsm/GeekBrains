import os
import sys


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

print('\n*** Задача-1 ***\n')

dir_path_start = os.path.join('.', 'dir_')

for idx in range(1,10):
    dir_path = dir_path_start + str(idx)
    print(dir_path)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')
    else:
        print('Такая директория создана')

for idx in range(1,10):
    dir_path = dir_path_start + str(idx)
    print(dir_path)
    try:
        os.rmdir(dir_path)
    except FileNotFoundError:
        print('Такая директория НЕ существует')
    else:
        print('Такая директория удалена')
        

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print('\n*** Задача-2 ***\n')

# вариант 1
print('Список только непосредственных папок в текущей директории:')
with os.scandir('.') as it:
    for entry in it:
        if entry.is_dir():
            print(entry.name)
# вариант 2
print('Список только непосредственных папок в текущей директории:')
dir_list = next(os.walk('.'))[1]
for x in dir_list:
    print(x)

# вариант 3
dir_list = [x[0] for x in os.walk('.')]
print('Количество всех вложенных папок текущей директории (включая ее) - {}, и список этих папок с путями от текущей папки:'.format(len(dir_list)))
for x in dir_list:
    print(x)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

print('\n*** Задача-3 ***\n')

file_path_1 = sys.argv[0]
file_path_2 = sys.argv[0]+'_copy'
with open(file_path_1, 'rb') as src, open(file_path_2, 'wb') as dst: dst.write(src.read()) 
print('Файл {} скопирован в файл-копию {}'.format(file_path_1, file_path_2))

