print("Rules:")
print("Bizz?")
j = int(input())
print("Buzz?")
k = int(input())
x = 1
u = 0
playerTurn = 1
print("How many players?")
playerNumber=int(input())
l=1
print("Answers: x,Bizz,Buzz,BizzBuzz")
alive = {i:True for i in range(playerNumber+1)}


while x<100:
    if l!=playerNumber:
        if playerTurn >playerNumber:
            playerTurn = 1
        if alive[int(playerTurn)] ==True:
            l=1
            print("player "+ str(int(playerTurn))+":")
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
            if u == 1:
                if str(n) == str(x):
                    print("correct!")
                    if playerNumber!=playerTurn:
                        playerTurn+=1
                    else:
                        playerTurn = 1
                else:
                    print("Wrong. SMH")
                    print("Player " + str(int(playerTurn)) + " is out!")
                    if playerNumber!=playerTurn:
                        alive[playerTurn] = False
                        playerTurn+=1
                    else:
                        alive[playerTurn] = False
                        playerTurn = 1
                x += 1
                print("Next person's turn")

            if u == 2:
                if str(n) == "Bizz":
                    print("correct!")
                    if playerNumber!=playerTurn:
                        playerTurn+=1
                    else:
                        playerTurn = 1
                else:
                    print("Wrong. SMH")
                    print("Player " + str(int(playerTurn)) + " is out!")
                    if playerNumber!= playerTurn:
                        alive[playerTurn] = False
                        playerTurn+=1
                    else:
                        alive[playerTurn] = False
                        playerTurn = 1
                x+=1
                print("Next person's turn")

            if u == 3:
                if str(n) == "Buzz":
                    print("correct!")
                    if playerNumber!=playerTurn:
                        playerTurn+=1
                    else:
                        PlayerTurn = 1
                else:
                    print("Wrong. SMH")
                    print("Player " + str(int(playerTurn)) + " is out!")
                    if playerNumber!=playerTurn:
                        alive[playerTurn] = False
                        playerTurn+=1
                    else:
                        alive[playerTurn] = False
                        playerTurn = 1
                x += 1
                print("Next person's turn")
            if u == 4:
                if str(n) == "BizzBuzz":
                    print("correct!")
                    if playerNumber!=playerTurn:
                        playerTurn+=1
                    else:
                        playerTurn = 1
                else:
                    print("Wrong. SMH")
                    print("Player " + str(int(playerTurn)) + " is out!")
                    if playerNumber!=playerTurn:
                        alive[playerTurn] = False
                        playerTurn+=1
                    else:
                        alive[playerTurn] = False
                        playerTurn = 1
                x+=1
                print("Next person's turn")
        else:
            if playerTurn != playerNumber+1:
                playerTurn+=1
            else:
                playerTurn = 1
            l+=1
    else:
        if playerTurn<=playerNumber:
            print("Player" + str(int(playerTurn)) + " wins!")
            break
        else:
            print("No one wins!")
            break