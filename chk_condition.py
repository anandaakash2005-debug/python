a=int(input("Enter first number(a): "))
b=int(input("Enter second number(b): "))
if a<0 or b<0:
    print("only non negative number is allowed")
else:
    s=a+b
    if s>80:
        print("Overflow!!")
    else:
        print("sum",s)