print("Bizz?")
j = int(input())
print("Buzz?")
k = int(input())
x = 1
u = 0
Player1Turn = True
print("Answers: x,Bizz,Buzz,BizzBuzz")
while x <= 100:
    if Player1Turn == True:
        n = input()
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
            if int(n) == x:
                print("correct!")
                Player1Turn = False
                x+=1
            else:
                print("Wrong. SMH")
                print("Player 2 Wins!")
                break
        if u==2:
            if str(n) == "Bizz":
                print("correct!")
                Player1Turn = False
                x+=1
            else:
                print("Wrong. SMH")
                print("Player 2 Wins!")
                break
        if u==3:
            if str(n) == "Buzz":
                print("correct!")
                x+=1
                Player1Turn = False
            else:
                print("Wrong. SMH")
                print("Player 2 Wins!")
                break
        if u==4:
            if str(n) == "BizzBuzz":
                print("correct!")
                x+=1
                Player1Turn = False
            else:
                print("Wrong. SMH")
                print("Player 2 Wins!")
                break
    if Player1Turn == False:
        n = input()
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
            if int(n) == x:
                print("correct!")
                x+=1
                Player1Turn = True
            else:
                print("Wrong. SMH")
                print("Player 1 Wins!")
                break
        if u==2:
            if str(n) == "Bizz":
                print("correct!")
                x+=1
                Player1Turn = True
            else:
                print("Wrong. SMH")
                print("Player 1 Wins!")
                break
        if u==3:
            if str(n) == "Buzz":
                print("correct!")
                x+=1
                Player1Turn = True
            else:
                print("Wrong. SMH")
                print("Player 1 Wins!")
                break
        if u==4:
            if str(n) == "BizzBuzz":
                print("correct!")
                x+=1
                Player1Turn = True
            else:
                print("Wrong. SMH")
                print("Player 1 Wins!")
                break
