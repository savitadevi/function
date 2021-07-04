# sum of number
def add_number(num1,num2):
    a=num1+num2
    print(a)
add_number(56,12)



# list a sum of number
def add_number_list(a,b):
    i=0
    sum=0
    c=[]
    while i<len(a):
        sum=a[i]+b[i]
        c.append(sum)
        i=i+1
    print(c)       
add_number_list([50,60,10],[10,20,13])    
