import random
# TODO: spells dictionary with damage/healing/item enchanting modifier

weaponsDictionary = { "hands": {
    "default":0,
    "enchanted":1
}, "sword": {"default":4, "enchanted":6} }  # extra damage
hidingSpots = { "boulder":4, "tree":3, "small bush":2, "blade of grass":1}  # value is hiding spot effectiveness

class Player(object):
    def __init__(self, health=100, armorArgument=0, level=0, weapon='hands', stealth=0):
        # TODO: add doc-string
        self.health = health
        self.armor = armorArgument
        self.weapon = weapon
        self.damageModifier = 1.0
        self.level = level
        self.weaponIsEnchanted = False
        self.stealth = stealth
        self.spellList = ["Heal","Enchantment","Damage","Boost"]
    
    # attack (special attack, with a sword)
    # kick (physical attack)
    # run (away?)
    # hide
    # spell (can do more than just attack the enemy)

    # read-only methods
    # we are getting an attribute (read-only)
    def getHealth(self):
        # TODO: add doc-string
        return self.health
    
    def getArmor(self):
        # TODO: add doc-string
        return self.armor
    
    def getWeapon(self):
        # TODO: add doc-string
        return self.weapon
    
    def getDamageModifer(self):
        # TODO: add doc-string
        return self.damageModifier
    
    def getLevel(self):
        # TODO: add doc-string
        return self.level

    def attack(self, otherEntity):
        # TODO: add doc-string
        if self.weaponIsEnchanted:
            attackDamage = (1 + weaponsDictionary[self.getWeapon()]['enchanted']) * self.damageModifier
        else:
            attackDamage = (1 + weaponsDictionary[self.getWeapon()]['default']) * self.damageModifier

        otherEntity.health -= attackDamage

        return attackDamage
    
    def kick(self, otherEntity):
        # TODO: add doc-string
        attackDamage = 1 * self.damageModifier
        otherEntity.health -= attackDamage
        return attackDamage
    
    def run(self):
        # TODO: add random events

        randomGeneratorInteger = random.randint(0, 3)
        # TODO: make if logic and print running actions
        if randomGeneratorInteger == 0:
            print("While attempting to run away, the Ogre grabs you back into the arena!")
        elif randomGeneratorInteger == 1:
            print("You run into a tree while attempting to run. -5 HP")
            self.health -= 5
        elif randomGeneratorInteger == 2:
            print("You trip while running away, and fall on a rock. -10 HP")
            self.health -= 10
        return

    def hide(self):
        # TODO: add doc-string
        # Possible hiding spots (random hiding number): (the lower a random number, the worse the spot)
        #       boulder, tree, a small bush, a blade of grass
        # chance ogre attacking = new random number
        # hiding random number (between 0 and self.stealth?)
        # possibilityforamiss = chance ogre attacking * hiding random number*hiding spot effectiveness
        randomHidingNumber = random.randint(0, 4)
        print("You hid behind a {0}.".format(hidingSpots[randomHidingNumber]))
        # possibilityforamiss = 20 * randomHidingNumber *
        pass
    # ogre who is about to attack
        # player who is hiding
        # if there is a random number greater than possibilityforamiss, then the ogre misses
        # the higher the number of possibilityforamiss, then the higher the chance of the ogre missing.
        # TODO: program this algorithm for hiding
        
    def spell(self):
        # TODO: add doc-string
        # Come up with names for these spells to print to the player, save them in spellList attribute
        # damage spell
        # healing spell
        # boost attack (boost damage modifier for One turn) cast on self - change damage modifier
        # enchant weapon (boost damage for your weapon)
        # TODO: enchant weapon code goes here:
        pass
        

class Enemy(object):
    # these methods are very similar to the Player
    # TODO: __init__ method
    # TODO: attack method
    # TODO: run method
    # TODO: hide method
    # TODO: shout/taunt method
    
    pass


def main():
    # TODO: Do 1 - 3 (4, 5 if you have time)
    # game application method
    #   1. run the game while the player health or enemy health is greater than 0
    #   2. get user input
    #   3. print stuff to screen
    #   4. make the player do what the user said
    #   5. make the ogre respond/attack/defend/run/hide
    
    playerOne = Player(health=10, level=1)
    Ogre = Enemy()
    # if "attack" in userInput:
    playerOne.attack(Ogre)


if __name__ == '__main__':
    main()
