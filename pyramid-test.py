import random
import json

with open("database.json", "r") as db:
    x = json.load(db)

def start(ID): 
    Ref = {
    "rocket league" : [["Win a game", "Get 3 goals", "Get 2 saves"],["play with the dominus", "play with the egg", "get a flip reset"]], 
    "xplane" : [["fly the a320", "fly the 737"],["fly to eham", "fly to egll"]],
    "csgo" : [["Win a game of casual", "win a game of competetive"], ["Get an AWP kill", "get first or second on the leaderboard"]],
    "subnautica" : [["Get a cyclops", "make a battery"], ["Don't drown", "dont equip any air thanks"]],
    "sor" : [["Play with the doctor", "play with the ninja"], ["Don't take any damage", "No ranged weapons"]],
    "steep" : [["win a race using skis", "Win a race with a snowboard"],["Do a backflip", "do a 360"]]
    }
    Games = ["rocket league", "xplane", "csgo", "subnautica", "sor", "steep"]
    RandGames = []
    Challenges = {}

    global x

    status =  x[ID]["status"]
    if status != "":
        print("Game in progres, would you like to quit the game? Y/N")
        inpt = input().lower()
        if inpt == "y":
            print("Resetting game.")
            ClearUsr(ID)
        else: 
            print("Continue your game")
            return 0

    for p in range(0, 5):      # Choses 5 random games from Games
        i = random.randint(0, len(Games) - 1)
        RandGames.append(Games[i])
        Games.pop(i)

    for y in RandGames: # assigns random challenges to the games and makes a dictionary Challenges: {Game : [Main challenge, secondary challenge]}
        Dic = Ref[y]
        Main = random.randint(0, len(Dic[0])- 1)
        Sub = random.randint(0, len(Dic[1])- 1)
        
        TempList = [(Dic[0][Main]), (Dic[1][Sub])]
        TempDic = {}
        TempDic[y] = TempList
        Challenges.update(TempDic)

    print("The following games and challenges have been generated: ")   #prints all the games and challenges
    for y in Challenges:
        Temp = Challenges[y]
        print("Game: ", y,", ", Temp[0], ", ", Temp[1])

    Ordered = {}

    print("Which game would you like to play first?")

    while True:
        i = input().lower()
        if i not in Challenges:
            print("Game not found, Check your spelling.")
        else:
            TempList = {}
            TempList[i] = Challenges[i]
            Ordered.update(TempList)
            Challenges.pop(i)
            break


    print("Which game would you like to play second?")
    while True:
        i = input().lower()
        if i not in Challenges:
            print("Game not found, Check your spelling.")
        else:
            TempList = {}
            TempList[i] = Challenges[i]
            Ordered.update(TempList)
            Challenges.pop(i)
            break


    print("Which game would you like to play third?")
    while True:
        i = input().lower()
        if i not in Challenges:
            print("Game not found, Check your spelling.")
        else:
            TempList = {}
            TempList[i] = Challenges[i]
            Ordered.update(TempList)
            Challenges.pop(i)
            break


    print("Which game would you like to play fourth?")
    while True:
        i = input().lower()
        if i not in Challenges:
            print("Game not found, Check your spelling.")
        else:
            TempList = {}
            TempList[i] = Challenges[i]
            Ordered.update(TempList)
            Challenges.pop(i)
            break

    print("Which game would you like to play fifth?")
    while True:
        i = input().lower()
        if i not in Challenges:
            print("Game not found, Check your spelling.")
        else:
            TempList = {}
            TempList[i] = Challenges[i]
            Ordered.update(TempList)
            Challenges.pop(i)
            break


    print("These are the games you have selected:")
    for i in Ordered:
        Temp = Ordered[i]
        print("Game: ", i,", ", Temp[0], ", ", Temp[1])

    data = x[ID]
    data["games"] = Ordered
    data["status"] = "Game set up"
    x[ID] = data
    with open("database.json", "r+") as db:
        json.dump(x, db)

def CheckUsr(ID):
    global x
    if ID in x:
        print("User in DB")
    else:
        print("adding user to DB")
        data = {
    "games" : {},
    "progress" : 0,
    "status" : "",
    "score" : 0,
    "failed" : [],
    "highscore" : 0}

        x[ID] = data
        with open("database.json", "w") as db:
            json.dump(x, db)

def ClearUsr(ID):
    global x
    data = x[ID]
    data["games"] = {}
    data["progress"] = 0
    data["status"] = ""
    data["score"] = 0
    data["failed"] = []
    x[ID] = data
    with open("database.json", "w") as db:
        json.dump(x, db)

