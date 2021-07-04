def function(a):
    i=1
    c=[]
    while i<=a:
        b=i*i
        c.append(i)
        c.append(b)
        i=i+1
    print(c)    
function(a=int(input("enter your number")))        