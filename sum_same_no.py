# a=[[5,7,9,8],[7,8,9,5]]
# def sum(a):
#  k=0
#  while k<len(a):
#     i=0
#     while i<len(a[k]):
#         j=0
#         while j<len(a[k+1]):
#             if a[k][i]==a[k+1][j]:
#                 sum=a[k][i]+a[k+1][j] 
#                 print(sum)
#             j=j+1
#         i=i+1 
#     break
#     k+=1
# sum(a=[[5,7,9,8],[7,8,9,5]]) 

# ===========seciond method===================
def sum(a):
    i=0
    while i<len(a):
        j=0
        sum=0
        while a[i]>0:
            d=a[i]%10
            a[i]=a[i]//10
            sum=sum+d
        j=j+1
        i=i+1    
        
        print(sum)
sum([123,4567])            







         






      



         
