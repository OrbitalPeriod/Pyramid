import random
import json

db = open("database.txt", "w+")

Challenges = {}    
Games = {} 

def start(): 
    Ref = {
    "rocket league" : [["Win a game", "Get 3 goals", "Get 2 saves"],["play with the dominus", "play with the egg", "get a flip reset"]], 
    "xplane" : [["fly the a320", "fly the 737"],["fly to eham", "fly to egll"]],
    "csgo" : [["Win a game of casual", "win a game of competetive"], ["Get an AWP kill", "get first or second on the leaderboard"]],
    "subnautica" : [["Get a cyclops", "make a battery"], ["Don't drown", "dont equip any air thanks"]],
    "sor" : [["Play with the doctor", "play with the ninja"], ["Don't take any damage", "No ranged weapons"]]
    }
    Games = ["rocket league", "xplane", "csgo", "subnautica", "sor"]
    RandGames = []
  

    for x in range(0, 4):      # Choses 4 random games from Games
        i = random.randint(0, len(Games) - 1)
        RandGames.append(Games[i])
        Games.pop(i)

    for x in RandGames: # assigns random challenges to the games and makes a dictionary {Game : [Main challenge, secondary challenge]}
        Dic = Ref[x]
        Main = random.randint(0, len(Dic[0])- 1)
        Sub = random.randint(0, len(Dic[1])- 1)
        
        TempList = [(Dic[0][Main]), (Dic[1][Sub])]
        TempDic = {}
        TempDic[x] = TempList
        Challenges.update(TempDic)

    print("The following games and challenges have been generated: ")   #prints all the games and challenges
    for x in Challenges:
        Temp = Challenges[x]
        print("Game: ", x,", ", Temp[0], ", ", Temp[1])
    

    Ordered = {}

    print("Which game would you like to play first?")
    AddToOrdered(Challenges, Ordered)

    print("Which game would you like to play second?")
    AddToOrdered(Challenges, Ordered)

    print("Which game would you like to play third?")
    AddToOrdered(Challenges, Ordered)

    print("Which game would you like to play fourth?")
    AddToOrdered(Challenges, Ordered)

    print("These are the games you have selected:")
    for x in Ordered:
        Temp = Ordered[x]
        print("Game: ", x,", ", Temp[0], ", ", Temp[1])
    return Ordered

def AddToOrdered(Dic, Ordered): 
    y = 0
    while y == 0:
        x = input().lower()
        if x not in Dic:
            print("Game not found, Check your spelling.")
        else:
            TempList = {}
            TempList[x] = Dic[x]
            Ordered.update(TempList)
            y += 1
            Challenges.pop(x)
  
def Main():
    print("Whats your name?")
    x = input().lower()
    db.write(x)
    while True:
        x = input().lower()
        if x == "!start":
            Games = start()
        if x == "!play":
            play()
        
def play():
    print("weee")

Main()
        
        





