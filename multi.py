# 1st method
def sqrt(num):
    for i in range(1,num):
        x=i*i
        return x
num=int(input("enter the num"))
print(sqrt(num))

#=====================================
# 2nd method
def sqrt(num):
    i=1
    while i<=num:
        print(i*i)
        i=i+1
num=int(input("enter the num"))
sqrt(num)