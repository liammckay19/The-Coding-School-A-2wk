import random

weapons = { "stick": 1, "sword": 5, "whip": 3, "club": 2, "gun": 10 }  # must be outside the class to work


class Player(object):
    
    def __init__(self, health=30, weapon='stick', strength=1, ):
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
        return self.weapon, enemy.health


class Enemy:
    pass

# comments:
# reformat code by going to: Code>Reformat Code
# change line 4 to weapons = {"stick": ... }
# argument names are always lower-case (line 17, line 22) Enemy change to enemy
#
# how to use random:
# random.randInt(0, 5) - returns a random value between 0 and 5
