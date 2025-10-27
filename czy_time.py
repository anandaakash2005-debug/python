def decfun(func):
    def intro(*arg,**kwarg):
        print("introduce yourself")
        return func(*arg,**kwarg)
    return intro


class office:
    @decfun
    def fun(self):
        print("Hello")

    @decfun
    def div(self,a,b):
        return a//b
        

off=office()
off.fun()
print(off.div(10,4))