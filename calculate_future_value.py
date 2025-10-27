p=float(input("Enter principal amount: "))
r=float(input("Enter rate of interest: "))
t=int(input("Enter time(in years): "))

fv=p*(1+r/100)**t
print("Future value: ",round(fv,2))