import random
import json

with open("database.json", "r") as db:
    x = json.load(db)

def start(ID):
    global x

    Ref = {
    "isaac" : [["Win the run starting as Eden", "Win the run starting as Isaac", "Win the run starting as Cain", "Win the run starting as Lazarus", "Win the run starting as Maggi", "Win the run starting as The Keeper", "Win the run starting as ???", "Win the run starting as forgotten", "Win the run starging as judas"],["No devil deals; only angel deals: beat the Chest", "No angel deals; Only devil deals: Beat the dark room", "Beat the boss rush; if you cannot make it to bosh rush you do not get points for this challenge; beat the chest", "Beat Hush; If you cannot make it to Hush, you do not get points for this challenge; Beat the dark room", "Skip two item room items; Beat the chest", "Skip a boss room item; Beat the chest", "Play on the VNKNOWN seed; Beat the chest", "Play on the GONESOON seed; beat the Chest", "Play on the KEEPTRAK seed; Beat the chest", "Using the debug console; Spawn both key pieces and beat mega satan", "Using the debug console; Spawn bob's brain and skip the first item room; Beat the dark room"]], 
    "bumbo" : [["Play as Bum-Bo the Brave;beat the third floor boss", "Play as Bum-Bo the Nimble; Beat the third floor boss", "Play as Bum-Bo the stout; Beat the third floor Boss", "Play as Bum-Bo the weird; Beat the third floor"],["Finish with atleast 1 soul heart", "Match at least 7 combos", "skip two spells in item rooms", "Do not spend any coins in the second casino", "Flawless a boss", "Finish without upgrading spells in the casino", "Go down half a heart at least once on the run", "Never have more than 3 poops out at a given time"]],
    "crypt" : [["Literally just see the first boss with any character but the Bard"], ["Do not buy items from any shop", "Do not let the floor song end"]],
    "dead cells" : [["Beat the Concierge and time keeper on 0 boost cells", "Beat Conjonctivius and Time Keeper on 0 boss cells"], ["You must carry a shield at all times", "You must not carry any grenades", "You cannot buy items from in-level shops", "Pick surival *green* for 5 or more scrolls", "After picking up your first bow; you cannot drop a bow", "Kill 50+ enemies in a row without getting hit", "Do not refill your health flask twice", "Carry a starting item through at least two floors"]],
    "dicey" : [["Win an Episode 1 run as the Warrior", "Win an Episode 1 run as the Thief", "Win an episode 1 run as the robot", "Win an Episode 1 run as the inventor", "Win an episode 1 run as the Witch", "Win an Episode 1 run as the Jester"], ["Insread of episode 1; Play episode 2", "Do not use any anvils", "At least one fight oer floor, have an open slot in your inventory", "Use every equipment you receive at least once", "Keep the first poison equipment you receive in your inventory", "Keep the first block equipment you receive in your inventory", "Keep the first attack equipment you receive in your inventory", "Keep the first healing equipment you receive in your inventory", "Leave a fight you start three times", "Do not spend any money in shops", "Leave at least one apple on the floor if there is at least one"]],
    "gungeon" : [["Beat the Dragun as the gunslinger", "Beat the dragun as the paradox",  "Beat the dragun as Convict", "Beat the dragun as hunger", "Beat the dragun as Marine", "Beat the dragun as the Robot", "Beat the dragun as pilot", "Beat the dragun as the Bullet"],["Beat the past of the character you are playing", "Spend as much money as you can each floor", "cannot buy keys in the shop", "Must use all blanks upon entering a new floor", "Do not buy any items from the shop", "Skip any two chests", "recieve three master rounds", "Have a total of 8 HP at some point(Hearts and armor Included)", "Do not use Blanks in boss fights", "You cannot open blue chests", "Drop a master round on the ground and leave it", "must visit every room one very floor"]],
    "sor" : [["Reach 3-1 as the Doctor", "Reach 3-1 as the gangster", "Reach 3-1 as the Hacker", "Reach 3-1 as the slum dweller", "Reach 3-1 as the soldier", "Reach 3-1 as the thief"],["Complete all optional quests", "free all people you see in locked doors", "Spend all money you can on each floor", "Get a cop to kill someone on one level", "Do not take anything from trash cans", "Do not use any guns", "Infect two filtration systems", "Bust an NPC through a wall", "Win a slot machine", "Do not use Sell-O-Matics"]],
    "spelunky" : [["Beat Olmec playing as the Blue guy", "Beat Olmec playing as the Browny dude who looks like a miner", "Beat Olmec playing as the guy with red clothing", "Beat Olmec playing as the green girl"], ["Ghost ay least 1 gem on the run", "Do not pick up a shotgun on the run", "kill a shopkeeper", "go to the worm level", "visit the black market", "Spend 4+ minutes on one floor", "do not use a jetpack", "Pick up at least two of these treasures, Yellow looks like a man", "Finish with a score of 300,000 or more", "Beat Olmec while still holding the Ankh", "Finish with 10+ bombs in your inventory"]],
    "spire" : [["Win a run as the Ironclad", "Win a run as the silent", "win a run as the defect", "Win a run as the Watcher"], ["Play on Ascension 0; Figjt as many elites on floor 1 as possible", "Play on ascension 0; you must pick up 3 key pieces", "Play on ascension 0; Using the custom mode; enable Praise Snecko", "Play on ascension 0; Using the custom mode; enable Diverse", "Play on ascension 0; Using the custom mode; enable My True Form", "Play on ascension 0; Using the custom mode; enable terminal", "Play on ascension 0; You must skip 1 relic froma  treasure chest or boss fight", "Play on ascension 0; You must finish the run with 30 or more cards", "Play on ascension 0; you must finish the run with 18 or less cards", "Play on ascension 0; You must finish the run wtih 0 basic strikes", "Play on ascension 0; You must finish the run with over half your cards being attacks", "Play on ascension 0; using the custom mode; enable Cursed"]]
    }
    Games = ["isaac", "bumbo", "crypt", "dead cells", "dicey", "gungeon", "sor", "spelunky", "spire"]
    RandGames = []
    Challenges = {}

    status =  x[ID]["status"]
    if status != "":
        print("Game in progres, would you like to quit the game? Y/N")
        if YorN():
            print("Resetting game.")
            ClearUsr(ID)
        else:
            print("Continue your game")
            return 0

    for p in range(0, 5):       # Choses 5 random games from Games
        i = random.randint(0, len(Games) - 1)
        RandGames.append(Games[i])
        Games.pop(i)

    for y in RandGames:         # Assigns random challenges to the games and makes a dictionary Challenges: {Game : [Main challenge, secondary challenge]}
        Dic = Ref[y]
        Main = random.randint(0, len(Dic[0])- 1)
        Sub = random.randint(0, len(Dic[1])- 1)
        
        Challenges[y] = [(Dic[0][Main]), (Dic[1][Sub])]

    print("The following games and challenges have been generated: ")   # Prints all the games and challenges
    for y in Challenges:
        Temp = Challenges[y]
        print(f"Game: {y}: {Temp[0]}, {Temp[1]}")

    Ordered = {}

    game_picks = ["first", "second", "third", "fourth", "fifth"]

    for pick in game_picks:
        print("Which game would you like to play " + pick + "?")
        while True:
            i = input().lower()
            if i not in Challenges:
                print("Game not found, Check your spelling.")
            else:
                Ordered[i] = Challenges[i]
                Challenges.pop(i)
                break

    print("These are the games you have selected:")
    for i in Ordered:
        Temp = Ordered[i]
        print(f"Game: {i}: {Temp[0]}, {Temp[1]}")

    x[ID]["games"] = Ordered
    x[ID]["status"] = "Game set up"
    with open("database.json", "r+") as db:
        json.dump(x, db)

