from datetime import datetime
import platform, socket, os
from uuid import getnode as get_mac # библиотека для получения MAC-адреса


menu_options = [
    'Информация об операционной системе',
    'Информация о памяти',
    'Информация о сети',
    'Выход'
]

line = '-' * 27

def menu():
    menu = 'Меню'
    current_date = str(datetime.now().strftime("%F %T"))
    print(current_date.center(len(current_date) + 7))  # выравнивает по центру
    print(line)
    print(menu.center(len(menu) + 20))
    print(line)
    for i in range(len(menu_options)):
        print(f'{i + 1}. {menu_options[i]}')

def system_info():
    name_1 = 'Системная информация'
    print(line)
    print(name_1.center(len(name_1) + 7))
    print(line)
    print('Имя операционной системы: ', platform.system())
    print("Архитектура: " + platform.architecture()[0])
    print('Имя хоста: ', platform.node())

def memory_info():
    name_2 = 'Информация о памяти'
    print(line)
    print(name_2.center(len(name_2) + 7))
    print(line)
    with open("/proc/meminfo", "r") as f:
        lines = f.readlines()
    print("     " + lines[0].strip())
    print("     " + lines[1].strip())

def network_info():
    name_3 = 'Сетевая информация'
    print(line)
    print(name_3.center(len(name_3) + 7))
    print(line)
    ip = socket.gethostbyname(socket.getfqdn())  # IP-адрес системы
    mac = get_mac()  # MAC адрес
    h = iter(hex(mac)[2:].zfill(12)) # преобразуем 48-байтовое представление MAC-адреса в формат ff:ff:ff:ff:ff:ff
    print('IP-адрес: ', ip)
    print('MAC-адрес: ', ":".join(i + next(h) for i in h))

def start():
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
        os.system('clear')


start()
