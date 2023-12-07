
class Artomat:
    def __init__(self, text1, text2, text3, text4, bin1=10, bin2=10, bin3=10, bin4=10, money=0, hopper=0):
        self.__bin1 = bin1
        self.__bin2 = bin2
        self.__bin3 = bin3
        self.__bin4 = bin4
        self.__text1 = text1
        self.__text2 = text2
        self.__text3 = text3
        self.__text4 = text4
        self.__money = money
        self.__hopper = hopper

#what's in the machine
    def printStatus(self):
        print()
        print("1:", self.__bin1, "packs of", self.__text1)
        print("2:", self.__bin2, "packs of", self.__text2)
        print("3:", self.__bin3, "packs of", self.__text3)
        print("4:", self.__bin4, "packs of", self.__text4)
        print("There is $", "%.2f"%(self.__money *0.25),"in the machine.")
        print("There is $", "%.2f"%(self.__hopper *0.25),"in the hopper.")
        print()


    def dropQuarter(self):
        print("ching")
        self.__hopper+=1


    #dispense the art from the right bins
    def pullKnob(self, knobNum):
        if self.__hopper < 3:
            print("(nothing happens)")
            return
        if knobNum == 1 and self.__bin1 > 0:
            print("A pack of", self.__text1, "slides into view.")
            self.__bin1 -= 1
            self.__money += self.__hopper
            self.__hopper = 0
        elif knobNum == 2 and self.__bin2 > 0:
            print("A pack of", self.__text2, "slides into view.")
            self.__bin2 -= 1
            self.__money += self.__hopper
            self.__hopper = 0
        elif knobNum == 3 and self.__bin3 > 0:
            print("A pack of", self.__text3, "slides into view.")
            self.__bin3 -= 1
            self.__money += self.__hopper
            self.__hopper = 0
        elif knobNum == 4 and self.__bin4 > 0:
            print("A pack of", self.__text4, "slides into view.")
            self.__bin4 -= 1
            self.__money += self.__hopper
            self.__hopper = 0


    def restock(self):
        print("A grouchy-looking attendant shows up, opens the back, fiddles around a bit, closes it, and leaves.")
        self.__bin1 = 10
        self.__bin2 = 10
        self.__bin3 = 10
        self.__bin4 = 10
        self.__hopper = 0
        self.__money = 0


# write your class definition above this line
# make no changes below this line

def main():
    photoMachine = Artomat(text1="Adams",text2="Arbus",text3="Dali",text4="Lange")
    portraitMachine = Artomat(money=212,hopper=2,bin1=1,bin2=0,bin3=8,bin4=10,text1="Picasso",text2="Rembrandt",text3="Van Gogh",text4="Monet")

    photoMachine.printStatus()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.pullKnob(1)
    photoMachine.pullKnob(2)
    photoMachine.dropQuarter()
    photoMachine.pullKnob(2)
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.pullKnob(2)
    photoMachine.printStatus()
    photoMachine.restock()
    photoMachine.printStatus()
    print("----")
    portraitMachine.printStatus()
    portraitMachine.dropQuarter()
    portraitMachine.pullKnob(1)
    portraitMachine.printStatus()


main()
