def odd_num():
    sum=0
    i=1
    while i<=10:
        if i%3==0 or i%5==0:
            sum+=i
        i+=1
    print(sum)
odd_num()
