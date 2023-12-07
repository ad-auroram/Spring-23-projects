import random

def verb():
    v=random.randint(1,10)
    if v == 1: return "Slay"
    if v == 2: return "Retrieve"
    if v == 3: return "Fight"
    if v == 4: return "Travel to"
    if v == 5: return "Steal"
    if v == 6: return "Search for"
    if v == 7: return "Listen to"
    if v == 8: return "Run from"
    if v == 9: return "Sneak to"
    if v == 10: return "Speak with"

def adjective():
    a = random.randint(1,10)
    if a == 1: return "hidden"
    if a == 2: return "ancient"
    if a == 3: return "dark"
    if a == 4: return "mysterious"
    if a == 5: return "enchanted"
    if a == 6: return "illusive"
    if a == 7: return "iridescent"
    if a == 8: return "celestial"
    if a == 9: return "infernal"
    if a == 10: return "whispering"

def noun():
    n = random.randint(1,10)
    if n == 1: return "goose."
    if n == 2: return "book."
    if n == 3: return "goblin."
    if n == 4: return "tree."
    if n == 5: return "dragon."
    if n == 6: return "castle."
    if n == 7: return "sword."
    if n == 8: return "amulet."
    if n == 9: return "forest."
    if n == 10: return "king."



def main():
    print("\n\nFantasy Adventure Instruction Generator\n")
    for i in range (1,11):
        print(i,"-",verb(),"the",adjective(),noun(),end="\n")
    print("\n\n")

main()