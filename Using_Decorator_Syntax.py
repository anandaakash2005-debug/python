def dec_func(func):
    def inner_func(*arg,**kwarg):
        print("give intro")
        return func(*arg,**kwarg)
    return inner_func

class senior:
    @dec_func
    def intro(self):
        print("Good morning")

S=senior()
S.intro()