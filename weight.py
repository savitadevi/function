def calculates (weight,hight):
    bmi=weight/hight
    if bmi<=18.5:
        return "underweight"
    if bmi <=25.0:
        return"normal"
    if bmi<=30.0:
        return"overweight"
    if bmi>30:
        return"obese"
    return bmi
weight =int(input("enter the weight"))
height=int(input("enter the hight"))
print(calculates (weight,height))                    

