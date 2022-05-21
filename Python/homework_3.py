import subprocess
import os

def func():
    a = subprocess.getoutput('cat ~/.bash_history')
    a = a.split('\n')
    b = input('Введите команду: ')
    for el in a:
        if b == el[0:len(b)]:
            print(el)
            c = input('Мне запустить команду? Выберите y/n/q: ')
            if c == 'y':
                os.system(el)
                return
            elif c == 'n':
                continue
            elif c == 'q':
                return
            else:
                print('Команды нет, введите y/n/q: ')
                break


func()



