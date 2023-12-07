import random
import time


def printLeftArrow(myRndPts, line):
    if myRndPts >= line and myRndPts < line + 5:
        print(format(myRndPts, ">2d"), ">>> ", end="")
    else:
        print("       ",end="")
def printDevilLeft(devilRndPts, line):
    if devilRndPts >= line and devilRndPts < line + 5:
        print(format(devilRndPts, ">2d"), ">>> ", end="")
    else:
        print("       ",end="")

def printScale(line):
    print(format(line, ">3d"), end="")

def diceRoll(die,line):
    if line == 70:
        print(format("die", "<3s"), end="")
    elif line == 65:
        print(format(die, "^3d"), end="")
    else:
        print("   ", end="")

def printRightArrow(myPts, line):
    if myPts >= line and myPts < line + 5:
        print(" <<<", format(myPts, "<2d"), end="")
    else:
        print("      ",end="")
def printDevilRight(devilPts, line):
    if devilPts >= line and devilPts < line + 5:
        print(" <<<", format(devilPts, "<2d"), end="")
    else:
        print("     ",end="")

def printCoolBoard(myRndPts, myPts, devilRndPts, devilPts, die, myTurn):
    print(format("  Devil's Dice","^60s"))
    if myTurn:
        print(format("   *You*\t\t\t\t\t\tThe Devil", "^45s"))
    else:
        print(format("\t   You\t\t\t\t\t   *The Devil*", "^45s"))
    print("\t\t turn\t\tscore\t\t\tturn\t\tscore")
    for line in range (100, -5, -5):
        print("        ", end="")
        printLeftArrow(myRndPts, line)
        printScale(line)
        printRightArrow(myPts, line)
        print("     ", end="")
        diceRoll(die, line)
        print("   ", end="")
        printDevilLeft(devilRndPts, line)
        printScale(line)
        printDevilRight(devilPts, line)

        print()


#the backup plan------------------------------------------------------------
def uDie(die):
    # die - Integer valued 1-6.  The rolled die value.

    if die == 1: return "\u2620"
    if die == 2: return "\u2681"
    if die == 3: return "\u2682"
    if die == 4: return "\u2683"
    if die == 5: return "\u2684"
    if die == 6: return "\u2685"

def printSimpleBoard(die, myTurn, myPts, devilPts, myRndPts, devilRndPts):
    # die - Integer valued 1-6.  The rolled die value.
    # myPts - Integer valued 0-100. The current saved score of the human player.
    # devilPts - Integer valued 0-100. The current saved score of the devil.
    # myTurn - Boolean value.  True if it is the human player's turn.
    # myRndPts - Integer valued 0-100.  The human's saved score plus points gained that round.
    # devilRndPts - Integer valued 0-100.  The devil's saved score plus points gained that round.

    print("\n")
    print(" my\t\tthis\tdevil's\t this")
    print("score\tround\t score\tround")
    print("  ", myPts, "\t  ", myRndPts, "\t  ", devilPts, "\t  ", devilRndPts)
    print(format("die", "^30s"))
    print(format(uDie(die), "^30s"))
#------------------------------------------------------------------------------


def getResponse():
    r = input("[r]oll or [p]ass?: ")
    while (r!='r' and r!='p'):
        print("huh?")
        r = input("[r]oll or [p]ass?: ")
    return r

def devilResponse(myPts, devilPts, devilRndPts):
    if myPts <= devilPts and devilRndPts-devilPts < 21:
        return 'r'
    elif myPts > devilPts and devilRndPts-devilPts < 30:
        return 'r'
    else:
        return 'p'



def main():
    print("Welcome to Devil's Dice!")
    print("Care for a game?")
    myPts=0
    devilPts=0
    myRndPts=0
    devilRndPts = 0
    die = random.randint(1, 6)
    myTurn=True


    while True:

        if myPts >= 100 or myRndPts >= 100 or devilPts >= 100 or devilRndPts>=100:
            myPts = myRndPts
            devilPts = devilRndPts
            printCoolBoard(myRndPts, myPts, devilRndPts, devilPts, die, myTurn)
            if myPts>=100:
                print(format("\u2606 Winner!\u2606", "^60s"))
            else:
                print(format("   Better luck next time!", "^60s"))
            break

        if myTurn:
            printCoolBoard(myRndPts, myPts, devilRndPts, devilPts, die, myTurn)
            r = getResponse()

        else:
            printCoolBoard(myRndPts, myPts, devilRndPts, devilPts, die, myTurn)
            print("\ndevil is rolling...")
            time.sleep(1)
            r = devilResponse(myPts, devilPts, devilRndPts)
            if r == 'p':
                print("The devil passes.")

        if r == "p":
            if myTurn:
                myPts = myRndPts
                myTurn = False
            else:
                devilPts = devilRndPts
                myTurn = True


        elif r == 'r':
            die = random.randint(1, 6)
            if die == 1:
                if myTurn:
                    print("You rolled a 1! Tough luck.")
                    myRndPts = myPts
                    myTurn = False
                else:
                    devilRndPts = devilPts
                    myTurn = True

            else:
                if myTurn:
                    print("You rolled a",die,"!")
                    myRndPts += die
                else:
                    print("The devil rolled a",die,"!")
                    devilRndPts += die



main()