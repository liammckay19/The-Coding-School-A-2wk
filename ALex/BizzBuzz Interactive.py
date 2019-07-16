print("Bizz?")
j = int(input())
print("Buzz?")
k = int(input())
x = 1
u = 0
playerTurn = 1
print("How many players?")
playerNumber=int(input())

print("Answers: x,Bizz,Buzz,BizzBuzz")
alive = {i:True for i in range(playerNumber)}


def beginPlayerTurn(PlayerTurn):
    if alive(playerTurn) == True:
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
            if int(n) == x:
                print("correct!")
                if playerNumber!=PlayerTurn:
                    PlayerTurn+=1
                else:
                    PlayerTurn = 1
                    x += 1
            else:
                print("Wrong. SMH")
                print("Player " + PlayerTurn + " is out!")
                alive
                if playerNumber!=PlayerTurn:
                    alive[PlayerTurn] = False
                    PlayerTurn+=1
                else:
                    alive[PlayerTurn] = False
                    PlayerTurn = 1
        if u == 2:
            if str(n) == "Bizz":
                print("correct!")
                if playerNumber!=PlayerTurn:
                    PlayerTurn+=1
                else:
                    PlayerTurn = 1
                    x += 1
            else:
                print("Wrong. SMH")
                print("Player " + PlayerTurn + " is out!")
                if playerNumber!=PlayerTurn:
                    alive[PlayerTurn] = False
                    PlayerTurn+=1
                else:
                    alive[PlayerTurn] = False
                    PlayerTurn = 1

        if u == 3:
            if str(n) == "Buzz":
                print("correct!")
                x += 1
                Player1Turn = 2
            else:
                print("Wrong. SMH")
                print("Player " + PlayerTurn + " is out!")
                if playerNumber!=PlayerTurn:
                    alive[PlayerTurn] = False
                    PlayerTurn+=1
                else:
                    alive[PlayerTurn] = False
                    PlayerTurn = 1

        if u == 4:
            if str(n) == "BizzBuzz":
                print("correct!")
                x += 1
                Player1Turn = 2
            else:
                print("Wrong. SMH")
                print("Player " + PlayerTurn + " is out!")
                if playerNumber!=PlayerTurn:
                    alive[PlayerTurn] = False
                    PlayerTurn+=1
                else:
                    alive[PlayerTurn] = False
                    PlayerTurn = 1
while x<=100:
    beginPlayerTurn(playerTurn)
