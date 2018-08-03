def comp(a,b,c):
     if a>b and a>c :
          return a
     elif b>a and b>c :
          return b
     else :
          return c
a=input("enter the first no:")
b=input("enter the sec no:")
c=input("enter the third no:")
d=comp(a,b,c)
print("largest no:",d)
