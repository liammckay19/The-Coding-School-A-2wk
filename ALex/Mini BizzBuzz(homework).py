print("Bizz?")
j = int(input())
print("Buzz?")
k = int(input())
x = 1
u = 0
Player1Turn = True
print("Input a number already!")
print("*whispers* What a loser.")
x=int(input())
if Player1Turn == True:
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

