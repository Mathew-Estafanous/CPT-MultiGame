import random
#Pokemon Statistics
name = "Charmander"
health = 110
type = 1 #fire
damageRate = 15
energy = 100
defendShield = 0

def findAbility(choosen, pokType):
    if choosen == 1:
        damage = ember()
    elif choosen == 2:
        damage = blaze()
    elif choosen == 3:
        return flamecharge()
    else:
        return rechargeEnergy()
    damage -= checkifBetter(pokType)
    return damage

def ember():
    global energy, energyUse
    energy -= energyUse[1]
    damage = damageRate
    if random.randint(1,50) <= 10:
        critical = random.randint(15,25)
        damage += critical
        print("Critical Hit! +", critical, "damage!")
    return damage

def blaze():
    global energy, energyUse
    energy -= energyUse[2]
    damage = damageRate
    if random.randint(1,400) <= 59:
        critical = random.randint(25,35)
        damage += critical
        print("Critical Hit! +", critical, "damage!")
    return damage

def flamecharge():
    global defendShield
    global energy, energyUse
    energy -= energyUse[3]
    defendShield = random.randint(10,15)
    print("Flame Shield Surrounds,", name, "protecting him from:", defendShield, "damage.")
    return False

def rechargeEnergy():
    global energy
    chargeAmount = random.randint(40, 100)
    if chargeAmount + energy <= 100:
        energy += chargeAmount
        print(name, "Now has", energy, "Energy")
    else:
        print(name, "Is back at 100 Energy")
        energy = 100
    return False

def takeDamage(dmg):
    global defendShield, health, name
    if defendShield > 0:
        if defendShield >= dmg:
            defendShield = 0
            print(name,"had a shield and did not take any damage.")
            return health
        else:
            dmg -= defendShield
            defendShield = 0
    if health > dmg and defendShield == 0:
        health -= dmg
        print(name + ": took", dmg, "damage. \n"+ name + ": now has", health, "health.")
        return health
    else:
        health = 0
        return health

def checkifBetter(poktype):
    if poktype == 2:
        reduction = random.randint(0,10)
        print(name, "Is countered by water type pokemon:", reduction, "damage has been lost!")
        return reduction
    else:
        return 0

energyUse = {
    1: 22,
    2: 30,
    3: 15,
    4:0
}
abilityNames = ["Ember", "Blaze", "Flame Charge", "Energy Recharge"]
abilities = {
    1: "Throw and ember at the other opponent.",
    2: "Release a blaze of fire in the opposing area.",
    3: "Defend with a shield of flame around charmander."
}