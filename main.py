# class Calculator:
#     def addition(self, a, b):
#         print(a + b)
#
# calculator = Calculator()
# calculator.addition(1, 2)

# class Transport:
#     name_transport = "Класс Транспорт"
#
#     def get_transport(self):
#         return 'Метод транспорт'
#
#
#
# class Car(Transport):
#     name_car = "Атрибут car"
#
#     def get_car(self):
#         return 'Метод car'
# #
# toyota = Car()
#
# print(toyota.name_transport, toyota.get_transport())
# print(Car.name_transport)

# car = Car()
# print(car.name_car, car.get_car(), car.name_transport, car.get_transport())
# transport = Transport()
# print(transport.name_transport, transport.get_transport())

# class Transport:
#     def __init__(self, name, distance):
#         self.name = name
#         self.distance = distance
#
# class Car(Transport):
#     pass
#
# class Airplane(Transport):
#     pass
#
# class Train(Transport):
#     pass
#
# toyota = Car('Легковой автобомобиль', 100)
# tu_154 = Airplane('Самолёт', 100)
# poezd = Train('Поезд', 300)
#
# print(toyota.__dict__) #{'name': 'Легковой автобомобиль', 'distance': 100}
# print(tu_154.__dict__) #{'name': 'Самолёт', 'distance': 100}
# print(poezd.__dict__) #{'name': 'Поезд', 'distance': 300}

# class Tramsport:
#     name = 'toyota'
#
# class Avto(Tramsport):
#     pass
#
# rav4 = Avto()
#
# print(rav4.name)

# class Transport:
#     name1 = 'toyota'
#     name2 = 'subaru'
#     name3 = 'opel'
#
# class Avto(Transport):
#     name2 = 'lada'
#
# rav4 = Avto()
# rav4.name3 = 'VaZ'
#
# print(rav4.name1, rav4.name2, rav4.name3)
# print(Avto.name1, Avto.name2, Avto.name3)
# print(Transport.name1, Transport.name2, Transport.name3)

# class Cat:
#     def say_cats(self):
#         print('МЯУУ')
#
#     def say_dogs(self):
#         print('ГАВ')
#
# class Dog(Cat):
#
#     def say_dogs(self):
#         print('не гав')
#
# cat = Cat()
# cat.say_cats()
# cat.say_dogs()
# print("))))))))))))))))))))))))))))))))))")
# dog= Dog()
# dog.say_dogs()
# dog.say_cats()
#
# print(1/3)


class Animal:
    def speak(self):
        print('Метод животного')

class Dog(Animal):
    print('Woof')

class Cat(Animal):
    print('Meow')


dog = Dog()
cat = Cat()
dog.speak()
cat.speak()