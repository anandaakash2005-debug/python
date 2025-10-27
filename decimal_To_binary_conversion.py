#1st process
# def decTobin(n):
#     bin_arr=[]
#     while(n>0):
#         bit=n%2
#         bin_arr.append(str(bit))
#         n//=2

#         bin_arr.reverse()
#         return"".join(bin_arr)

#2nd process
# def decTobinaryrec(n,binarr):
#     if n == 0:
#         return 
    
#     decTobinaryrec(n//2,binarr)

#     binarr.append(str(n%2))

# def decTobinary(n):
#     if n==0:
#         return "0"
    
#     binarr=[]
#     decTobinaryrec(n,binarr)
#     return "".join(binarr)

#3rd process
# def decTobinary(n):
#     bin=""
#     while n>0:
#         bit=n&1
#         bin+=str(bit)
#         n=n>>1
    
#     return bin[::-1]

#4th process
import math

def decTobinary(n):
    return bin(n)[2::]
    
n=5
print(decTobinary(n))