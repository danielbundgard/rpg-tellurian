#Author: Daniel Bundgard
#Date: 2019-01-08
#Description: This game is a text-based role playing game where the player will encounter different obstacles and people where he/she will have to choose their own path.

#Import stuff
import sys
import time
#Game items
objectsword = False
knife = False
name = ("Jerome")

#Title
print(" _______   _ _            _             ")
print("|__   __| | | |          (_)            ")
print("   | | ___| | |_   _ _ __ _  __ _ _ __  ")
print("   | |/ _ \ | | | | | '__| |/ _` | '_ \ ")
print("   | |  __/ | | |_| | |  | | (_| | | | |")
print("   |_|\___|_|_|\__,_|_|  |_|\__,_|_| |_|")
time.sleep(2)
#Introduction
print("You are a man walking down a country lane. You have no memory of your life other than a small coin in your pocket. As you walk, you stumble upon a small earpiece. You  pick it up and put it in your ear and it begans speaking.")


def Chainsaw(): #if QB3 == 2 or QA3 == 1:
    print ("you began to see the outline of the town in the distance. It is bigger than you thought, but looks empty. All you hear is silence.")
    print ("All of a sudden, a man appears in front of you. He in holding a chainsaw. He tries to say something but you cant hear. What do you do?")
    print ("1. Hear him out 2. run away") #Options
    Q4 = int(input())
    if Q4 == 1:
        print ("He turns off the chainsaw and says - count to five. (seperate each number by a space, ex: 1 2... 5)")
        a = [int(s) for s in input().split()] #Input for the list
        #
        if a == [1, 2, 3, 4, 5]: #Lived
            print("Hi im harriay, sorry if a scared you, just had to make sure you werent a zombEE")
        else:
            print("Haha you're dead.") #Died
            print("The man cuts you in half and you die.")
            time.sleep(3)
            endGameBad()
            restart()
    else: 
        print ("The man catches you and cuts you in half. You bleed out.") #If use wants to run away, they die
        time.sleep(2)
        endGameBad()
        restart()
def LeavingThePath():        #else:#(QA3 == 2)
    print("Your finger begans to throb with pain. You walk into the forest your left hand side of the road to look for some water. You come across some mushrooms and realize you are very hungry. Eat mushrooms?(Y/N)")
    Q5 = input()
    if Q5 == 'Y' or Q5 == 'y':
        global objectsword
        global QA5
        print("You eat the mushrooms, they taste amazing. You continue to find a fresh pool of water to drink from. After drinking the water, you notice a strange object at the bottom of the pool. Swim down to grab it?(Y/N)")
        QA5 = input()
        if QA5 == 'Y' or QA5 == 'y':
            print ("You retreive the object, it appears to be a short sword.")
            print ("as you walk toward the road, you trip over your sword and kill yourself.")
            time.sleep(4)
            endGameBad()
            restart()
        else:
            print ("You look around for a long stick to fish out the object. you find two branches that look long enough to grab it.")
            print ("You reach the branches in and pull out the object. it is a sword.")
            print ("As you turn around, you see a man with a chainsaw in the distance.")
            print ("The man starts walking towards you, waving. You wave back to go talk to him")
            print ("--------")
            time.sleep(7)
            objectsword = True
        return objectsword
        return QA5
    else:
        print("You turn back towards the road, as you approach the road, something crawls through the bushes. You walk closer to investigate and a zombie jumps out at you. You try to fight it away but it bites your hand. You are now infected.")
        time.sleep(5)
        endGameBad()
        restart()
def ContinueToTown():
    print("You continue to the town.")
    print("The earpeice starts speaking again - Help, come quick traveller, they're everywhere, they're... - ")
    print("What would you like to do, 1. examine the earpeice 2. Take it out and crush it")
    QA3 = int(input())
    if QA3 == 1: #Earpeice is OK
        print("You examine the earpeice. You notice it has a small opening and you assume its for the microphone. It says made in China")
        print("What would you like to do,  1. try speaking into it 2. put it back in your ear")
        nothing = int(input())
        print ("You hear static and then continue on your way")
        Chainsaw()
    elif QA3 == 2: #Earpeice is crushed
        print("The earpeice releases smoke and then burns your finger tips. You continue on your way")
        LeavingThePath()
        #Break
def ContinueAwayFromTown():
    print("You start walking back the way you came, theres some blood on the side of the road")
    print("1. Investigate the blood splatter 2. Keep walking 3. Eat the blood")
    QB3 = int(input())
    if QB3 == 1:
        print("A zombie crawls out of the ditch and bites you. You are now infected")
        #break
        time.sleep(2)
        endGameBad()
        restart()
    elif QB3 == 2:
        print("You continue down the path")
        Chainsaw()
        #break
    else:
        print("The earpeice says - You're dumb - and you curl up and die")
        #break
        time.sleep(2)
        endGameBad()
        restart()
