def log_method_call(func):
    def wrapper(*args,**kwargs):
        print(f"calling method: {func.__name__}")
        result=func(*args,**kwargs)
        print(f"Finished method: {func.__name__}")
        return result
    return wrapper

class calculator:
    @log_method_call
    def add(self,a,b):
        return a+b
    
    @log_method_call
    def multiply(self,a,b):
        return a+b
    
calc=calculator()
print(calc.add(3,5))
print(calc.multiply(4,6))