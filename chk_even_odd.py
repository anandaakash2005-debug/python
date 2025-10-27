#1st process
# def chkeven(n):
#     remainder=n%2
#     if(remainder==0):
#         return True
#     else:
#         return False

#2nd process
def chkeven(n):
    if (n&1) == 0:
        return True
    else:
        return False
    
n=9
if chkeven(n):
    print("Even")

else:
    print("Odd")