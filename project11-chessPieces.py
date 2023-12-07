import random


# the chess piece super class
class ChessPiece:
    def __init__(self, color, x, y):
        self.__color = color
        self.__x = x
        self.__y = y

    def color(self):
        return self.__color

    def location(self):
        return (self.__x, self.__y)

    def x(self):
        return self.__x

    def y(self):
        return self.__y


# TODO: write all your code below this line
#Roxanne Seeley
#Section 002

class Bishop(ChessPiece):
    def __init__(self,c,x,y):
        super().__init__(c,x,y)

    def pic(self):
        if self.color() =="w":
            return "\u2657"
        else:
            return "\u265d"

    def validMove(self,x,y):
        diffx = abs((self.x()-x))
        diffy = abs((self.y()-y))
        if diffx == diffy:
            return True


class Knight(ChessPiece):
    def __init__(self,c,x,y):
        super().__init__(c,x,y)

    def pic(self):
        if self.color()=="w":
            return "\u2658"
        else:
            return "\u265E"

    def validMove(self,x,y):
        diffx = abs((self.x() - x))
        diffy = abs((self.y() - y))
        if diffx==2 and diffy ==1:
            return True
        if diffx==1 and diffy==2:
            return True


class Queen(ChessPiece):
    def __init__(self,c,x,y):
        super().__init__(c,x,y)

    def pic(self):
        if self.color() == "w":
            return "\u2655"
        else:
            return "\u265b"

    def validMove(self,x,y):
        diffx = abs((self.x()-x))
        diffy = abs((self.y()-y))
        if diffx and not diffy:
            return True
        if diffy and not diffx:
            return True
        if diffx == diffy:
            return True


class King(ChessPiece):
    def __init__(self,c,x,y):
        super().__init__(c,x,y)

    def pic(self):
        if self.color()=="w":
            return "\u2654"
        else:
            return "\u265a"
    def validMove(self,x,y):
        diffx = abs((self.x()-x))
        diffy = abs((self.y()-y))
        if diffx == 1 and diffy == 1: return True
        if diffy == 1 and diffx==0: return True
        if diffx == 1 and diffy==0: return True


class Rook(ChessPiece):
    def __init__(self,c,x,y):
        super().__init__(c,x,y)

    def pic(self):
        if self.color()=="w":
            return "\u2656"
        else:
            return "\u265c"

    def validMove(self,x,y):
        diffx = abs((self.x()-x))
        diffy = abs((self.y()-y))
        if diffx and not diffy:
            return True
        if diffy and not diffx:
            return True


class Pawn(ChessPiece):
    def __init__(self,c,x,y):
        super().__init__(c,x,y)

    def pic(self):
        if self.color() == "w":
            return "\u2659"
        else:
            return "\u265f"
    def validMove(self,x,y):
        diffx = ((self.x()-x))
        diffy = ((self.y()-y))
        if self.color()=="b":
            if diffy == 1 and diffx==0: return True
        if self.color()=="w":
            if diffy == -1 and diffx ==0: return True

# TODO: write all your code above this line


# print a nice picture of the valid moves
# white pawns only move "up" one space
# black pawns only move "down" one space
# other chess pieces move normally
def printValidMoves(cp):
    print("\t  ", cp.pic(), "at", cp.location())
    for i in range(7, -1, -1):
        print("\t" + str(i) + " ", end="")
        for j in range(0, 8):
            if cp.x() == j and cp.y() == i:
                print(cp.pic() + " ", end="")
            elif cp.validMove(j, i):
                print("* ", end="")
            else:
                print(". ", end="")
        print()
    print("\t  ", end="")
    for i in range(0, 8):
        print(str(i) + " ", end="")
    print()
    print()


# returns a random chess piece at a random location
# each of these types must inherit from ChessPiece
def randomChessPiece():
    if random.randint(0, 1) == 0:
        c = "w"
    else:
        c = "b"
    t = random.randint(1, 6)
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    if t == 1: return Pawn(c, x, y)
    if t == 2: return Queen(c, x, y)
    if t == 3: return King(c, x, y)
    if t == 4: return Rook(c, x, y)
    if t == 5: return Knight(c, x, y)
    else: return Bishop(c, x, y)


def main():
    clist = []

    # make a list of random chess pieces
    for i in range(0, 10):
        clist.append(randomChessPiece())

    # display thier valid moves
    for i in range(0, len(clist)):
        # behold! polymorphism works!
        printValidMoves(clist[i])


main()