def HomelessMan():
    print("Oh look, a homless man. What would you like to do?")
    print("1. Kill him and take his items 2. Leave him alone 3. Hand him your coin.")
    Q2 = int(input())
    if Q2 == 1:
        print("You try to shove the coin down his throat, he bites off your fingers and beats you with a baseball.")
        time.sleep(3)
        endGameBad()
        restart()
    elif Q2 == 2:
        print("As you walk by, the man twitches.")
    else:
        print("He smiles at you, but says 'Keep it, you'll need it more.'")
def endGameBad():
    print("  _____          __  __ ______    ______      ________ _____  ")
    print(" / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ ")
    print("| |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |")
    print("| | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / ")
    print("| |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ ")
    print(" \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_]")
def endGameGood():
    print("__     ______  _    _  __          _______ _   _ ")
    print("\ \   / / __ \| |  | | \ \        / /_   _| \ | |")
    print(" \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |")
    print("  \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |")
    print("   | | | |__| | |__| |    \  /\  /   _| |_| |\  |")
    print("   |_|  \____/ \____/      \/  \/   |_____|_| \_|")
def dialogueWithChainsawMan():
    print("Its nice to meet you,", str(name))
    print("Its been years since ive seen another human.")
    print("YOU: What happened here?")
    print("Do you not know? Theres been an apocalypse, the town is completely overrun. I believe there is still some survivors hiding in the school.")
def Name():
    #First option to tell the travellers name
    global name
    global p
    print ("Hello ugly traveller, tell me, what is your name?")
    print ("Would you like to answer?(Y/N)")
    Q1 = str(input())
    if Q1 == "Y" or Q1 == "y":
        print("What is your name")
        name = str(input())
    elif Q1 == "N" or Q1 == "n":
        print("Alrighty then, keep your secrets")
def killman():
    print("Would you like to kill the chainsaw man?(Y/N)")
    Q6 = str(input())
    if Q6 == "Y" or Q6 == "y": #Yes kill man (DIE)
        print("You punch the man in the face, and then kick him in the groin. You then succed in killing him but look up to see a swarm of zombies coming at you from the city. they are moving fast.")
        print("What would you like to do? 1. Take chainsaw and fight 2. Run away")
        QA6 = int(input())
        if QA6 == 1: #die both ways unless sword
            if objectsword == False:
                print("You pick up the chainsaw and try to start it. It wont work. You try to run away but they're too fast. They catch you and kill you.")
                time.sleep(3)
                endGameBad()
                restart()
            else:
                print("You kill the chainsaw man with the sword and take his chainsaw. You then proceed to kill a swarm of zombies that came from the town")
        else: #die
            print("You run away as fast as you can. You almost escape but they still manage to catch you.")
            time.sleep(2)
            endGameBad()
            restart()
    else: #No kill man
        print("There's some zombies coming our way, here take my knife, youll need it.")
        knife = True
        time.sleep(2)
        print("*fighting*")
        time.sleep(2)
        print ("*still going*")
        time.sleep(2)
        print ("*Almost done..*")
        time.sleep(2)
def gotoSchool():
    print("The man leads you down a path in the forest.")
    time.sleep(1)
    print(".")
    time.sleep(1)    
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("")
def restart():
        endgameRestart = input("Would you like to play again? Please enter 'Y' for YES or 'N' for NO: ")
        if endgameRestart == "Y" or endgameRestart == "y":
            main()
        else:
            print ("Thanks for playing!")
            sys.exit()

def main():
    while True:
        Name()
        print("Well lets keep going, theres a town just around the corner")
        #Second option to kill homeless man
        HomelessMan()
        print ("Would you like to continue to the town?(Y/N)")
        Q3 = str(input())
        if Q3 == "Y" or Q3 == "y":
            ContinueToTown()
        else: #Q3 == "N" or Q3 == "n" #earpeice is ok
            ContinueAwayFromTown()
        dialogueWithChainsawMan()
        killman()
        print("Do you want to go to the school now?(Y/N)")
        Q7 = str(input())
        if Q7 == "Y" or Q7 == "y":
            gotoSchool()
        else:
            print("OK")
            time.sleep(1)
            print("Well theres no point letting you become a zombie.")
            print("the man kills you with your own knife.")
            time.sleep(2)
            endGameBad()
            restart()
        restart()


    
#common code to ensure main is only called when necessary    
if __name__ == "__main__":
    main()
