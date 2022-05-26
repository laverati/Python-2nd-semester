from datetime import datetime
from netifaces import interfaces, ifaddresses, AF_INET
import platform
import socket
import ipaddress
import click
import os

menu_options = [
    'Информация об операционной системе',
    'Информация о хосте и dns',
    'Информация о сети',
    'Выход'
]

def menu():
    menu = 'Меню'
    current_date = str(datetime.now().date())
    print(current_date.center(len(current_date) + 13))  # выравнивает по центру
    print('-' * 27)
    print(menu.center(len(menu) + 20))
    print('-' * 27)
    for i in range(len(menu_options)):
        print(f'{i + 1}. {menu_options[i]}')

def system_info():
    name_1 = 'Системная информация'
    print('-' * 27)
    print(name_1.center(len(name_1) + 7))
    print('-' * 27)
    print('Имя операционной системы: ', platform.system())

def host_info():
    print('-' * 27)
    print('Имя хоста и информация о DNS')
    print('-' * 27)
    print("IP-адрес :", socket.gethostbyname(socket.gethostname()))
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])]
        print(' '.join(addresses))

def network_info():
    name_2 = 'Сетевая информация'
    print('-' * 27)
    print(name_2.center(len(name_2) + 7))
    print('-' * 27)
    ipv4 = ipaddress.ip_address('10.0.1.1')
    print(ipv4)

def start():
    choice = 0
    while(choice != len(menu_options)):
        menu()
        choice = int(input(f'Ввведите цифру от 1 до {len(menu_options)}: '))
        if choice == 1:
            system_info()
        elif choice == 2:
            host_info()
        elif choice == 3:
            network_info()
        elif choice == 4:
            print('Чао!')
            break
        else:
            print(f'Пожалуйста, выберите только от 1 до {len(menu_options)}')
        input('Нажмите Enter для продолжения')
        os.system('clear')


start()
