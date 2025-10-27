def decfun(f):
    def inner_fun():
        print("welcome")
    f()
    return inner_fun

@decfun
def fun():
    print("user")
#fun=decfun(fun)


fun()