def perfect_number(a):
    sum=0
    i=1
    while i<a:
        if a%i==0:
            sum=sum+i
        i=i+1
    if sum==a:
        print("perfect")
    else:
        print("not perfect")      

perfect_number(int(input("enter your number")))                
