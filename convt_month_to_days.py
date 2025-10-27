month=input("Enter month name: ")
if month in("January","March","May","July","August","October","December"):
    print("31 days")
elif month in("April","June","September","November"):
    print("30 days")
elif month in("February"):
    print("28 or 29 days")
else:
    print("Invalid Month name")