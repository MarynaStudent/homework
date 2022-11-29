# ЗАДАНИЕ 3
#Сгенерировать список из 10 случайных элементов (чисел в диапазоне от -100 до 100) и вывести его на экран вставьте на 3-ю позицию новое случайное значение, удалите элемент из списка под индексом 6 выведите на экран новый список.
 
import random
 
arr = []
for i in range(10):
 arr.append(random.randrange(-100, 100))
 
print('array:')
print(arr)
 
# replace 3
arr[2] = random.randrange(-100, 100)
print('replace 3:')
print(arr)
 
# removed by index 6
arr.pop(6)
 
print("result:")
print(arr)