def CheckUsr(ID):
    global x

    if ID in x:
        print("User in DB")

    else:
        print("Adding user to DB")
        data = {
            "games" : {},
            "progress" : 0,
            "status" : "",
            "score" : 0,
            "failed" : [],
            "highscore" : 0,
            "results" : {
                "game 1" : [],
                "game 2" : [],
                "game 3" : [],
                "game 4" : []}
            }

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
    data["results"] = {
        "game 1" : [],
        "game 2" : [],
        "game 3" : [],
        "game 4" : []}
    x[ID] = data
    with open("database.json", "w") as db:
        json.dump(x, db)

def play(ID):
    data = x[ID]
    progress = data["progress"] #int progress, 0 = no games played, 1 = 1 games played, etc
    status = data["status"] #str status
    games = data["games"] #dictionary Games

    if status == "" or "Playing" in status:
        print("Cant start a game right now, use !status to see your current state")
        return

    game_picks = ["first", "second", "third", "fourth", "fifth"]

    if progress >= 0 and progress <= 4:
        game = [element for element in games]

        print("Your " + game_picks[progress] + f" game is: {game[0]}, With challenges: {games[game[progress]][0]} & {games[game[progress]][1]}")
        print("Do you wanna start the " + game_picks[progress] + " game? Y/N")

        while True:
            inpt = input().lower()

            if inpt == "y":
                print("Game " + str(progress) + " started, when youre done, use !update to update your score. For a status check, use !status")
                status = "Playing game " + str(progress)
                data["status"] = status
                x[ID] = data
                with open("database.json", "w") as db:
                    json.dump(x, db)
                return 0

            elif inpt == "n":
                print("When you wanna play, use !play")
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

def YorN():
    while True:
        Inpt = input().lower()
        if Inpt == "y":
            return True
        elif Inpt == "n":
            return False
        else:
            print("unknown input")

def update(ID):
    global x

    data = x[ID]
    status = data["status"]
    games = data["games"]
    game = [element for element in games]
    results = data["results"]
    progress = data["progress"]

    
    if status == "Playing game 1":
        print("Have you finished playing your first game? Y/N")
        B = YorN()
        if B == False:
            print("Use !update when you finished your game.")
            return 0
        print(f"Your first game was{game[0]}, Did you complete your main challenge: {games[game[0]][0]}? Y/N.")
        B = YorN()
        if B == True:
            results["game 1"].append(True)
            print(f"Did you complete the additional challenge, {games[game[0]][1]}")
            I = YorN()
            if I == True:
                results["game 1"].append(True)
                print("Game 1 finished flawlessly, use !play to start the second game")
            if I == False:
                results["game 1"].append(False)
                print("Game 1 finished, use !play so start the second game")
        if B == False:
            print("Game 1 fully failed, use !play to start the second game")
            results["game 1"].append(False)
            results["game 1"].append(False)

        status = "ready"
        progress = 1
    elif status == "Playing game 2":
        return 0
    elif status == "Playing game 3":
        return 0
    elif status == "Playing game 4":
        return 0
    elif status == "Playing game 5":
        return 0
   
    data["status"] = status
    data["games"] = games
    data["results"] = results
    data["progress"] = progress
    x[ID] = data

    with open("database.json", "w") as db:
        json.dump(x, db)

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