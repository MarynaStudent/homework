#Написать функцию, которая принимает список состоящий из строк и возвращает текст составленный из этих строк
#def get_text(['Hello', 'world']):
    # тут написать код

#print(get_text) # напечатает 'Hello world' одной строкой

#После этого написать декоратор text_up, который должен переводить то, что
#возвращает фукнция в верхний регистр
#@text_up
#def get_text(['Hello', 'world']):
 #   ...

#print(get_text) # напечатает 'HELLO WORLD' одной строкой



def text_up(func):
    def wrap(*args):
        args = list(args)
        for i, v in enumerate(args):
            args[i] = v.upper()
        res = func(*args)
        return res
    return wrap
@text_up
def get_text(*args):
    return ' '.join(args)
print(get_text('Hello', 'world'))



