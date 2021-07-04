# def number(isprime):
#     i=0
#     a=[]
#     while i<len(isprime):
#         j=1
#         count=0
#         while j<=(isprime[i]):
#             if isprime[i]%j==0:
#                 count=count+1
#             j=j+1
#         if count==2:
#             a.append(isprime[i])
#         i=i+1
#     print(a)
# number(isprime=[6,8,9,7,3,5,2,4])              



isprime=[6,8,8,7,3,5,4]
i=0
a=[]
while i<len(isprime):
    j=1
    count=0
    while j<=(isprime[i]):
        if isprime[i]%j==0:
            count=count+1
        j=j+1
    if count==2:
        a.append(isprime[i])
    i=i+1
print(a)
