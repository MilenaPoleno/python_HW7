"""Реализуйте базовый класс Car.
У данного класса должны быть
следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go,
stop, turn(direction), которые должны
сообщать, что машина поехала,
остановилась, повернула (куда).
Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод
show_speed, который должен показывать
текущую скорость автомобиля.
Для классов TownCar и WorkCar
переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться
сообщение о превышении скорости.
Создайте экземпляры классов, передайте
значения атрибутов. Выполните доступ к
атрибутам, выведите результат.
Выполните вызов методов и также
покажите результат."""


class Car:

    def __init__(self, color, name, is_police):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f"Скорость {speed} км/ч")

    def stop(self):
        self.speed = 0
        print("Остановка")

    def turn(self, direction):
        if self.speed > 0:
            print(f"Поворот {direction}")
        else:
            print("Остановка")

    def show_speed(self):
        print(f"Скорость {self.speed} км/ч")


class TownCar(Car):

    def __init__(self, color, name):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость превышена на "
                    f"{self.speed - 60} км/ч")
        else:
            print(f"Скорость {self.speed} км/ч")


class SportCar(Car):

    def __init__(self, color, name):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False


class WorkCar(Car):

    def __init__(self, color, name):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость превышена на "
                    f"{self.speed - 40} км/ч")
        else:
            print(f'Скорость {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, color, name):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True


def test_drive(move):
    print(f"Тест-драйв {'полицейского' if move.is_police else 'гражданского'} автомобиля {move.name}, цвет {move.color}")
    move.go(20)
    move.show_speed()
    move.turn("направо")
    move.stop()
    move.show_speed()
    move.turn("налево")
    move.go(100)
    move.show_speed()
    move.go(70)
    move.show_speed()
    move.stop()
    print("Тест-драйв окончен", end="\n\n")


town = TownCar("черный", "Ford")
test_drive(town)

sport = SportCar("красный", "Ferrari")
test_drive(sport)

work = WorkCar("серый", "BMW")
test_drive(work)

police = PoliceCar("белый", "KIA")
test_drive(police)
