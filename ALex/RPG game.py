import random

class Player(object):
    weapons : {"stick":1,"sword":5,"whip":3,"club":2,"gun":10}
    def __init__(self, health=30, weapon='stick', strength=1):
        # TODO: add doc-string
        self.health = health
        self.weapon = weapon
        self.strength = strength
    def heal(self):
        self.health = self.health*1.5 +5
        return self.health
    def hitEnemy(self, Enemy):
        damageDealt=weapons[self.weapon]*self.strength*2
        Enemy.health-=damageDealt
        return Enemy.health
    def throwWeapon(self,Enemy):
        damageDealt=weapons[self.weapon]*self.strength*2
        Enemy.health-=damageDealt
        self.weapon = "stick"
        return self.weapon,Enemy.health
class Enemy(object):
    ability: {"hit":True,"arrow":False,"cripple":False,"firebreath":False, "heal":False}
    def __init__(self, health=20, weapon='none', damage=10):
        # TODO: add doc-string
        self.health = health
        self.weapon = weapon
        self.damage = strength
    def hitPlayer(self,Player):
        Player.health -= self.damage
        return Player.health
        print("Enemy hits you for "+str(self.damage) + " damage!")
    def cripple(self,Player):
        Player.health -= self.damage/2.5
        Player.strength = Player.strength*2/3
        return Player.health, Player.strength

        print("Enemy hits you for " + str(self.damage*2.5) + " damage and cripples you, taking a third of your strength!")

    def arrow(self, Player):
        arrowRandom=random(.5,3.4999)
        arrowRoundRandom=round(arrowRandom,0)
        if arrowRoundRandom ==3
            Player.health-=self.damage*2
            print("Enemy shoots you for " str(self.damage*2) + " damage!")
        else
            Player.health-=self.damage*2/3
            print("Enemy shoots you for " str(self.damage*2/3) + " damage!")
        return Player.health
    def firebreath(self,Player):
        player.health-=damage*3
        return Player.health
        print("Enemy breaths fire on you for "+ str(self.damage * 3) + " damage!")
        def heal(self):
        self.health = self.health+10+self.health*1.5
        print("Enemy heals for "+str(self.health+10 + self.health*1.5))
        return self.health
def main():
    mainCharacter = Player()