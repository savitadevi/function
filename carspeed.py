# function ques no. 7(speed)
def driver(speed):
    if speed <=70:
        print("it is ok")
    else:
        speed1= (speed-70)//5
        if speed1 > 12:
            print("licens suspend")
        else:
            print(speed1,"point")
speed=int(input("enter the number"))
driver(speed)
