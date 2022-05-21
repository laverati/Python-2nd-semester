import os.path

def work_with_file(name_of_file, previous_text, next_text):
    condition_1 = not os.path.isfile(name_of_file)
    condition_2 = not name_of_file[-4:] == '.txt'
    condition_3 = not os.path.exists('/home/sirius/Рабочий стол/Elizabeth.txt')
    if  condition_1 and condition_2 and condition_3:
        print('Это не файл, не .txt или такого пути не существует')
        return
    file = open(name_of_file, "r")
    st = file.read()
    st = st.replace(previous_text, next_text)
    file = open(name_of_file, "w")
    file.write(st)


work_with_file('Elizabeth.txt', '*', ' ')

