#ЗАДАЧА 2
#Написать функцию is_right_angle_triangle(a, b, c), которая принимает на вход 3 числа, 
#которые записываются в три переменные a, b, c.
#При этом самое большое число попадает в переменную c, самое маленькое в переменную a, среднее в переменную b. 
#Функция должна:
#1. Проверить может ли существовать треугольник с такими сторонами
#(сумма любых двух сторон должна быть больше третьей)
#2. Если треугольник не может существовать функция возвращает словарь
#{
#    'result': False,
#    'description': 'no such triangle exists'
#}
#3. Если треугольник может существовать, то функция проверяет является ли
#треугольник прямоугольным (сумма квадратов меньших сторон (катетов) должна равняться
#квадрату наибольшой стороны (гипотенузы))
#4. Если треугольник не явяляется прямоугольным, то функция возвращает  словарь
#{
#    'result': False,
#    'description': 'the triangle is not right-angled'
#}
#5. A если является, то возвращает словарь
#{
#    'result': True,
#    'description': 'the triangle is right-angled'
#}

#Примеры использования:
#result = is_right_angle_triangle(3, 4, 5)
#print(result) 
# {
#    'result': True,
#    'description': 'the triangle is right-angled'
# } 
# так как из этих чисел можно собрать 
# прямоугольный треугольник (3, 4 - катеты, 5 - гипотенуза)

#result = is_right_angle_triangle(3, 5, 9)
#print(result) 
# {
#    'result': False,
#    'description': 'no such triangle exists'
# } 
# так как из этих чисел нельзя собрать треугольник

#result = is_right_angle_triangle(11, 11, 21)
#print(result) 
# {
#    'result': False,
#    'description': 'the triangle is not right-angled'
# } 
# так как из этих чисел можно собрать треугольник, но
# но не прямоугольный.


def is_right_angle_triangle(a, b, c):
 
    result = {}
    if  a + b > c and a + c > b and b + c > a:
        print('if 1')
        result['success'] = True
        result['description'] = 'the triangle is right-angled'
        if a**2 + b**2 == c**2: 
            print('if 2')
            result['success'] = True
            result['description'] = 'the triangle is right-angled'
        else:
                print('else 1')
                result['success']= False
                result['description'] = 'the triangle is not right-angled'
    else:
        print('else 2')
        result['success'] = False 
        result['description'] = 'no such triangle exists'
    
    return result 


result = is_right_angle_triangle(3, 5, 9)
print(result)


    


