
def main():
    print("How's the cat going to react?")
    if input("Is it food? [y/n]: ") == "y":
        if input("From a can? [y/n]: ") == "y":
            print("Eat half.")
        else:
            print("Ignore it")
    #end of food branch
    elif input("Is it a cat tree? [y/n]: ") == "y":
        if input("Did it come in a box? [y/n]: ") == "y":
            print("Sit in the box.")
        else:
             print("Ignore it.")
    #end of cat tree branch
    elif input("Is it a human? [y/n]: ") == "y":
        if input("Does it want to pet me? [y/n]: ") == "y":
            print("Cough up a hairball.")
        else:
            print("Jump in its lap.")
    #end of human branch
    elif input("Is it a laptop? [y/n]: ") == "y":
        if input("In use? [y/n]: ") == "y":
            print("Lay on keyboard.")
        else:
            print("Knock it off the table.")
    else:
        print("Sleep")

main()