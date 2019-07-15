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
    print("Divisible by neither")
elif y == y1 and z != z1:
    print("Divisible by Bizz only")
elif y != y1 and z == z1:
    print("Divisible by Buzz only")
else:
    print("Divisible by neither")
