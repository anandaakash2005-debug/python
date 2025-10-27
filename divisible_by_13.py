#1st Approach

# def divby13(s):
#     num=int(s)

#     return num%13==0

#2nd Approach

# def divby13(s):

#     length=len(s)
#     if length==1 and s[0]=='0':
#         return True
    
#     if length%3==1:
#         s+="00"
#         length+=2

#     elif length%3==2:
#         s+="0"
#         length+=1

#     sum=0
#     p=1

#     i=length-1
#     while i>=0:
#         group=0
#         group+=int(s[i])
#         i-=1
#         group+=int(s[i])*10
#         i-=1
#         group+=int(s[i])*100
#         i-=1

#         sum+=group*p
#         p*=-1

#     sum=abs(sum)
#     return sum%13==0

#3rd Approach

def divby13(s):
    rem=0
    for ch in s:
        rem=(rem*10+int(ch))%13
    
    return rem==0

s="261386147"
if(divby13(s)):
    print("True")

else:
    print("False")