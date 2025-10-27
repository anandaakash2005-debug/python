def func1():
    print("inside function 1")

def func2(f):
    print("inside function 2")
    f()

f=func1
f()
func2(f)