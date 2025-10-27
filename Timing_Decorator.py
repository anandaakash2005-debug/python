import time

def timer(func):
    def rapper(*arg,**kwarg):
        start_time=time.time()
        print(f"{func.__name__} started")
        result=func(*arg,**kwarg)
        end_time=time.time()
        print(f"finished {func.__name__} in {end_time - start_time:.4f} seconds")
        return result
    return rapper

class operation:
    @timer
    def factorial(self,n):
        result=1
        for i in range(1,n+1):
            result*=i
        return result
    
    @timer
    def power(sef,x,y):
        return x**y
    
op=operation()
print(op.factorial(20))
print(op.power(2,10))