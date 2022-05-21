# Функцию принимает список аргументов, выравнивая по словам ('center', 'left', 'right')
# Например, ввод: список [1, 2, 3], 'center', '*' ------ Вывод: ****1****
#                                                               ****2****
#                                                               ****3****

def func(list, cen, simvol, num):
    if cen == 'center':
        cen = '^'
    elif cen == 'left':
        cen = '<'
    elif cen == 'right':
        cen = '>'
    else:
        print("Ошибка, надо выбрать center, left, right")
        return
    a = "{:" + simvol + cen + str(num) + "}"
    b = ''
    for el in list:
        b += a.format(el) + "\n"
    print(b)
    return b

func([1, 2, 3], 'center', '*', 9)