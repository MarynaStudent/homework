#ЗАДАЧА 3:
#Программа на вход должна принимать файл с каким-то текстом. Пользователь вводит любую английскую букву.
#Программа должна считать сколько раз эта буква встречается в тексте (без учёта регистра). То есть буквы n и N 
#считать одинаковыми.

#Пример работы:
#Введите букву: n
#Результат: буква встречается 124 раза в тексте.

f = open('test.txt', 'r')
text = f.read().lower()
find = input('Введите букву: ').lower()
count = text.count(find)
print(count)
f.close()



#text = input('text:').lower()
#find = input('find:').lower()
#count = text.count(find)
#print(count)