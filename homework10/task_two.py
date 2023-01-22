#Задание 2
#Создайте класс Student, содержащий поля: фамилия и имя, номер группы, успеваемость (массив из пяти элементов, каждый элемент число от 1 до 10). 
#Проверить что фамилия и имя строки через property. Если не строка, вызываем ошибку ValidationError.
#Создать класс School, содержащий список учеников (изначально пустой):
#Добавить возможность для добавления студентов в школу (метод add_student)
#Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 5 или 6. Метод (get_best_students) 
#Добавить возможность вывода учеников заданной группы (get_students(self, group_number))
#Добавить возможность вывода учеников претендующих на автомат(средний балл >= 7) (get_students_without_exams)

# Задание 2
# Создайте класс Student, содержащий поля: фамилия и имя, номер группы, успеваемость (массив из пяти элементов, каждый элемент число от 1 до 10).
# Проверить что фамилия и имя строки через property. Если не строка, вызываем ошибку ValidationError.
# Создать класс School, содержащий список учеников (изначально пустой):
# Добавить возможность для добавления студентов в школу (метод add_student)
# Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 5 или 6. Метод (get_best_students)
# Добавить возможность вывода учеников заданной группы (get_students(self, group_number))
# Добавить возможность вывода учеников претендующих на автомат(средний балл >= 7) (get_students_without_exams)

class Student:
    def __init__(self, name, surname, group_number, score):
        self.name = name
        self.surname = surname
        self.group_number = group_number
        self.score = score

    @property
    def name(self):
        if not isinstance(self._name, str):
            raise ValueError
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def surname(self):
        if not isinstance(self._surname, str):
            raise ValueError
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_best_students(self):
        for s in self.students:
            for score in s.score:
                if score == 5 or score == 6:
                  print(f'get_best_students | surname: {s.surname} | group_number: {s.group_number} | score: {s.score}')

    def get_students(self, group_number):
        for s in self.students:
            if s.group_number == group_number:
                print(f'get_students | surname: {s.surname} | group_number: {s.group_number}')

    def get_students_without_exams(self):
        for s in self.students:
            if exist_score_without_exams(s.score):
                print(f'get_students_without_exams | surname: {s.surname} | group_number: {s.group_number}')


def exist_score_without_exams(scores):
    for score in scores:
        if score >= 7:
            return True


a = Student('Marina', 'Shurpakova', 'QAP11-onl', [6, 7, 8, 9, 10])
b = Student('Dimka', 'Isaev', 'QAP11-onl', [1, 2, 3])

print(a.name)

s = School()
s.add_student(a)
s.add_student(b)

print(s.get_best_students())

