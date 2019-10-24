import random
#Pokemon Statistics
name = "Pikachu"
health = 100
type = 4 #Electricity
damageRate = 15
energy = 100
defendShield = 0

def findAbility(choosen, pokType):
    if choosen == 1:
        damage = Discharge()
    elif choosen == 2:
        damage = Thunderbolt()
    elif choosen == 3:
        return electricCharge()
    else:
        return rechargeEnergy()
    damage -= checkifBetter(pokType)
    return damage

def Discharge():
    global energy, energyUse
    energy -= energyUse[1]
    damage = damageRate
    if random.randint(1,100) <= 21:
        critical = random.randint(10,20)
        damage += critical
        print("Critical Hit! +", critical, "damage!")
    return damage

def Thunderbolt():
    global energy, energyUse
    energy -= energyUse[2]
    damage = damageRate
    if random.randint(1,80) <= 13:
        critical = random.randint(20,30)
        damage += critical
        print("Critical Hit! +", critical, "damage!")
    return damage

def electricCharge():
    global energy, energyUse
    global defendShield
    energy -= energyUse[3]
    defendShield = random.randint(10,15)
    print("Pikachu is charging with electricity. Defending for,", defendShield, "damage.")
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
        print(name + ": took", dmg, "damage. \n"+ name + ": now has", health, "health.")
        return health
    else:
        health = 0
        return health

def checkifBetter(poktype):
    if poktype == 1:
        reduction = random.randint(0,10)
        print(name, "Is countered by fire type pokemon:", reduction, "damage has been lost!")
        return reduction
    else:
        return 0

energyUse = {
    1: 21,
    2: 26,
    3: 17,
    4:0
}
abilityNames = ["Discharge", "Thunderbolt", "Wild Charge", "Energy Recharge"]
abilities = {
    1: "Release a discharge of electricity on opposing enemy.",
    2: "Bring a lightning bolt from the sky onto opposing enemy.",
    3: "Charge up with electricity."
}
