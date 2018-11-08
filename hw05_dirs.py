import os

def change_dir(path=''):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print('Невозможно перейти в папку ', path)
    else:
        print('Успешно перешел в папку ', path)

def show_dir(path='.'):
    try:
        os.listdir(path)
    except FileNotFoundError:
        print('Невозможно вывести содержимое папки ', path)
    else:
        print('Содержимое папки ',path,':')    
        for name in os.listdir(path):
            print(name)

def del_dir(path=''):
    try:
        os.rmdir(path)
    except FileNotFoundError:
        print('Невозможно удалить папку ', path)
    else:
        print('Успешно удалена папка ', path)

def make_dir(path=''):
    try:
        os.mkdir(path)
    except FileExistsError:
        print('Невозможно создать папку ', path)
    else:
        print('Успешно создано папка ', path)

if __name__ == '__main__':
    make_dir('test')
    show_dir('test')
    change_dir('test')
    show_dir()
    change_dir('..')
    del_dir('test')
    