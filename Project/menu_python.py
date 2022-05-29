from datetime import datetime
import platform
import socket
import os
from uuid import getnode as get_mac  # библиотека для получения MAC-адреса


menu_options = [
    'Информация об операционной системе',
    'Информация о памяти',
    'Информация о сети',
    'Выход'
]

line = '-' * 27


def menu():  # функция, показывающая меню
    menu = 'Меню'
    current_date = str(datetime.now().strftime("%F %T"))  # показывает дату
    print(f"{current_date.center(len(current_date) + 7)}\n{line}\n{menu.center(len(menu) + 20)}\n{line}")
    for i in range(len(menu_options)):  # выводит на экране пункты меню
        print(f'{i + 1}. {menu_options[i]}')


def system_info():  # функция, выводит системную информацию
    name_1 = 'Системная информация'
    print(f"{line}\n{name_1.center(len(name_1) + 7)}\n{line}\nИмя операционной системы: "
          f"{platform.system()}\nАрхитектура: {platform.architecture()[0]}\nИмя хоста: {platform.node()}")


def memory_info():  # функция, выводит информацию о памяти
    name_2 = 'Информация о памяти'
    print(f"{line}\n{name_2.center(len(name_2) + 7)}\n{line}")
    with open("/proc/meminfo", "r") as f:  # открывает файл на чтение
        lines = f.readlines()              # строки в файле --> список
    print("     " + lines[0].strip() + "\n     " + lines[1].strip())  # strip удаляет лишние пробелы


def network_info():  # функция, выводит информацию о сети
    name_3 = 'Сетевая информация'
    print(f"{line}\n{name_3.center(len(name_3) + 7)}\n{line}")
    ip = socket.gethostbyname(socket.getfqdn())  # IP-адрес
    print('IP-адрес: ', ip)
    mac = get_mac()  # MAC-адрес
    h = iter(hex(mac)[2:].zfill(12))  # преобразует 48-байтовое представление
    print('MAC-адрес: ', ":".join(i + next(h) for i in h))  # добавляет ":"


def start():  # основная логика программы
    choice = 0
    while(choice != len(menu_options)):
        menu()
        choice = int(input(f'Ввведите цифру от 1 до {len(menu_options)}: '))
        if choice == 1:
            system_info()
        elif choice == 2:
            memory_info()
        elif choice == 3:
            network_info()
        elif choice == 4:
            print('Чао!')
            break
        else:
            print(f'Пожалуйста, выберите только от 1 до {len(menu_options)}')
        input('Нажмите Enter для продолжения')
        os.system('clear')  # очищает консоль


start()
