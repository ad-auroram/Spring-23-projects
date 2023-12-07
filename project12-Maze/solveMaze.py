#Roxanne Seeley
#Section 002

import time
import sys

SLEEPTIME = 0.1
FILENAME = "maze.txt"
VERBOSE = True

# TODO: write all your code below this line
#
# put the line "if VERBOSE: printMaze(maze)"
# every time you drop/retrieve a marker
#
def solve(maze, r, c):
    if maze[r][c]== "X": return False
    if maze[r][c]== ".": return False
    if r==len(maze)-2 and c==len(maze[r])-1:
        maze[r][c]="\u2606"
        return True

    maze[r][c]="."
    if VERBOSE: printMaze(maze)

    if solve(maze, r + 1, c): return True
    if solve(maze, r - 1, c): return True
    if solve(maze, r, c + 1): return True
    if solve(maze, r, c - 1): return True

    maze[r][c]=" "
    if VERBOSE: printMaze(maze)
    return False


# TODO: write all your code above this line

def readMaze(maze):
    mazefile = open(FILENAME, "r")
    for line in mazefile.read().splitlines():
        maze.append([])
        for c in line:
            maze[-1].append(c)
    mazefile.close()


def printMaze(maze):
    print("\n\n\n\n\n\n\n\n\n")
    for i in range(0,len(maze)):
        for j in range(0,len(maze[i])):
            print(maze[i][j],end="")
        print()
    time.sleep(SLEEPTIME)
    print()
    

def main():
    maze = []
    readMaze(maze)
    if not solve(maze,1,0):
        print("no solution is possible.")
    else:
        printMaze(maze)



main()
