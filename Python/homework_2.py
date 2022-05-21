import random

# класс машины, принимает скорость машины и имя машины
class Car:
    def __init__(self, speed, name):
        self.speed = speed
        self.name = name

def get_speed(car):
    return car.speed

# класс гонки, принимает длину круга, есть метод play
class Races:
    def __init__(self, track_len):
        self.track_len = track_len

    def play(self, array_of_car, cicle):
        array_result = []
        for i in range(cicle):
            b = len(array_of_car) - 1
            a = random.randint(0, b)
            array_result.append(array_of_car.pop(a))  # pop удаляет по рандомному индексу
                                                      # машинку из списка машинок и возвращает ее в скобки
                                                      # append берет из этих скобок удаленный элемент и ставит в
                                                      # конец результирующего списка
        array_result += sorted(array_of_car, key=get_speed)
        return array_result


c1 = Car(70, "Ferrari")
c2 = Car(80, "Tesla")
c3 = Car(120, "Bentley")
c4 = Car(80, "Nissan")
c5 = Car(30, "Toyota")
c6 = Car(80, "Porsche")

array_of_car = [c1, c2, c3, c4, c5, c6]

race = Races(6)

l = race.play(array_of_car, 3)
for i, el in zip(range(len(l),0,-1), l):
    print(i, el.name)