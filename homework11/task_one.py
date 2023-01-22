#ЗАДАНИЕ 1
#Написать класс User, который принимает в инициализаторе следующие значения:
#1. Имя ('John', 'Jane', 'Mary', 'David', 'Alex', 'Max', 'Nick', 'Anastasia', 'Leo')
#2. Никнейм (имя + строка из 5 случайных цифр) например: Nick13917
#3. Возраст (от 0 до 100)
#4. Цвет глаз (blue, green, brown, grey, black)

#Также класс должен содержать метод-свойство (property) info, которое возвращает словарь в 
#формате {'Name': 'Nick', 'Nickname': 'Nick1397', 'Age': 20, 'Eyes_color': 'blue'}, естественно данные
#подставляются те, которые переданы в инициализатор при создании объекта.
#Так же над объектами класса должны поддерживаться операции ==, !=, >=, <=, >, <
#В этих операциях сравнивается возраст двух объектов User.

#Также в программе реализовать функцию-генератор users_generator(number), в которую передаётся количество нужных юзеров.
#Внутри функции идёт генерация каждого юзера, согласно количеству и возвратy созданных объектов через ключевое слово yield.
#Данные для создания объекта генерировать рандомно с помощью модуля random.
#=============================================================================
#Структура программы:
#AVAILABLE_NAMES = ['John', 'Jane', 'Mary', 'David', 'Alex', 'Max', 'Nick', 'Anastasia', 'Leo']
#AVAILABLE_COLORS = ['blue', 'green', 'brown', 'grey', 'black']

#class User:
    # тут реализовать класс


#НЕ В КЛАССЕ User
#def users_generator(number):
    # тут реализовать генерацию объектов класса User


#gen = users_generator(50)
#for user in gen:
#    print(user.info) # на экран должно вывести информацию о 50 сгенерированных юзеров.

AVAILABLE_NAMES = ['John', 'Jane', 'Mary', 'David', 'Alex', 'Max', 'Nick', 'Anastasia', 'Leo']
AVAILABLE_COLORS = ['blue', 'green', 'brown', 'grey', 'black']
import random


class User:
    def __init__(self, name, nickname, age, eyes_color):
        self.name = name
        self.nickname = nickname
        self.age = age
        self.eyes_color = eyes_color
    @property
    def info(self):
        return {'Name': self.name, 'Nickname': self.nickname, 'Age': self.age, 'Eyes_color': self.eyes_color}

def users_generator(number):
    for x in range(number):
        name = random.choice(AVAILABLE_NAMES)
        nickname = name + str(random.randrange(00000, 99999))
        age = random.randrange(0, 100)
        eyes_color = random.choice(AVAILABLE_COLORS)
        u = User(name, nickname, age, eyes_color)
        print(u.info)


users_generator(2)
