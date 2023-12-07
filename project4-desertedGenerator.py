# engine state variables
oilLevel = 0
fuelLevel = 0
fuelCutOff = True
throttleAdvance = False
engineRunning = False
choke = False
lightsOn = False
generatorEngage = False
breakerEngage = False
electricity = False
printStatus = True
printMenu = True
done = False

# main event loop
while not done:
    if printStatus:
        # print the status
        print("\n")
        print(format("Oil Level:",">33s"),end="  ")
        print(oilLevel,end="")
        if(oilLevel==3): print(" >>FULL<<")
        elif(oilLevel==1): print(" >>LOW<<")
        elif(oilLevel==0): print(" >>EMPTY<<")
        else:print()
    
        print(format("Fuel Level:",">33s"),end="  ")
        print(fuelLevel,end="")
        if(fuelLevel==5): print(" >>FULL<<")
        elif(fuelLevel==1): print(" >>LOW<<")
        elif(fuelLevel==0): print(" >>EMPTY<<")
        else:print()
    
        print(format("Throttle:",">33s"),end="  ")
        if(throttleAdvance): print("advanced")
        else: print("not advanced")
    
        print(format("Choke:",">33s"),end="  ")
        if(choke): print("engaged")
        else: print("not engaged")
    
        print(format("Fuel Cutoff:",">33s"),end="  ")
        if(fuelCutOff): print("fuel off")
        else: print("fuel on")

        print(format("Generator:", ">33s"), end="  ")
        if (generatorEngage):
            print("engaged")
        else:
            print("not engaged")

        print(format("Breaker:", ">33s"), end="  ")
        if (breakerEngage):
            print("engaged")
        else:
            print("not engaged")
    
        print(format("The engine is:",">33s"),end="  ")
        if(not engineRunning):print(">>Not Running<<")
        elif(throttleAdvance): print(">>At Speed<<")
        else:print(">>At Idle<<")

        print(format("The generator is:", ">33s"), end="  ")
        if (generatorEngage): print(">>Spinning<<")
        else:
            print(">>Not Spinning")

        print(format("The lights are:", ">33s"), end="  ")
        if (breakerEngage):
            print(">>On<<")
        else:
            print(">>Off<<")
        printStatus = False
    
    if(printMenu):
        # print the menu
        print("")
        print(format("\ts - starter button","<34s"),end="    ")
        print(format("f - add diesel fuel","<34s"))
        print(format("\tt - advance/retard throttle","<34s"),end="    ")
        print(format("o - add oil","<34s"))
        print(format("\tb - engage breaker", "<34s"), end="    ")
        print(format("c - choke on/off", "<34s"))
        print(format("\tg - engage generator", "<34s"), end="    ")
        print(format("w - wait","<34s"))
        print(format("\tv - fuel cutoff valve open/closed","<34s"),end="    ")
        print(format("q - quit","<34s"))
        print("")
        print(format("\tp - panel ","<34s"),end="    ")
        print(format("m - menu","<34s"))

        printMenu = False
     
    # get response
    print("")
    r = input("action: ")
    while(r!='s' and r!='t' and r!='f' and r!='c' and 
          r!='o' and r!='v' and r!='w' and r!='q' and
          r!='p' and r!='m' and r!='g' and r!='b'):
        print("huh?")
        r = input("action: ")

    if(r=='s'):
        print("You punch the starter button.")
        if(engineRunning):
            print("You hear the starter grind into the running engine, then release.")
        else:
            if(oilLevel<1):
                print("You hear the pistons scraping in their cylinders.")
                print("The engine refuses to turn.")
            elif(fuelLevel==0):
                print("You hear the engine turning, but it won't fire up.")
            elif(fuelCutOff):
                print("You hear the engine turning, but it won't fire up.")
            elif(not choke):
                print("You hear the engine turning, but it won't fire up.")
            elif(throttleAdvance):
                print("You hear the engine turning, but it won't fire up.")
            else:
                engineRunning = True
                print("The engine sputters to life!")


    if(r=='t'):
        if(throttleAdvance):
            throttleAdvance = False
            print("You back off the throttle.")
            if(engineRunning):
                print("The engine drops to idle.")
                if (generatorEngage):
                    engineRunning = False
                    print("The engine sputters and dies.")
                    print("The generator shuts off.")
                    generatorEngage = False
                    electricity = False
                    if(breakerEngage):
                        breakerEngage = False
                        print("The breaker flips and the lights shut off.")

        else:
            print("You advance the throttle.")
            throttleAdvance = True
            if(choke and engineRunning):
                engineRunning = False
                print("The engine sputters and dies.")
                if (generatorEngage):
                    print("The generator shuts off.")
                    generatorEngage = False
                    electricity = False
                    if (breakerEngage):
                        breakerEngage = False
                        print("The breaker flips and the lights shut off.")
            elif(engineRunning):
                print("The engine revs up to operating speed.")


    if(r=='f'):
        if(fuelLevel<5):
            fuelLevel+=1
            print("You pour in a gallon of diesel fuel.")
        else:
            print("The tank is already full.")

    if(r=='c'):
        if(choke):
            choke = False
            print("You disengage the engine choke.")
        else:
            choke = True
            print("You engage the engine choke.")
            if(engineRunning and throttleAdvance):
                engineRunning = False
                print("The engine sputters and dies.")
                if (generatorEngage):
                    print("The generator dies too.")
                    generatorEngage = False
                    electricity = False
                    if (breakerEngage):
                        breakerEngage = False
                        print("And also the lights.")
            

    if(r=='o'):
        if(oilLevel<3):
            oilLevel+=1
            print("You put in a quart of oil.")
        else:
            print("The oil reservoir already is full.")


    if(r=='v'):
        if(fuelCutOff):
            fuelCutOff = False
            print("You set the Fuel Cutoff Valve to \"fuel on\".")

        else:
            fuelCutOff = True
            print("You set the Fuel Cutoff Valve to \"fuel off\".")
            if(engineRunning):
                engineRunning = False
                print("After a few moments, the engine sputters and dies.")
                if (generatorEngage):
                    print("The generator dies too.")
                    generatorEngage = False
                    electricity = False
                    if (breakerEngage):
                        breakerEngage = False
                        print("...And also the lights.")
    if(r=='w'):
        print("You sit in the console chair to monitor the gauges.")
        print("But it is pretty boring and you soon drift off to sleep.")
        print("Zzzz....")
        if(engineRunning):
            if(oilLevel>0):oilLevel-=1
            if(fuelLevel>0):fuelLevel-=1
            if(oilLevel==0 or fuelLevel==0):
                engineRunning = False
                print("After an hour, you awake with a start!")

                if(oilLevel ==0): print("The engine screeches to a halt.")
                if (generatorEngage):
                    print("The generator shuts off.")
                    generatorEngage = False
                    electricity = False
                    if (breakerEngage):
                        breakerEngage = False
                        print("The lights shut off.")
                else: print("The engine sputters and dies.")
                if (generatorEngage):
                    print("The generator dies too.")
                    generatorEngage = False
                    electricity = False
                    if (breakerEngage):
                        breakerEngage = False
                        print("...And also the lights.")


            else:
                print("You wake up after an hour.")
                print("Everything appears to be operating normally.")
        else:
            print("You wake up after an hour.")
            print("The engine has miraculously not started itself during your nap.")

    if(r=='g'):
        if(generatorEngage):
            generatorEngage=False
            print("You shut off the generator.")
            if (breakerEngage):
                breakerEngage = False
                print("The breaker flips and the lights shut off.")
        elif(engineRunning and throttleAdvance):
            generatorEngage = True
            electricity = True
            print("The generator rumbles to life!")
        elif(not throttleAdvance and engineRunning):
            engineRunning = False
            print("You just killed the engine. Great.")
        else:
            print("You click the switch but nothing happens. Maybe try something else first?")

    if (r=='b'):
        if (breakerEngage):
            breakerEngage = False
            print("The lights shut off.")
        elif(generatorEngage):
            print("The lights flicker on.")
            breakerEngage = True
        else:
            print("The switch flips back off. Nothing happens.")


    if(r=='q'): 
        print("quitting...")
        done = True

    if(r=='p'): printStatus = True

    if(r=='m'): printMenu = True

    



