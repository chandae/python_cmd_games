#!/usr/bin/python3

import sys, time

credits = """The Tower of Hanoi By Emmanuel Chanda @2022 emmmanuelvchanda1@gmail.com"""
introMessage = """
    The Tower of Hanoi puzzle uses a stack of disks of different sizes. The disks
    have holes in their centers, so you can place them over one of three poles.
    To solve the puzzle, the player must move the stack of disks to
    one of the other poles. There are three restrictions:
        1. The player can move only one disk at a time.
        2. The player can only move disks to and from the top of a tower.
        3. The player can never place a larger disk on top of a smaller disk.
"""
instructions1 = "Enter 'from' and 'to' letters to move disks between towers. Use 'exit' to QUIT."
instructions2 = "For Example: 'AB' or 'ab' to moves a disk from tower A to tower B."

def intro():
    """ Print credits and game instructions and rules"""
    print(credits)
    print('Loading...')
    time.sleep(1.5)
    print(introMessage)

def initialise():
    """ Player and Game Setup """
    # get player details
    playerName = input("Enter Player Username (Must be at least three (3) letters long): ")
    while len(playerName) < 3:
        print("Username too short. Try another one :)")
        playerName = input("Enter Player Username (Must be at least three (3) letters long): ")
    print(f"Welcome {playerName}! The Tower Of Hanoi Awaits You.")
    return playerName

def printScreen(poles):    
    """ Print the screen to the user """
    print()
    canvas = list(zip(poles.get('A'), poles.get('B'), poles.get('C')))
    for pole in canvas:
        print(*pole)
    print(f"      A            B           C          ")
    print()
    
def updateScreen(move, poles, disks, stand, username):
    """ Update the screen and disks after a player makes a move """
    # remove all whitespaces and unwanted chars before getting the individual moves
    source = poles.get(move[0])
    target = poles.get(move[1])
    
    # first check if source pole is empty; if not get the top-most disk on the source pole
    while True:
        if sourceEmpty(source, stand)[0]:
            print()
            print("Pole is empty. Pick another one.")
            gamePlay(poles, disks, stand, username)
        else:
            top_most, open_index = sourceEmpty(source, stand)[1:]
            break
    # check for next available slot on target pole
    open_slot = 1
    
    for slot in range(2, len(target)):
        if target[slot] != stand:
            break
        open_slot = slot

    # validate player move
    if dropValidator(target, open_slot, top_most):
        target[open_slot]  = top_most
        source[open_index] = stand
        poles[move[0]] = source
        poles[move[1]] = target
        return poles
    else:
        print("Invalid move. You can't drop a big disk on a smaller one. Try Again!")
        return poles

def validator(move):
    """ Validate a player's move """
    # check move length: maximum and minimum should be 2
    if len(move) == 2 and move in ['AB', 'AC', 'BC', 'BA', 'CA', 'CB']:
        if move[0] != move[1]:
            return True
    else:
        return False

def dropValidator(target, open_slot, top_most):
    """ Validator to check disk sizes before dropping them according to game rules """
    if (open_slot + 1) == len(target):
        # first disk on the pole
        return True
    else:
        currentBase = target[open_slot + 1]
        newDisk = top_most
        if len(currentBase.strip()) > len(newDisk.strip()):
            return True
        else:
            return False
        
def sourceEmpty(source, stand):
    """ Check if source is empty. If not, get the top-most disk """
    top_most = stand
    open_index = ""

    for disk in range(len(source)):
        if source[disk] != stand:
            top_most = source[disk]
            open_index = disk
            break
    if top_most == stand: 
        return [True]
    else:
        return [False, top_most, open_index]
    
def playerHasWon(poles, disks):
    """ Check if a player has won. Player can only win on pole B and C """
    # get poles B and C; check if player has won
    hasWon_check1 = hasWon_check2 = False
    poleB = poles.get('B')
    poleC = poles.get('C')

    # check pole B; first, second, third, fourth and fifth
    if (poleB[1] == disks.get(1) and poleB[2] == disks.get(2) and poleB[3] == disks.get(3) and poleB[4] == disks.get(4)):
        hasWon_check1 = True
    if (poleC[1] == disks.get(1) and poleC[2] == disks.get(2) and poleC[3] == disks.get(3) and poleC[4] == disks.get(4)):
        hasWon_check2 = True
    # final check
    if hasWon_check1 or hasWon_check2: return True
    return False
    
# get player move and print screen with new changes
def gamePlay(poles, disks, stand, username):
    """ Get player move and update screen with new changes. Print screen afterwards """
    # Number of attempts made
    attemptsCounter = 1

    while True:
        try: 
            print(instructions1)
            print(instructions2)
            playerMove = input(f"Enter your move {username}: ").strip().upper()
            if playerMove.lower() == 'exit':
                break
            while not validator(playerMove):
                print("Invalid Move. Refer To Game Rules And Try Again!")
                playerMove = input(f"Enter your move {username}: ").strip().upper()
            poles = updateScreen(playerMove, poles, disks, stand, username)
            print()
            print(f"Attempts: {attemptsCounter}")
            printScreen(poles)

            if playerHasWon(poles, disks):
                print(f"Congratulations {username}! You have WON. The Tower Of Hanoi Belongs to You.")
                print(f"You made (moved the disks) {attemptsCounter} times.")
                print()
                break
            attemptsCounter += 1
        except KeyboardInterrupt:
            break
    print("Thanks for playing!")
    print("Quitting...")
    time.sleep(2)
    sys.exit()

def main():
    global credits, introMessage
    # game screen and canvas
    stand = f"{' ' * 5}||{' ' * 5}"
    disks = {0: "     ||     ", 1: "    @_1@    ", 2: "   @@_2@@   ", 3: "  @@@_3@@@  ", 4: " @@@@_4@@@@ ", 5: "@@@@@_5@@@@@"}
    poles = {'A': [disk for disk in disks.values()], 'B': [stand for i in range(6)], 'C': [stand for i in range(6)]}

    intro()
    username = initialise()
    printScreen(poles)
    
    # get player move and print screen with new changes
    gamePlay(poles, disks, stand, username)

# ************************************************************ MAIN *****************************************************************
if __name__ == "__main__":
    main()
