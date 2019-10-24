#This script is incharge of all the fighting between the player and the AI pokmon.
import Pokemon.Charmander
import Pokemon. Bulbasor
import Pokemon.Squirtle
import Pokemon.Pikachu
from time import sleep
import random
import operator
import gamesMenu

#Player Information
characterScript = 0
charName = ""
charType = ""
charHealth = 0
#Enemy Information
enemyScript = 0
enemyName = ""
enemyType = ""
enemyHealth = 0

#Time to wait
waitTime = 6

def getPokemon(character, enemy):
    global characterScript, charName,charType,charHealth
    global enemyScript, enemyName, enemyType,enemyHealth
    print("Getting Pokemon Information")
    characterScript = character
    #Getting Player's Pokemon
    charName = character.name
    charType = character.type
    charHealth = character.health
    #Getting Enemy Pokemon
    enemyScript = enemy
    enemyName = enemy.name
    enemyType = enemy.type
    enemyHealth = enemy.health
    chooseAbility()

def chooseAbility():
    print("_____________________________________________")
    global characterScript, charName, charHealth
    global enemyName, enemyHealth
    print("[Game Statistics:]")
    print(charName + "'s Health:", charHealth)
    print(charName + "'s Energy Level:", characterScript.energy)
    print(enemyName + "'s Health:", enemyHealth)
    print(enemyName + "'s Energy Level:", enemyScript.energy)
    #Player Gets To Choose The Move
    print("[CHOOSE YOUR MOVE:]")
    for x in characterScript.abilities:
        print(characterScript.abilityNames[x - 1].upper() + ": " + characterScript.abilities[x], "(", characterScript.energyUse[x], "Energy)")
    print("1 =", characterScript.abilityNames[0], "|| 2 =", characterScript.abilityNames[1], "|| 3 =", characterScript.abilityNames[2], "|| 4 = Energy Recharge")
    while True:
        abilityChoose = input("Choose Move: ")
        try:
            abilityChoose = int(abilityChoose)
        except:
            print("INVALID INPUT: Input must be between 1-4!")
            continue

        if abilityChoose < 1 or abilityChoose > 4:
            print("INVALID INPUT: Input must be between 1-4!")
            continue
        elif characterScript.energy < characterScript.energyUse[abilityChoose]:
            print("Not Enough Energy: You have,", characterScript.energy, "energy.")
            continue
        abilityResult = characterScript.findAbility(abilityChoose, enemyType)
        if abilityResult != False:
            enemyHealth = enemyScript.takeDamage(abilityResult)
            if enemyHealth != 0:
                enemyMove()
            else:
                endTitle(1)
            break
        else:
            enemyMove()
            break

def currentStats(x):
    global waitTime
    sleep(waitTime)
    print("CURRENT STATS:_______________________________")
    if x == 1: #Update Just the Player Stats
        print("Your Pokemon:", charName)
        print(charName + "'s Health:", charHealth)
    elif x == 2: #Update Player On Both Player and Enemy.
        print("Your Pokemon:", charName)
        print(charName + "'s Health:", charHealth)
        print("------")
        print("Enemy Pokemon:", enemyName)
        print(enemyName + "'s Health:", enemyHealth)
    else: #Update Player on Just Enemy
        print("Enemy Pokemon:", enemyName)
        print(enemyName + "'s Health:", enemyHealth)
    sleep(waitTime)
    chooseAbility()

def enemyMove():
    global charHealth, characterScript
    global enemyName, enemyScript, waitTime
    print("_____________________________________________")
    print(enemyName + ": choosing their move....")
    sleep(waitTime)
    move = chooseGoodMove()
    print(enemyName + ": used the ability,", enemyScript.abilityNames[move - 1])
    damage = enemyScript.findAbility(move, charType)
    if damage != False:
        charHealth = characterScript.takeDamage(damage)
    if charHealth != 0:
        sleep(waitTime)
        chooseAbility()
    else:
        endTitle(2)

def chooseGoodMove():
    global enemyHealth, enemyScript
    global charHealth

    secLowest = list(sorted(enemyScript.energyUse.values()))[-3]
    if enemyScript.energy >= secLowest:
        while True:
            decision = random.randint(1,3)
            if enemyScript.energy >= enemyScript.energyUse[decision]:
                    break
    else:
        decision = 4
    return decision

def endTitle(x):
    global enemyName
    global charName
    if x == 1:
        print(enemyName, "has fainted! You Have WON!")
        sleep(waitTime)
        gamesMenu.playAgain()
    elif x == 2:
        print(charName, "has fainted! You Have LOST!")
        sleep(waitTime)
        gamesMenu.playAgain()