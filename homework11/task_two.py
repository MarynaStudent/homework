#В задаче с декоратором (задание номер 8) переписать его в class-based стиле.
class text_up:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        args = list(args)
        for i, v in enumerate(args):
            args[i] = v.upper()
        res = self.func(*args)
        return res
@text_up
def get_text(*args):
    return ' '.join(args)
print(get_text('Hello', 'world'))

