a=float(input("Enter 1st number: "))
b=float(input("Enter 2nd number: "))
c=float(input("Enter 2nd number: "))

if(a>b):
    if(a>c):
        print(a," is greatest")
    else:
        print(b," is greatest")
elif(b>a):
    if(b>c):
        print(b," is greatest")
    else:
        print(c," is greatest")
