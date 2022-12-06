# ЗАДАЧА1
#Написать программу для валидации белорусских телефонных номеров. Пользователь должен вводить в консоли номер телефона в международном формате (например: +375297283847),программа должна проверять является ли он валидным, а также определить мобильного операторого и сохранить данные в словарь.
#Правила определения оператора:
#+375 25 xxx xx xx — life:)
#+375 29 1xx xx xx — А1
#+375 29 2xx xx xx — МТС
#+375 29 3xx xx xx — А1
#+375 29 5xx xx xx — МТС
#+375 29 6xx xx xx — А1
#+375 29 7xx xx xx — МТС
#+375 29 8xx xx xx — МТС
#+375 29 9xx xx xx — А1
#+375 33 xxx xx xx — МТС
#+375 44 xxx xx xx — А1
#После каждой попытки спрашивать пользователя о том, хочет ли он проверить ещё один номер или завершить сеанс. 
#При выборе завершения сеанса происходит выход из программы.

#Правила валидности номера:
#1. Строка длиной 13 символов.
#2. Первый символ знак плюс, остальные цифры
#3. Проверить код страны, он должен быть равен 375.
#4. Правильный код хоть одного мобильного оператора.


#Примеры вывода программы:
#1. Если номер НЕ валидный:
#{
#  "success": False,
#  "description": "Причины ошибки"
#}
#2. Если валидный:
#{
#  "success": True,
#  "phone": +375258929929
#  "operator": "life:)",
#}

operator = {'+37525': 'life:)', 
'+375291': 'А1',
'+375292': 'МТС',
'+375293': 'А1',
'+375295': 'МТС',
'+375296': 'А1',
'+375297': 'МТС',
'+375298': 'МТС',
'+375299': 'А1',
'+37533': 'МТС',
'+37544': 'А1'}

while True:
    result = {}
    error = False
    phone = input('Введите номер телефона: ')
    if len(phone) != 13:
        result['success'] = False
        result['description'] = "Phone number should contains only 13 symbols."
        error = True
    if phone[0] not in ('+'):
        result['success'] = False
        result['description'] = "The phone number must contain the first character plus sign"
        error = True
    for char in phone[1:13]:
        if not char.isdigit():
            result['success'] = False
            result['description'] = "Phone number should contains only integers."
            error = True
            break
    if phone[0:3] not in ('+375'):
        result['success'] = False
        result['description'] = "Phone number must be +375"
        error = True
    if error:
        print(result)
    else:
        result['success'] = True
        result['phone'] = phone
        result['operator'] = operator[phone[0:7]]
        
        print(result)
    

    exit_choice = input('Хотите ли вы проверить ещё один номер(Y/N): ')
    if exit_choice == 'N':
        break

