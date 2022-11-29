# ЗАДАНИЕ 2
#Пользователь вводит строку в консоли состоящую из двух слов, например: “Ivan Ivanou”Поменять слова местами и вывести на экран новую строку: Ivanou Ivan
name = input("Введите фамилию и имя: ")
arr = name.split(" ")
arr.reverse()
result = " ".join(arr)
print(result)
