print("Bizz?")
j = int(input())
print("Buzz?")
k = int(input())
x = 1
u = 0
print("INPUT A NUMBER ALREADY!")
print("*whispers* (What a loser)")
x=int(input())
y = x / j
y1 = round(y, 0)
z = x / k
z1 = round(z, 0)
if y != y1 and z != z1:
    u = 1
elif y == y1 and z != z1:
    u = 2
elif y != y1 and z == z1:
    u = 3
else:
    u = 4
if u==1:
    print("Divisible by neither")
if u==2:
    print("Divisible by Bizz only")
if u==3:
    print("Divisible by Buzz only")
if u==4:
    print("Divisible by Bizz and Buzz")