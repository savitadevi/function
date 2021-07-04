def calculator(a,b,symbol):
    if symbol =="-":
        print(a-b)
    elif symbol=="+":
        print(a+b)
    elif symbol=="*":
        print(a*b)
    elif symbol=="/":
        print(a/b)
calculator(a=int(input("enter your number")),b=int(input("enter your number")),symbol=(input("enter your symbol")) )

