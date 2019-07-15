def even(x):
    z=x/2
    y=round(z,0)
    if z==y:
        return True
    else:
        return False
a=1
while a<=10:
    print(even(a))
    a+=1
