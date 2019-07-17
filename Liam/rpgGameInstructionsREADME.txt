
Summer 2019 July 3rd

Requirements:
    - make a condition to exit the game when the player or enemy has HP <= 0
    - Clean output styling (shown below)
    - random.randint() must be used to deal damage to the player/enemy

- Enemy class
    attributes:
        hp
        moveSet
        baseDamage (add this to damage dealt when attacking)
    methods:
        attack()
        getHP()

- Player class
    attributes:
        hp
        moveSet
        baseDamage
    methods:
        attack() commented - what this method does, how its going to work
        getHP() commented - what this method does, how its going to work

Only these classes alone will be enough to organize the game,
but you will need to execute this game in main()

be creative!
    ideas:
    add more methods than the ones I have shown here!
        what would a defend() method do?
    add more attributes than the ones I have shown here!
        what would a defense attribute mean when dealing damage?
    use random.randint(0, x)
        to change about enemy name, name of attacks, and deal different amounts of damage

Example output:




=====================================
An ogre is attacking!
Player HP: 100
Ogre HP: 20
What do you do?
------- ATTACKS --------------- SPELLS --------
> Fire Blast            > Spell1
> Sword Slash           > Spell2
> Double Kick           > Spell3
> Shield Bash           > Spell4
-----------------------------------------------
> Fire Blast




=====================================
You fire a ball of flaming magma that burns into the ogre!
Deals 5 damage!
The ogre hurls its club at you!
Deals 10 damage!




=====================================
An ogre is attacking!
Player HP: 90
Ogre HP: 15
What do you do?
------- ATTACKS --------
> Fire Blast
> Sword Slash
> Double Kick
> Shield Bash
------------------------
