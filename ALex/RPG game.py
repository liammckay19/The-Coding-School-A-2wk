import random

class Player(object):
    weapons : {"stick":1,"sword":5,"whip":3,"club":2,"gun":10}
    def __init__(self, health=30, weapon='stick', strength=1, ):
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
class Enemy
