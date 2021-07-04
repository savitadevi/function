def add(a,b):
    return(a+b)
def multiply(a,b):
    return(a*b)
def sub(a,b):
    return(a-b)
def div(a,b):
    return(a/b)
def main(a,b,symbol):
    a=int(input("enter your number"))
    b=int(input("enter your number"))
    symbol=(input("enter your symbol"))
    if symbol=="+":
        print(add(a,b))
    elif symbol=="-":
        print(sub(a,b))
    elif symbol=="*":
        print(multiply(a,b))
    elif symbol=="/":
        print(div) 
main(3,4,"*")