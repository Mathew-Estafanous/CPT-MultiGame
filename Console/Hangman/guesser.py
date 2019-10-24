import operator
import random
import gamesMenu
#The maximum number of guesses that the AI can have
maxNumGuess = 10
#has guessed. True = 1/ false = 0
hasguessed = 1
#List of all guessed letters
guessed = []
#Generated visual word with blanks.
genWord = []

#Get list of words and turn them into a list.
listWords = open("words")
currWords = listWords.read().splitlines()
listWords.close()

def gameStart():
    print("Welcome- to the hang man game! You will be thinking of any word and I will try to guess it!")
    print("I have", maxNumGuess, "guesses!")
    print("Time To Guess!--------------")
    input("Enter anything when you have a name in mind!")
    decideGuess()

#Using the letter given make a guess to the player.
def makeGuess(let):
    print("Is,", let, "a letter in the word you chose?")
    yesOrNo = input("Input y/n: ")

    if yesOrNo.lower() == "y":
        #Asking for the location of the letters
        location = input("What is the location of the letter in the word?")
        location = location.split()
        location = list(map(int, location))
        print("----------------------")
        #Filter the possible words
        filterWords(let, location, yesOrNo)
    elif yesOrNo.lower() == "n":
        #Computer Losses 1 Guess
        global maxNumGuess
        maxNumGuess -= 1
        print("No! Damnit! Let me try again.")
        print("I have,", maxNumGuess, "tries left.")
        if maxNumGuess > 0:
            print("----------------------")
            location = [0]
            #Filter the possible words
            filterWords(let, location, yesOrNo)
        else:
            print("Looks like I lost! You are too smart for me!")
    else:
        makeGuess(let)

#Decide which letter to guess based on the most popular letters.
def decideGuess():
    global currWords
    global hasguessed
    #If this is first guess ask for length of the word.
    if hasguessed == 1:
        wordlength = int(input("Input the length of your word."))
        hasguessed = 0
        #Filter out all words that are not the provided length
        initialFilter(wordlength, currWords)
        #Make a visual representation of the word with blanks.
        generateWord("first", wordlength, 0, 0)

    #Dictionary that will store the letter and the amount of it found.
    letters = {
        #Letter: Number
    }
    #check each letter in every word and add it to the letter dictionary.
    for n in currWords:
        for i in range(len(n)):
            if n[i] in letters and n[i] not in guessed:    #Make sure letter is not already guessed.
                letters[n[i]] += 1  #Adding to an already stated letter
            elif n[i] not in guessed:
                letters[n[i]] = 1   #Making a new letter in the dictionary

    #Choose the most popular letter and make the guess.
    guesslet = max(letters.items(), key=operator.itemgetter(1))[0]
    guessed.append(guesslet)
    makeGuess(guesslet)

#Filter the possible words
def filterWords(let, location, yes):
    global currWords
    #variable for new list of filter names.
    newWords = []
    #Check if already visually generated the word.
    generated = 0
    #The amount of the certain letter needed to find in the word.
    needtofind = len(location) - 1
    #Check the location and character of each word and compare it to the required location and letter.
    for word in currWords:
        locationsfound = 0
        for loc in location:
            if word[loc - 1] == let and yes == "y" and locationsfound != needtofind:  #Found 1 letter but not all yet.
                locationsfound += 1
            elif word[loc - 1] == let and yes == "y": #Found all letters needed
                newWords.append(word)
                #Generate the word visually
                if generated == 0:
                    generateWord("", 0, let, location)
                    generated += 1
            #If the letter is NOT in the word then filter out any word with that letter in it.
            elif let not in word and yes == "n":
                newWords.append(word)
                break
    #Update the current list of words with new list of words
    currWords = newWords
    checkifFound(currWords)

#Filtering out every word that is not the specefied length
def initialFilter(length, theWords):
    global currWords
    newWords = []
    for word in theWords:
        if len(word) == length:
            newWords.append(word)
    currWords = newWords

#Checking if the word is found or not.
def checkifFound(name):
    global genWord
    #If the list only has one word then the state that is the word.
    if len(name) == 1:
        print("The word you are thinking of is,", name[0])
    else:
        blank = 0
        for let in genWord:
            #Checking if the letter is blank and adding it to the total blanks.
            if let == "__":
                blank += 1
        #If the generated word has only 1 blank left start making random word guesses
        if blank == 1:
            randomguess()
        #If it has more than one blank continue with guessing letters
        else:
            decideGuess()

#Generating the word visual for the player
def generateWord(isFirst, wordlength, let, location):
    global genWord
    #If it is the first time generating just make every character a blank line.
    if isFirst == "first":
        for i in range(wordlength):
            genWord.append("__")
    #Update the word with the character at the stated location.
    else:
        for loc in location:
            genWord[loc - 1] = let
    print("This is your Word:", genWord)

#Make a random guess as to what word it could be.
def randomguess():
    global maxNumGuess
    randGuess = random.randint(0, len(currWords) - 1)
    #Ask if the word guessed is correct
    print("Is,", currWords[randGuess], "the word you are thinking of?")
    isRight = input("(y/n):")
    #If it is not correct lose a guess and try again.
    if isRight == "n":
        currWords.remove(currWords[randGuess])
        #when guesses reach 0 the computer has lost.
        if maxNumGuess - 1 == 0:
            print("I Lost! Thanks for playing with me!")
            gamesMenu.playAgain()
        #Make a new guess and lose a life.
        else:
            maxNumGuess -= 1
            randomguess()
    #If the guess was right then the computer wins!
    else:
        print("I win! Looks like I was right after all!")
        gamesMenu.playAgain()
