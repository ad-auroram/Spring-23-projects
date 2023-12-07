#Roxanne Seeley
#Section 02

class PiggyBank:
    def __init__(self, broken=False, balance=0.00):
        self.broken = broken
        self.balance = balance

#adding money
    def deposit(self, money):
        if self.broken == False:
            self.balance += money
        elif self.broken == True:
            self.balance+= 0

#breaking
    def smash(self):
        self.balance = 0.00
        self.broken = True

def printStatus(text,PiggyBank):
    if PiggyBank.broken == False:
        print(text,"has $","%.2f"%(PiggyBank.balance),"and is not broken.")
    elif PiggyBank.broken == True:
        print(text,"has $","%.2f"%(PiggyBank.balance), "and is broken.")

def main():
    p1 = PiggyBank()
    p2 = PiggyBank()
    printStatus("p1",p1)
    p1.deposit(1.25)
    printStatus("p1",p1)
    p1.deposit(6.55)
    printStatus("p1",p1)
    p1.smash()
    printStatus("p1",p1)
    p1.deposit(2.15)
    printStatus("p1",p1)
    p1.__balance=100.0
    p1.__broken=False
    printStatus("p1",p1)

main()