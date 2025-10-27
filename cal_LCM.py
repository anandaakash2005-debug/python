#1st Approach

# def lcm(a,b):
#     g=max(a,b)
#     s=min(a,b)
#     for i in range(g,a*b+1,g):
#         if i%s==0:
#             return i
#     return a*b

#2nd Approach

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return (a//gcd(a,b))*b

a,b=10,9
print(lcm(a,b))