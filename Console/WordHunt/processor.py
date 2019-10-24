from time import sleep
import random
import math
import string
import gamesMenu

players = []
scores = [0,0]
possibleWords = []

#Get list of words and turn them into a list.
listWords = open("words")
allWords = listWords.read().splitlines()
listWords.close()
#Keeping only words that are 4-6 letters
for x in allWords:
    if len(x) <= 5 and len(x) >= 4:
        possibleWords.append(x)

def gameInfo():
    global players
    print("Welcome to the game Word Hunt! \nYour goal is to guess the word provided by using the given index. Some letters are added!\n")
    print("This is a two player game! To keep it fair, make sure the player who is \nnot playing is looking away from the screen at all times to ensure they are not cheating!")
    print("_________________________________________")
    players.append(input("Input Player 1's Name:"))
    players.append(input("Input Player 2's Name:"))
    print("Starting Game....")
    sleep(5)
    runGame()

def runGame():
    rounds = 1
    while rounds < 4:
        print("___________________________________")
        print("[ROUND",rounds, "]")
        playerAction(0)
        print("Changing Turns...")
        sleep(2)
        playerAction(1)
        rounds += 1
    endGame()


def playerAction(currentPlayer):
    global players, scores,possibleWords
    print(players[currentPlayer], "is going this round.")
    sleep(1)
    triesLeft = 4
    word = generateCharacters()
    print("Time To Guess The Words")
    while triesLeft > 0:
        print("You have", triesLeft, "tries left.")
        guess = input("Input Hunted Word: ").lower()
        if guess == word:
            scores[currentPlayer] += triesLeft * 100
            print("CORRECT!", guess,"is the word given!.")
            break
        else:
            print("WRONG!", guess,"is not the word given.")
        triesLeft -= 1
    if triesLeft == 0:
        print("The word was:", word.upper())
    print("Game Stats______________________")
    print("Player:", players[currentPlayer])
    print("Score:", scores[currentPlayer])
    print("Good Job!")
    return

def generateCharacters():
    global possibleWords
    word = possibleWords[random.randint(0, len(possibleWords) - 1)]
    letters = []
    for x in word:
        letters.append(x)
    random.shuffle(letters)
    print("Here Are Your Letter Choices:")
    print(letters)
    return word

def endGame():
    global players, scores
    print("GAME OVER:")
    if scores[0] > scores[1]:
        print("Congratulations to,", players[0], "for getting the better score of,", scores[0], "points!")
    elif scores[0] < scores[1]:
        print("Congratulations to,", players[1], "for getting the better score of,", scores[1], "points!")
    else:
        print("It's a Tie! Maybe next time someone will win.")
    input("Press Enter When Ready! ")
    gamesMenu.playAgain()