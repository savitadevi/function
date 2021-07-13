a=["savita"]
str1=""
i=0
while i<len (a):
    j=0
    while j<len(a[i]):
        str1=str1+str(a[i][j]+" ")
        j=j+1
    i=i+1
print(str1)        
