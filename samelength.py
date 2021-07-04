def name (a,b):
   c=len(a)
   d=len(b)
   if c==d:
       print(a,"\n",b)
   elif c>d:
       print(a)
   else:
       print(b)
name(a=(input("enter your name ")),b=(input("enter your input")))              