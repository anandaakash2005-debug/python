def calpowexp(x,n):
    res=1
    while n>=1:
        if n%2==1:
            res=res*x
            n-=1

        else:
            x*=x
            n//=2

    return res

x,n=3,15
print(calpowexp(x,n))