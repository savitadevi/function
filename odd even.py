# def check_numbers(user1,user2):
    
#     if user1%2==0 and user2%2==0:
#         print(" dono even hai")
#     else:
#         print("dono even nahin hain")
# check_numbers(user1=int(input("enter the num")),user2=int(input("enter the num")))

#============================
def check_number_list(a,b):
    i=0
    while i<len(a):
        if a[i]%2==0 and b[i]%2==0:
            print("dono even hai")
        else:
            print("dono even nahi hain ")
        i=i+1
check_number_list([2,6,18,10,3,75],[6,19,24,12,3,87])    
