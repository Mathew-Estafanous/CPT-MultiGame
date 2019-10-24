from time import sleep
import gamesMenu

chipTypes = ["x", "o"]
playerNames = ["",""]
curPlayer = 0
playfield = [[" "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "]]

def startGame():
    print("Welcome to Connect Four! Your goal is to connect 4 of your chips in a row to win! \n")
    print("This is a 2 player game! Please make sure you are playing with another player, or yourself,\nor this will be basically pointless.")
    print("Choose the column that you would like to place your chip in by inputting the column number from left-->right.")
    print("________________________________")
    playerNames[0] = input("Who is Player(X): ")
    playerNames[1] = input("Who is Player(O): ")
    print("Starting Game...")
    sleep(2)
    gameProcessor()

def gameProcessor():
    global playerNames, curPlayer, playfield
    while True:
        print("________________________________________")
        print(playerNames[curPlayer],"is choosing.")
        print("[Current Connect Four Table:]")
        genArea()
        location = input("Input Your Choice 1-7: ")
        try:
            location = int(location) - 1
        except:
            print("Invalid Column: Please choose a valid column.")
            continue

        if location < 1 and location > 7:
            print("Invalid Column: Input a column between 1-7")
            continue

        print("Inputting Chip...")
        sleep(1)
        row = addChip(location)
        if row == -1:
            continue
        result = checkForConnection(location,row)
        if result == True:
            print("_______________________________________")
            print(playerNames[curPlayer], "WINS! Great Job!!!")
            genArea()
            input("Click enter when ready: ")
            #Reset The Playfield
            playfield = [[" "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "],
             [" "," "," "," "," "," "," "]]
            gamesMenu.playAgain()
            break

        if curPlayer == 0:
            curPlayer = 1
            print("Updating To;", curPlayer)
            continue
        curPlayer = 0

def genArea():
    global playfield
    rows = 0
    while rows < 6:
        print("[", playfield[rows][0], "|",playfield[rows][1], "|",playfield[rows][2], "|"
        ,playfield[rows][3], "|",playfield[rows][4], "|",playfield[rows][5], "|",playfield[rows][6], "]")
        rows += 1

def addChip(location):
    global playfield, curPlayer, chipTypes
    column = []
    row = 0
    for x in playfield:
        column.append(x[location])

    rng = len(column) - 1
    while rng >= 0:
        if column[rng] == " ":
            row = rng
            break
        rng -= 1
    else:
        print("COLUMN IS FULL!")
        return -1 #FALSE but not False since a return value of FALSE also equals 0 which is used as a row

    playfield[row][location] = chipTypes[curPlayer]
    return row

def checkForConnection(column, row):
    global playfield, curPlayer, chipTypes

    currentLocation = [row, column]
    #Check heading right in diagonal(and reverse) for connection.
    if rDiagonal(currentLocation) >= 4:
        return True
    #Checking heading Left in Diagonal(and reverse) for connection.
    if lDiagonal(currentLocation) >= 4:
        return True
    #Checking heading right side(and reverse) for connection.
    if sides(currentLocation) >= 4:
        return True
    #Checking heading up and down for connection.
    if upDown(currentLocation) >= 4:
        return True
    return False

def rDiagonal(currentLocation):
    connect = 1
    originalLoc = currentLocation
    while True:
        try:
            if playfield[currentLocation[0] - 1][currentLocation[1] + 1]  != chipTypes[curPlayer]:
                currentLocation = [originalLoc[0], originalLoc[1]]
                break
            connect += 1
            currentLocation = [currentLocation[0] - 1,currentLocation[1] + 1]
        except:
            currentLocation = [originalLoc[0], originalLoc[1]]
            break
    while True:
        try:
            if playfield[currentLocation[0] + 1][currentLocation[1] - 1]  != chipTypes[curPlayer]:
                currentLocation = [originalLoc[0], originalLoc[1]]
                break
            connect += 1
            currentLocation = [currentLocation[0] - 1,currentLocation[1] + 1]
        except:
            currentLocation = [originalLoc[0], originalLoc[1]]
            break

    return connect

def lDiagonal(currentLocation):
    connect = 1
    originalLoc = currentLocation
    while True:
        try:
            if playfield[currentLocation[0] - 1][currentLocation[1] - 1]  != chipTypes[curPlayer]:
                currentLocation = [originalLoc[0], originalLoc[1]]
                break
            connect += 1
            currentLocation = [currentLocation[0] - 1,currentLocation[1] - 1]
        except:
            currentLocation = [originalLoc[0], originalLoc[1]]
            break
    while True:
        try:
            if playfield[currentLocation[0] + 1][currentLocation[1] + 1]  != chipTypes[curPlayer]:
                currentLocation = [originalLoc[0], originalLoc[1]]
                break
            connect += 1
            currentLocation = [currentLocation[0] + 1,currentLocation[1] + 1]
        except:
            currentLocation = [originalLoc[0], originalLoc[1]]
            break

    return connect

def sides(currentLocation):
    connect = 1
    originalLoc = currentLocation
    while True:
        try:
            if playfield[currentLocation[0]][currentLocation[1] - 1]  != chipTypes[curPlayer]:
                currentLocation = [originalLoc[0], originalLoc[1]]
                break
            connect += 1
            currentLocation = [currentLocation[0],currentLocation[1] - 1]
        except:
            currentLocation = [originalLoc[0], originalLoc[1]]
            break
    while True:
        try:
            if playfield[currentLocation[0]][currentLocation[1] + 1]  != chipTypes[curPlayer]:
                currentLocation = [originalLoc[0], originalLoc[1]]
                break
            connect += 1
            currentLocation = [currentLocation[0],currentLocation[1] + 1]
        except:
            currentLocation = [originalLoc[0], originalLoc[1]]
            break
    return connect

def upDown(currentLocation):
    connect = 1
    originalLoc = currentLocation
    while True:
        try:
            if playfield[currentLocation[0] - 1][currentLocation[1]]  != chipTypes[curPlayer]:
                currentLocation = [originalLoc[0], originalLoc[1]]
                break
            connect += 1
            currentLocation = [currentLocation[0] - 1,currentLocation[1]]
        except:
            currentLocation = [originalLoc[0], originalLoc[1]]
            break
    while True:
        try:
            if playfield[currentLocation[0] + 1][currentLocation[1]]  != chipTypes[curPlayer]:
                currentLocation = [originalLoc[0], originalLoc[1]]
                break
            connect += 1
            currentLocation = [currentLocation[0] + 1,currentLocation[1]]
        except:
            currentLocation = [originalLoc[0], originalLoc[1]]
            break
    return connect