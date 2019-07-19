import random
gameLost = False
weapons = {"stick": 1, "sword": 5, "whip": 3, "club": 2, "gun": 10, "potato":1000000}  # must be outside the class to work
catchChance = 0
turnsTaken = 0
class Player(object):

    def __init__(self, health=30, weapon='stick', strength=5):
        # TODO: add doc-string
        self.health = health
        self.weapon = weapon
        self.strength = strength

    def heal(self):
        self.health = self.health * 1.5 + 5
        return self.health

    def hitEnemy(self, enemy):
        damageDealt = weapons[self.weapon] * self.strength * 2
        enemy.health -= damageDealt
        return enemy.health

    def throwWeapon(self, enemy):
        damageDealt = weapons[self.weapon] * self.strength * 2
        enemy.health -= damageDealt
        self.weapon = "stick"
        return (self.weapon, enemy.health)
    def cripple(self, enemy):
        enemy.health -= self.strength *weapons[self.weapon]
        enemy.damage = enemy.damage * 2 / 3
        return (enemy.health, enemy.damage)
    def run(self,catchChance, gameLost, enemy):
        catchChance+=1
        self.strength = self.strength/2
        enemy.health = 1
        if catchChance == 2:
            gameLost = True
        return (self.strength, gameLost, enemy.health)
ability = {"hit": True, "arrow": False, "cripple": False, "firebreath": False, "heal": False}


class Enemy(object):
    def __init__(self, name = "", health=20, weapon='none', damage=10):
        # TODO: add doc-string
        self.health = health
        self.weapon = weapon
        self.damage = damage
        self.name = name

    def hitplayer(self, player):
        player.health -= self.damage
        return player.health
        print("Enemy hits you for " + str(self.damage) + " damage!")

    def cripple(self, player):
        player.health -= self.damage / 2.5
        player.strength = player.strength * 2 / 3
        return (player.health, player.strength)

        print("Enemy hits you for " + str(self.damage * 2.5) + " damage and cripples you, taking a third of your strength!")

    def arrow(self, player):
        arrowRandom = random.randint(1,3)
        if arrowRandom == 3:
            player.health -= self.damage * 2
            print("Enemy shoots you for " + str(self.damage * 2) + " damage!")
        else:
            player.health -= self.damage * 2 / 3
            print("Enemy shoots you for " + str(self.damage * 2 / 3) + " damage!")
            return player.health

    def firebreath(self, player):
        player.health -= damage * 3
        return player.health
        print("Enemy breaths fire on you for " + str(self.damage * 3) + " damage!")

    def heal(self):
        self.health = self.health + 10 + self.health * 1.5
        print("Enemy heals for " + str(self.health + 10 + self.health * 1.5))
        return self.health
mainCharacter = Player()

def level1Enemy(healthGained, strengthGained):
    x = random.randint(1, 5)
    if (x == 1):
        enemy1 = Enemy("Weak Ogre", 15, "stick", 10)
    elif (x == 2):
        enemy1= Enemy("Angry Dwarf", 10, "stick", 15)
    elif (x == 3):
        enemy1= Enemy("Drunk Guard", 20, "whip", 10)
    elif (x == 4):
        enemy1 = Enemy("Angry Relative", 10, "club", 10)
    else:
        enemy1 = Enemy("Giant Toad", 20, "stick", 8)
    if catchChance >1:
        print("You were caught trying to run and killed!")
    while mainCharacter.health > 0 and enemy1.health > 0 and catchChance <2:
        print("health = " + str(mainCharacter.health))
        print("strength = " + str(mainCharacter.strength))
        print("Enemy Health = " + str(enemy1.health))
        print("A(n) "+ enemy1.name +" is attacking you!")
        print("What's your move?")
        print("Print [heal],[attack],[cripple],[throw weapon], or [run]. If you run more than two times you lose!")
        playerInput = str(input())
        if playerInput == "heal":
            mainCharacter.heal()
        elif playerInput == "attack":
            mainCharacter.hitEnemy(enemy1)
        elif playerInput == "cripple":
            mainCharacter.cripple(enemy1)
        elif playerInput == "throw weapon":
            mainCharacter.throwWeapon(enemy1)
        elif playerInput == "run":
            mainCharacter.run(catchChance,gameLost, enemy1)
        else:
            print("You forfeit your attack!")
        if(enemy1.health <= 0):
            mainCharacter.health = healthGained
            mainCharacter.strength = strengthGained
            print("You won this fight!")
            print("health = " + str(mainCharacter.health))
            print("strength = " + str(mainCharacter.strength))
            print("Keep your weapon or pick up "+ str(enemy1.weapon) + "?")
            print("[Y] or [N]")
            switchWeapon = str(input())
            if switchWeapon == "Y":
                mainCharacter.weapon = enemy1.weapon
            break
        enemy1.hitplayer(mainCharacter)
        if(mainCharacter.health <= 0):
            print("You lose the game!")
            gameLose = True
            break
