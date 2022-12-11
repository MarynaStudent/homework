# ЗАДАНИЕ 1
#Написать функцию, которая принимает n-ое количество координат точек.
#И в ответ возвращает длину маршрута между ними.
#Каждая координата представлена кортежем, состоящим из двух объектов типа int.
#Примеры использования функции:
#result = distance((1, 1), (1, 2))
#print(result) # выведет 1

#В общем виде:
#result = distance((1, 1), (2, 3), (5, 8), ..., (xn, yn))

def distance(*args):
    sum_of_distance = 0
    for index, coords in enumerate(args):
        if index == len(args) - 1:
            break
        x1, y1 = coords
        x2, y2 = args[index+1]
        length = ((x2-x1)**2 + (y2-y1)**2)**0.5
        sum_of_distance += length
    return sum_of_distance
result = distance((1, 1), (1, 2))
print(result)