def play(ID):
    data = x[ID]
    progress = data["progress"] #int progress, 0 = no games played, 1 = 1 games played, etc
    status = data["status"] #str status
    games = data["games"] #dictionary Games

    if status == "":
        print("Set up a game first using !start")
        return 0
    elif status == "finished":
        print("All games played, view results using !finish")
        return 0
    
    if progress == 0:
        game = [element for element in games]
        print(f"Your first game is: {game[0]}, With challenges: {games[game[0]][0]} & {games[game[0]][1]}")
        print("Do you wanna start the firt game? Y/N")
        y = 0
        while y == 0:
            inpt = input().lower()
            if inpt == "y":
                print("Game 1 started, when youre done, use !update to update your score. For a status check, use !status")
                status = "Playing game 1"
                data["status"] = status
                x[ID] = data
                with open("database.json", "w") as db:
                    json.dump(x, db)
                y += 1
                return 0
            if inpt == "n":
                print("When you wanna play, use !play")
                y += 1
                return 0
            else:
                print("Unknown input, Y/N")

    if progress == 1:
        game = [element for element in games]
        print(f"Your second game is: {game[1]}, With challenges: {games[game[1]][0]} & {games[game[1]][1]}")
        print("Do you wanna start the second game? Y/N")
        y = 0
        while y == 0:
            inpt = input().lower()
            if inpt == "y":
                print("Game 2 started, when youre done, use !update to update your score. For a status check, use !status")
                status = "Playing game 2"
                data["status"] = status
                x[ID] = data
                with open("database.json", "w") as db:
                    json.dump(x, db)
                y += 1
                return 0
            if inpt == "n":
                print("When you wanna play, use !play")
                y += 1
                return 0
            else:
                print("Unknown input, Y/N")
    if progress == 2:
        game = [element for element in games]
        print(f"Your third game is: {game[2]}, With challenges: {games[game[2]][0]} & {games[game[2]][1]}")
        print("Do you wanna start the third game? Y/N")
        y = 0
        while y == 0:
            inpt = input().lower()
            if inpt == "y":
                print("Game 3 started, when youre done, use !update to update your score. For a status check, use !status")
                status = "Playing game 3"
                data["status"] = status
                x[ID] = data
                with open("database.json", "w") as db:
                    json.dump(x, db)
                y += 1
                return 0
            if inpt == "n":
                print("When you wanna play, use !play")
                y += 1
                return 0
            else:
                print("Unknown input, Y/N")
    if progress == 3:
        game = [element for element in games]
        print(f"Your fourth game is: {game[3]}, With challenges: {games[game[3]][0]} & {games[game[3]][1]}")
        print("Do you wanna start the fourth game? Y/N")
        y = 0
        while y == 0:
            inpt = input().lower()
            if inpt == "y":
                print("Game 4 started, when youre done, use !update to update your score. For a status check, use !status")
                status = "Playing game 4"
                data["status"] = status
                x[ID] = data
                with open("database.json", "w") as db:
                    json.dump(x, db)
                y += 1
                return 0
            if inpt == "n":
                print("When you wanna play, use !play")
                y += 1
                return 0
            else:
                print("Unknown input, Y/N")
    if progress == 4:
        game = [element for element in games]
        print(f"Your fifth game is: {game[4]}, With challenges: {games[game[4]][0]} & {games[game[4]][1]}")
        print("Do you wanna start the fifth game? Y/N")
        y = 0
        while y == 0:
            inpt = input().lower()
            if inpt == "y":
                print("Game 4 started, when youre done, use !update to update your score. For a status check, use !status")
                status = "Playing game 4"
                data["status"] = status
                x[ID] = data
                with open("database.json", "w") as db:
                    json.dump(x, db)
                y += 1
                return 0
            if inpt == "n":
                print("When you wanna play, use !play")
                y += 1
                return 0
            else:
                print("Unknown input, Y/N")
    else:
        print("Fatal error, talk to OrbitalPeriod#1771")

def status(ID):
    global x

    data = x[ID]
    games = data["games"]
    status = data["status"]
    score = data["score"]
    failed = data["failed"]
    game = [element for element in games]

    if status == "": #WIP until after !update
        print("no game set up")
        return 0
    elif status == "Game set up":
        print("Game set up, not playing right now.\n", f"Your next game will be {game[0]}, with challenges {games[game[0]][0]} & {games[game[0]][1]}.")
        return 0

def update(ID):
    global x

    data = x[ID]
    status = data["status"]

    if status == "Playing game 1" or status == "Playing game 2" or status == "Playing game 3" or status == "Playing game 4" or status == "Playing game 5":
        if status == "Playing game 1":
            return 0
        elif status == "Playing game 2":
            return 0
        elif status == "Playing game 3":
            return 0
        elif status == "Playing game 4":
            return 0
        elif status == "Playing game 5":
            return 0

    else:
        print("Not in game right now, use !start to set up a game and !play to start a game")

def Main():
    ID = input().lower()
    CheckUsr(ID)

    while True:
        x = input().lower()
        if x == "!start": #starts Start()
            start(ID)
        if x == "!play": #starts play()
            play(ID)
        if x == "!clear": #starts the clear function
            y = 0
            while y == 0:
                print("You sure you want to clear your current game? Y/N")
                x = input().lower()
                if x == "y":
                    print("Clearing game")
                    ClearUsr(ID)
                    print("Game cleared...")
                    y = 1
                elif x == "n":
                    print("Roger")
                    y = 1
                else:
                    print("Unknown input; Y/N")
        if x == "!status":
            status(ID) 
        if x == "!update":
            update(ID)


Main()