def level2Enemy(healthGained, strengthGained):
    x = random.randint(1, 5)
    if (x == 1):
        enemy2 = Enemy("Enemy Guard", 70, "sword", 20)
    elif (x == 2):
        enemy2= Enemy("Large Ogre", 100, "club", 15)
    elif (x == 3):
        enemy2= Enemy("Python", 60, "stick", 25)
    elif (x == 4):
        enemy2 = Enemy("Giant Spider", 75, "whip", 20)
    else:
        enemy2 = Enemy("Mega Toad", 80, "club", 20)
    if catchChance >1:
        print("You were caught trying to run and killed!")
    while mainCharacter.health > 0 and enemy2.health > 0 and catchChance <2:
        print("health = " + str(mainCharacter.health))
        print("strength = " + str(mainCharacter.strength))
        print("Enemy Health = " + str(enemy2.health))
        print("A(n) "+ enemy2.name +" is attacking you!")
        print("What's your move?")
        print("Print [heal],[attack],[cripple],[throw weapon], or [run]. If you run more than two times you lose!")
        playerInput = str(input())
        if playerInput == "heal":
            mainCharacter.heal()
        elif playerInput == "attack":
            mainCharacter.hitEnemy(enemy2)
        elif playerInput == "cripple":
            mainCharacter.cripple(enemy2)
        elif playerInput == "throw weapon":
            mainCharacter.throwWeapon(enemy2)
        elif playerInput == "run":
            mainCharacter.run(catchChance,gameLost,enemy2)
        else:
            print("You forfeit your attack!")
        if(enemy2.health <= 0):
            mainCharacter.health = healthGained
            mainCharacter.strength = strengthGained
            print("You won this fight!")
            print("health = " + str(mainCharacter.health))
            print("strength = " + str(mainCharacter.strength))
            print("Keep your weapon or pick up "+ str(enemy2.weapon) + "?")
            print("[Y] or [N]")
            switchWeapon = str(input())
            if switchWeapon == "Y":
                mainCharacter.weapon = enemy2.weapon
            break
        enemyAttack = random.randint(1,2)
        if enemyAttack == 1:
            enemy2.hitplayer(mainCharacter)
        elif enemyAttack == 2:
            enemy2.cripple(mainCharacter)
        if(mainCharacter.health <= 0):
            print("You lose the game!")
            gameLose = True
            break
def level3Enemy(healthGained, strengthGained):
    x = random.randint(1, 3)
    if (x == 1):
        enemy3 = Enemy("Giant", 150, "whip", 40)
    elif (x == 2):
        enemy3= Enemy("Samauri", 100, "sword", 55)
    elif (x == 3):
        enemy3= Enemy("Giant Python", 120, "whip", 60)
    if catchChance >1:
        print("You were caught trying to run and killed!")
    while mainCharacter.health > 0 and enemy3.health > 0 and catchChance <2:
        print("health = " + str(mainCharacter.health))
        print("strength = " + str(mainCharacter.strength))
        print("Enemy Health = " + str(enemy3.health))
        print("A(n) "+ enemy3.name +" is attacking you!")
        print("What's your move?")
        print("Print [heal],[attack],[cripple],[throw weapon], or [run]. If you run more than two times you lose!")
        playerInput = str(input())
        if playerInput == "heal":
            mainCharacter.heal()
        elif playerInput == "attack":
            mainCharacter.hitEnemy(enemy3)
        elif playerInput == "cripple":
            mainCharacter.cripple(enemy3)
        elif playerInput == "throw weapon":
            mainCharacter.throwWeapon(enemy3)
        elif playerInput == "run":
            mainCharacter.run(catchChance,gameLost,enemy3)
        else:
            print("You forfeit your attack!")
        if(enemy3.health <= 0):
            mainCharacter.health = healthGained
            mainCharacter.strength = strengthGained
            print("You won this fight!")
            print("health = " + str(mainCharacter.health))
            print("strength = " + str(mainCharacter.strength))
            print("Keep your weapon or pick up "+ str(enemy3.weapon) + "?")
            print("[Y] or [N]")
            switchWeapon = str(input())
            if switchWeapon == "Y":
                mainCharacter.weapon = enemy3.weapon
            break
        enemyAttack = random.randint(1,3)
        if enemyAttack == 1:
            enemy3.hitplayer(mainCharacter)
        elif enemyAttack == 2:
            enemy3.cripple(mainCharacter)
        else:
            enemy3.heal()
        if(mainCharacter.health <= 0):
            print("You lose the game!")
            gameLose = True
            break
