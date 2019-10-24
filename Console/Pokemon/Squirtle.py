import random
#Pokemon Statistics
name = "Squirtle"
health = 85 #85
type = 2 #Water
damageRate = 20
energy = 100
defendShield = 0

def findAbility(choosen, pokType):
    if choosen == 1:
        damage = waterGun()
    elif choosen == 2:
        damage = bubble()
    elif choosen == 3:
        return hydroPump()
    else:
        return rechargeEnergy()
    damage -= checkifBetter(pokType)
    return damage

def waterGun():
    global energy, energyUse
    energy -= energyUse[1]
    damage = damageRate
    if random.randint(1,6) <= 2:
        critical = random.randint(10,20)
        damage += critical
        print("Critical Hit! +", critical, "damage!")
    return damage

def bubble():
    global energy, energyUse
    energy -= energyUse[2]
    damage = damageRate
    if random.randint(1,16) <= 4:
        critical = random.randint(20,30)
        damage += critical
        print("Critical Hit! +", critical, "damage!")
    return damage

def hydroPump():
    global defendShield
    global energy, energyUse
    energy -= energyUse[3]
    defendShield = random.randint(5,15)
    print(name,"has pumped up with water. Defending for,", defendShield, "damage.")
    return False

def rechargeEnergy():
    global energy
    chargeAmount = random.randint(40, 100)
    if chargeAmount + energy <= 100:
        energy += chargeAmount
        print(name, "Now has", energy, "energy")
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
    if poktype == 3:
        reduction = random.randint(0,10)
        print(name, "Is countered by grass type pokemon:", reduction, "damage has been lost!")
        return reduction
    else:
        return 0

energyUse = {
    1: 20,
    2: 25,
    3: 10,
    4:0
}
abilityNames = ["Water Gun", "Bubble", "Hydro Pump", "Energy Recharge"]
abilities = {
    1: "Shoot a water gun at the opposing enemy.",
    2: "Release dangerous bubbles that pop on the opposing enemy.",
    3: "Pump up with water in defense."
}
