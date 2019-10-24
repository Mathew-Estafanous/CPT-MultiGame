from time import sleep

import Pokemon.startingTitle
import WordHunt.processor
import ConnectFour.cnt4

import sys

def chooseGame():
    print("Welcome to GameSpace! Here you can play a variaty of small mini games for you to enjoy. \n all the the mini games are text based and easy to play!")
    print("Lets start! Choose the game you want to play!")
    print("[CHOOSE A GAME:]")
    print("1)",gameNames[0].upper() + ":", description[0])
    print("2)",gameNames[1].upper() + ":", description[1])
    print("3)",gameNames[2].upper() + ":", description[2])
    print("4)",gameNames[3].upper() + ":", description[3])
    print("____________________________________________________________")
    while True:
        choice = input("Choose A Game: ")
        try:
            choice = int(choice)
        except:
            print("Invalid Input: Input a valid number")
            continue

        if choice < 1 or choice > 4:
            print("Invalid Input: Input a number between 1-4")
            continue

        print("STARTING GAME.....")
        sleep(2)
        if choice == 1:
            import Hangman.guesser
            Hangman.guesser.gameStart()
        elif choice == 2:
            Pokemon.startingTitle.chooseCharacter()
        elif choice == 3:
            WordHunt.processor.gameInfo()
        else:
            ConnectFour.cnt4.startGame()

def playAgain():
    print("_____________________________________________")
    print("Thanks for playing!")
    while True:
        chosen = input("Would you like to play again? (y/n): ").lower()
        if chosen == "y":
            sleep(2)
            print("____________________")
            chooseGame()
        elif chosen == "n":
            print("Thank You! Hope to see you again another time!")
            sys.exit()
            break
        else:
            print("Invalid Input: Input y or n.")

gameNames = ["AI HangMan", "Pokemon Battle", "Word Hunt","Connect Four"]
description = {
    0: "Think of any word in the entire english dictionary and see if the AI can guess the word you are thinking of!",
    1: "Choose a pokemon of your choice and start playing against an enemy pokemon until one of you wins!",
    2: "Be given a list of letters and try to find out what the word is. (2 Player Game)",
    3: "Player with a friend and see who can get 4 in a row! (2 Player Game)"
}

chooseGame()