import random
#Pokemon Statistics
name = "Bulbasaur"
health = 125
type = 3 #Grass
damageRate = 20
energy = 100
defendShield = 0

def findAbility(choosen, pokType):
    if choosen == 1:
        damage = vinewip()
    elif choosen == 2:
        damage = razorLeaf()
    elif choosen == 3:
        return sludgebomb()
    else:
        return rechargeEnergy()
    damage -= checkifBetter(pokType)
    return damage

def vinewip():
    global energy, energyUse
    energy -= energyUse[1]
    damage = damageRate
    if random.randint(1,6) == 1:
        critical = random.randint(10,20)
        damage += critical
        print("Critical Hit! +", critical, "damage!")
    return damage

def razorLeaf():
    global energy, energyUse
    energy -= energyUse[2]
    damage = damageRate
    if random.randint(1,8) == 1:
        critical = random.randint(20,30)
        damage += critical
        print("Critical Hit! +", critical, "damage!")
    return damage

def sludgebomb():
    global defendShield
    global energy, energyUse
    energy -= energyUse[3]
    defendShield = random.randint(15,25)
    print("Put a defensive poison surrounding,", name + ". Shielding for:", defendShield, "damage.")
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
    global defendShield
    global health
    global name
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
        print(name + ": took", dmg, "damage. \n" + name + ": now has", health, "health.")
        return health
    else:
        health = 0
        return health

def checkifBetter(poktype):
    if poktype == 4:
        reduction = random.randint(0,10)
        print(name, "Is countered by electric type pokemon:", reduction, "damage has been lost!")
        return reduction
    else:
        return 0

energyUse = {
    1: 15,
    2: 20,
    3: 30,
    4:0
}
abilityNames = ["Vine Wip", "Razor Leaf", "Sludge Bomb", "Energy Recharge"]
abilities = {
    1: "Whip a vin at opposing enemy.",
    2: "Throw a razor leaf at the opposing enemy.",
    3: "Defend by placing a dangerous poison bomb around, Bulbasaur."
}