def level4Enemy(healthGained, strengthGained):
    x = random.randint(1, 2)
    if (x == 1):
        enemy4 = Enemy("Rifleman", 130, "gun", 80)
    elif (x == 2):
        enemy4= Enemy("Dragon", 160, "gun", 80)
    if catchChance > 1:
        print("You were caught trying to run and killed!")
    while mainCharacter.health > 0 and enemy4.health > 0 and catchChance <2:
        print("health = " + str(mainCharacter.health))
        print("strength = " + str(mainCharacter.strength))
        print("Enemy Health = " + str(enemy4.health))
        print("A(n) "+ enemy4.name +" is attacking you!")
        print("What's your move?")
        print("Print [heal],[attack],[cripple],[throw weapon], or [run]. If you run more than two times you lose!")
        playerInput = str(input())
        if playerInput == "heal":
            mainCharacter.heal()
        elif playerInput == "attack":
            mainCharacter.hitEnemy(enemy4)
        elif playerInput == "cripple":
            mainCharacter.cripple(enemy4)
        elif playerInput == "throw weapon":
            mainCharacter.throwWeapon(enemy4)
        elif playerInput == "run":
            mainCharacter.run(catchChance,gameLost,enemy4)
        else:
            print("You forfeit your attack!")
        if(enemy4.health <= 0):
            mainCharacter.health = healthGained
            mainCharacter.strength = strengthGained
            print("You won this fight!")
            print("health = " + str(mainCharacter.health))
            print("strength = " + str(mainCharacter.strength))
            print("Keep your weapon or pick up "+ str(enemy4.weapon) + "?")
            print("[Y] or [N]")
            switchWeapon = str(input())
            if switchWeapon == "Y":
                mainCharacter.weapon = enemy4.weapon
            break
        enemyAttack = random.randint(1,4)
        if enemyAttack == 1:
            enemy4.hitplayer(mainCharacter)
        elif enemyAttack == 2:
            enemy4.cripple(mainCharacter)
        elif enemyAttach == 3:
            enemy4.heal()
        elif enemyAttach == 4:
            if enemy4.name == "Dragon":
                enemy4.firebreath(mainCharacter)
            else:
                enemy4.arrow(mainCharacter)
        if(mainCharacter.health <= 0):
            print("You lose the game!")
            gameLose = True
            break


def level5Enemy(healthGained, strengthGained):
    print("Final Fight!")
    enemy5 = Enemy("Diablo", 1000, "potato", 100)
    if catchChance >1:
        print("You were caught trying to run and killed!")
    while mainCharacter.health > 0 and enemy5.health > 0 and catchChance <2:
        print("health = " + str(mainCharacter.health))
        print("strength = " + str(mainCharacter.strength))
        print("Enemy Health = " + str(enemy5.health))
        print("A(n) "+ enemy5.name +" is attacking you!")
        print("What's your move?")
        print("Print [heal],[attack],[cripple],or [throw weapon].")
        playerInput = str(input())
        if playerInput == "heal":
            mainCharacter.heal()
        elif playerInput == "attack":
            mainCharacter.hitEnemy(enemy5)
        elif playerInput == "cripple":
            mainCharacter.cripple(enemy5)
        elif playerInput == "throw weapon":
            mainCharacter.throwWeapon(enemy5)
        else:
            print("You forfeit your attack!")
        if(enemy5.health <= 0):
            mainCharacter.health = healthGained
            mainCharacter.strength = strengthGained
            print("You won this fight!")
            print("health = " + str(mainCharacter.health))
            print("strength = " + str(mainCharacter.strength))
            print("Enemy Health = " +str(enemy5.health))
            print("Keep your weapon or pick up "+ str(enemy5.weapon) + "?")
            print("[Y] or [N]")
            switchWeapon = str(input())
            if switchWeapon == "Y":
                mainCharacter.weapon = enemy5.weapon
            print("You won! Congradulations!")
            break
        enemyAttack = random.randint(1,5)
        if enemyAttack == 1:
            enemy5.hitplayer(mainCharacter)
        elif enemyAttack == 2:
            enemy5.cripple(mainCharacter)
        elif enemyAttach == 3:
            enemy5.heal()
        elif enemyAttach == 4:
            enemy5.firebreath(mainCharacter)
        else:
            enemy5.arrow(mainCharacter)
        if(mainCharacter.health <= 0):
            print("You lose the game!")
            gameLose = True
            break




def main():
    print("Hello young traveler. You have come to this land to rid us of these evil invaders!")
    print("These are dark times. To rid us of these invaders, you will have to fight them.")
    print("There will be many enemies along the way. Be prepared, as the tools you have are these:")
    print("Your health is represents how many attacks you can sustain until you die.")
    print("Keep this above zero at all costs.")
    print("Your weapon shows how much damage you will deal. Enemies may drop weapons once you kill them!")
    print("Your strength is your damage multiplier. The higher that is, the more damage you will do.")
    print("Begin your quest!")
    level1Enemy(40,10)
    if gameLost == False:
        level1Enemy(50,12)
        if gameLost == False:
            level2Enemy(70,15)
            if gameLost == False:
                level2Enemy(80, 17)
                if gameLost == False:
                    level3Enemy(100,20)
                    if gameLost == False:
                        level3Enemy(140,22)
                        if gameLost == False:
                            level4Enemy(170,25)
                            if gameLost == False:
                                level4Enemy(450,30)
                                if gameLost == False:
                                    level5Enemy(1000000,1000000)
    print("Game Over!")

if __name__ == '__main__':
    main()