import random
import time

def printMap(map):
    print("\n\n\n")
    for i in range(0,len(map)):
        for j in range(0,len(map[i])):
            print(map[i][j],end="  ")
        print()

#who's next to me
def howManyNeighbors(map, r,c):
    neighbors = 0
    for i in range(r-1,r+2):
        for j in range(c-1,c+2):
            if map[i][j]=="X": neighbors +=1
    if map[r][c] == "X":
        neighbors -= 1
    return neighbors

#what's next
def nextGen(map, nextMap):
    for i in range(1, len(map) -1):
        for j in range(1, len(map[i]) -1):
            n = howManyNeighbors(map, i, j)
            if map[i][j] == "X" and (n==2 or n==3):
                nextMap[i][j] = "X"
            elif map[i][j]==" " and n==3:
                nextMap[i][j]="X"
            else:
                nextMap[i][j]=" "
    for i in range(1, len(map)-1):
        for j in range(1,len(map[i])-1):
            map[i][j]=nextMap[i][j]


def main():
    world = 22
    map = []
    nextMap = []

    for i in range(0, world):
        map.append([])
        nextMap.append([])

    for i in range(0, world):
        for j in range(0, world):
            map[i].append(" ")
            nextMap[i].append(" ")

    for i in range(0,((world-2)**2)//3):
        map[random.randint(1,world-2)][random.randint(1,world-2)]="X"

    for i in range(1,50):
        printMap(map)
        nextGen(map, nextMap)
        time.sleep(0.3)




main()