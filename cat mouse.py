def cat_mouse(cat_a,cat_b,mouse_c):
    if cat_b==0:
        return("cat_a")
    a=cat_a-mouse_c
    b=cat_b-mouse_c
    if a<0:
        a=a*-1
    if b<0:
        b=b*-1
    if a==b:
        return("mouse_c")
    elif a>b:
        return("cat_b")
    else:
        return("cat_a")
print(cat_mouse(1,2,3))

