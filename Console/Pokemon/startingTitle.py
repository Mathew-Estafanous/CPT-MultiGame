import random
from time import sleep

import Pokemon.Pikachu
from Pokemon import fighting

#Character Information
choosenChar = 0
#Enemy Information
choosenEnemy = 0

#All Pokemon
characters = {
        1: Pokemon.Charmander,
        2: Pokemon.Bulbasor,
        3: Pokemon.Squirtle,
        4: Pokemon.Pikachu
}

pokemonType = {
    1: "Fire",
    2: "Water",
    3: "Grass",
    4: "Electricity"
}

def chooseCharacter():
    print("Welcome to POKEMON TOURNAMENT! \nChoose Your POKEMON")
    print("Charmander = 1 || Bulbasaur = 2 || Squirtle = 3 || Pikachu = 4 ")
    while True:
        global choosenChar
        choosenChar = input("Choose Your Pokemon: ")
        try:
            choosenChar = int(choosenChar)
        except:
            print("Invalid Input")

        if type(choosenChar) == int:
            if choosenChar > 0 and choosenChar < 5:
                AcessCharacter(choosenChar)
                break
            else:
                print("Invalid Number: please choose a valid character number.")

def AcessCharacter(characterVal):
    print("_____________________________________________")
    global characters
    global choosenEnemy
    charScript = characters[characterVal]
    #Displaying Character Statistics
    print("Your Pokemon:", charScript.name)
    print(charScript.name,"has",charScript.health, "health. \n"+ charScript.name,"is type",pokemonType[charScript.type])
    print(charScript.name,"deals",charScript.damageRate, "damage.")
    #Break between information given:
    sleep(5)
    #Randomly Generate Enemy
    enemyScript = generateEnemy()
    #Break between information given:
    sleep(5)
    #StartFight
    fighting.getPokemon(charScript, enemyScript)

def generateEnemy():
    print("_____________________________________________")
    global characters
    global choosenChar
    global choosenEnemy
    while True:
        choosenEnemy = random.randint(1,4)
        if choosenEnemy != choosenChar:
            break
    enemyScript = characters[choosenEnemy]
    print("Enemy Pokemon:", enemyScript.name)
    print(enemyScript.name,"has",enemyScript.health, "health. \n"+ enemyScript.name,"is type",pokemonType[enemyScript.type])
    print(enemyScript.name,"deals",enemyScript.damageRate, "damage.")
    return enemyScript