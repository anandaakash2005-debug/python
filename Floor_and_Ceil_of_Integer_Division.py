#1st methode
# def calfloor(a,b):
#     return a//b

# def calceil(a,b):
#     return -(-a//b)

#2nd methode
import math

def divceilfloor(a,b):

    floor_val=math.floor(a/b)

    ceil_val=math.ceil(a/b)

    return [floor_val,ceil_val]

a,b=-7,2

res=divceilfloor(a,b)

print("ceil=",res[1])
print("Floor=",res[0])