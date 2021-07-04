# 1st method
def number(a):
    i=1
    while i<(a):
        if i%3==0:
            print("nav")
        elif i%7==0:
            print("gurukul")
        elif i%7==0 and i%3==0:
            print("navgurukul")
        else:
            print(i,"savuta")
        i=i+1
n = int(input("enter the number="))
number(n)        


#  2nd method
n = int(input("enter the number="))
i=1
while i<(n):
    if i%3==0:
        print("nav")
    elif i%7==0:
        print("gurukul")
    elif i%7==0 and i%3==0:
        print("navgurukul")
    else:
        print(i,"savita")
    i=i+1
