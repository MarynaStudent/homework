#Создать класс треугольник Triangle в программе. В инициализаторе класс должен принимать три переменные a, b, c. 
#Каждая переменная должна хранить целое число - одну из сторон треугольника.
#При инициализации реализовать проверку может ли существовать треугольник с такими сторонами.
#Если не может вызвать исключение ValueError.
#Если может, то присвоить эти значение атрибутам класса.
#Также класс должен содержать метод:
#is_right_angled(self) - возвращает true, если треугольник прямоугольный и False если нет
#Также между объектами класса должна поддерживаться операции == !=, 
#которые сравнивали бы периметры треугольников
#Пример работы программы:
#class Triangle:
#    def __init__(self, a, b, c):
#        # тут прописать проверку и инициализацию
    
    # тут прописать методы
#t1 = Triangle(3, 4, 5)
#print(t1.is_right_angled()) # выведет True
#t2 = Triangle(10, 10, 22) # вызовет ошибку ValueError
#t3 = Triangle(11, 11, 20)
#print(t3.is_right_angled()) # выведет False
#t1 != t3 # выведет True, так как периметр треугольника t3 не равен периметру треугольника t1.
class Triangle:

    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c
    def is_right_angled(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            res = f'Triangle: {self.a}, {self.b}, {self.c}'
            if self.a**2 + self.b**2 == self.c**2:
                res = True
            else:
                res = False
        else:
            raise ValueError
        return res 
    def perimetr(self):
        return self.a + self.b + self.c
    def __eq__(self, other):
        
        print(self)
        print(other)


t1 = Triangle(3, 4, 5)
t2 = Triangle(10, 10, 22)
t3 = Triangle(11, 11, 20)

print(t3.is_right_angled())
print(t1 != t3)
        