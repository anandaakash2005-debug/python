# 1st Methode

# def gcd(a,b):
#     result=min(a,b)
#     while result >0:
#         if a%result==0 and b%result==0:
#             break
#         result-=1
#     return result

# 2nd Methode

# def gcd(a,b):
#     if a==0:
#         return b
#     if b==0:
#         return a
#     if a==b:
#         return a
#     if a>b:
#         return gcd(a-b,b)
    
#     return gcd(a,b-a)

# 3rd Approach
# def gcd(a, b):
#     # Everything divides 0
#     if a == 0:
#         return b
#     if b == 0:
#         return a

#     # Base case
#     if a == b:
#         return a

#     # a is greater
#     if a > b:
#         if a % b == 0:
#             return b
#         return gcd(a - b, b)

#     # b is greater
#     if b % a == 0:
#         return a
#     return gcd(a, b - a)

#4th Approach
def gcd(a,b):
    if b==0:
        return a
    return (b,a%b)

a=20
b=28
print(gcd(a,b))