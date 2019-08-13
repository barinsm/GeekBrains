# coding: utf-8

import yaml
import socket
from argparse import ArgumentParser

'''
Описываем конфигурацию по умолчанию
'''
config = {
    'host': '127.0.0.1',
    'port': 8000,
    'buffersize': 1024
}

'''
Создаём объект парсера аргументов командной строки
'''
parser = ArgumentParser()

'''
Добавляем аргументы для парсинга
Перечень допустимых аргументов конфигурации аргумента командной строки можно найти здесь:
https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument
'''
parser.add_argument(
    '-c', '--config', type=str, required=False,
    help='Sets config file path'
)
parser.add_argument(
    '-ht', '--host', type=str, required=False,
    help='Sets server host'
)
parser.add_argument(
    '-p', '--port', type=int, required=False,
    help='Sets server port'
)

'''
Создаем пространство имён args на основе аргументов командной строки
https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args
'''
args = parser.parse_args()

'''
Обновляем конфигурацию на основе словаря
Подробнее о словарях python можно узнать здесь:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries
'''
if args.config:
    with open(args.config) as file:
        file_config = yaml.safe_load(file)
        config.update(file_config or {})

if args.host:
    config['host'] = args.host

if args.port:
    config['port'] = args.port

'''
Код в теле данной конструкции будет выполнен только в случае запуска данного модуля
python client.py [-c] [-p] [-ht]
'''
if __name__ == '__main__':
    try:
        '''
        Создаём сокет
        https://docs.python.org/3/library/socket.html#socket.socket
        '''
        sock = socket.socket()
        '''
        Подключаемся к серверу по его IP
        Если сервер не запущен метод connect вызовет ошибку
        '''
        sock.connect((config.get('host'), config.get('port')))

        print('Client was started')

        data = input('Enter data: ')
        '''
        Отправляем данные на сервер
        '''
        sock.send(data.encode())
        print('Client send data')
        '''
        Принимаем ответ сервера
        '''
        bytes_response = sock.recv(config.get('buffersize'))
        print(bytes_response.decode())
        '''
        Закрываем сокет
        '''
        sock.close()
    except KeyboardInterrupt:
        '''
        В случае нажатия сочетания клавиш Ctrl+C(Ctrl+Backspace на windows)
        обрабатываем завершение работы клиента
        '''
        print('Client shutdown')

