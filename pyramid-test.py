import random
import json
import datetime

with open("database.json", "r") as db:
    x = json.load(db)

def start(ID): 
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

    global x

    status =  x[ID]["status"]
    if status != "":
        print("Game in progres, would you like to quit the game? Y/N")
        B = YorN()
        if B == True:
            print("Resetting game.")
            ClearUsr(ID)
        elif B == False:
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
    "highscore" : {
        "Highscore" : 0,
        "time" : "",
        "cycle" : 1},
    "results" : {
        "game 0" : [0, 0],
        "game 1" : [0, 0],
        "game 2" : [0, 0],
        "game 3" : [0, 0],
        "game 4" : [0, 0]}
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
    data["results"] = {
        "game 0" : [0, 0],
        "game 1" : [0, 0],
        "game 2" : [0, 0],
        "game 3" : [0, 0],
        "game 4" : [0, 0]}
    x[ID] = data
    with open("database.json", "w") as db:
        json.dump(x, db)

def play(ID):
    data = x[ID]
    progress = data["progress"] #int progress, 0 = no games played, 1 = 1 games played, etc
    status = data["status"] #str status
    games = data["games"] #dictionary Games

    if status == "" or "Playing" in status or status == "Finished":
        print("Cant start a game right now, use !status to see your current state")
        return
    
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
        B = YorN()
        if B == True:
            print("Game 2 started, when youre done, use !update to update your score. For a status check, use !status")
            status = "Playing game 2"
            data["status"] = status
            x[ID] = data
            with open("database.json", "w") as db:
                json.dump(x, db)
            return 0
        if B == False:
            print("When you wanna play, use !play")
            return 0
    if progress == 2:
        game = [element for element in games]
        print(f"Your third game is: {game[2]}, With challenges: {games[game[2]][0]} & {games[game[2]][1]}")
        print("Do you wanna start the third game? Y/N")
        B = YorN()
        if B == True:
            print("Game 3 started, when youre done, use !update to update your score. For a status check, use !status")
            status = "Playing game 3"
            data["status"] = status
            x[ID] = data
            with open("database.json", "w") as db:
                json.dump(x, db)
            return 0
        if B == False:
            print("When you wanna play, use !play")
            return 0
    if progress == 3:
        game = [element for element in games]
        print(f"Your fourth game is: {game[3]}, With challenges: {games[game[3]][0]} & {games[game[3]][1]}")
        print("Do you wanna start the fourth game? Y/N")
        B = YorN()
        if B == True:
            print("Game 4 started, when youre done, use !update to update your score. For a status check, use !status")
            status = "Playing game 4"
            data["status"] = status
            x[ID] = data
            with open("database.json", "w") as db:
                json.dump(x, db)
            return 0
        if B == False:
            print("When you wanna play, use !play")
            return 0
    if progress == 4:
        game = [element for element in games]
        print(f"Your fifth game is: {game[4]}, With challenges: {games[game[4]][0]} & {games[game[4]][1]}")
        print("Do you wanna start the fifth game? Y/N")
        B = YorN()
        if B == True:
            print("Game 5 started, when youre done, use !update to update your score. For a status check, use !status")
            status = "Playing game 5"
            data["status"] = status
            x[ID] = data
            with open("database.json", "w") as db:
                json.dump(x, db)
            return 0
        if B == False:
            print("When you wanna play, use !play")
            return 0
    else:
        print("Fatal error, talk to OrbitalPeriod#1771")

def status(ID):
    global x

    data = x[ID]
    games = data["games"]
    status = data["status"]
    score = data["score"]
    progress = data["progress"]
    game = [element for element in games]

    if status == "": 
        print("no game set up\nUse !start to set up a game")
        return 0
    elif status == "Game set up":
        print("Game set up, not playing right now.\n", f"Your next game will be {game[0]}, with challenges {games[game[0]][0]} & {games[game[0]][1]}.")
        return 0
    elif "Playing" in status:
        print(f"{status}, The challenges being; {games[game[progress]][0]} & {games[game[progress]][1]}")
    elif status == "ready":
        print(f"You have finished {progress} games, your next game will be {game[progress]}\n Your current score is: {score}")
    elif status == "Finished":
        print("You have finished your run, see !finish to see your results")

def YorN():
    while True:
        Inpt = input().lower()
        if Inpt == "y":
            return True
        elif Inpt == "n":
            return False
        else:
            print("unknown input")

def Score(ID):
    global x
    data = x[ID]
    results = data["results"]
    score = data["score"]

    l = [results["game 0"][0], results["game 1"][0], results["game 2"][0], results["game 3"][0],results["game 4"][0], 0]

    y = 0
    max_count = 0
    extra_score = 0

    for j in l:
        if j == 100:
            y += 1
        else:
            if y > max_count:
                max_count = y
            y = 0  

    if max_count >= 2:
        extra_score += 100
    if max_count >= 3:
        extra_score += 150
    if max_count >= 4:
        extra_score += 200
    if max_count >= 5:
        extra_score += 300

    game_score = 0
    for i in range(0,5):
        game_score += results[f"game {i}"][0] +  results[f"game {i}"][1]

    score = extra_score + game_score
    data["score"] = score
    x[ID] = data
    with open("database.json", "w") as db:
        json.dump(x, db)
    return score

def update(ID):
    global x

    data = x[ID]
    status = data["status"]
    games = data["games"]
    game = [element for element in games]
    results = data["results"]
    progress = data["progress"]
    game_picks = ["first", "second", "third", "fourth", "fifth"]

    if "Playing" not in status:
        print("Not currently playing, Use !status to see your status.")
        return 0
    
    if "Playing" in status and "5" not in status:
        if "1" in status:
            i = 0
        elif "2" in status:
            i = 1
        elif "3" in status:
            i = 2
        elif "4" in status:
            i = 3
        print(f"Have you finished playing your {game_picks[i]} game? Y/N")
        B = YorN()
        if B == False:
            print("Use !update when you finish your game.")
            return 0
        print(f"Your {game_picks[i]} game was {game[i]}, Did you complete your main challenge: {games[game[i]][0]}")
        B = YorN()
        if B == True:
            results[f"game {i}"][0] = 100
            print(f"Did you complete the additional challenge, {games[game[i]][1]}")
            I = YorN()
            if I == True:
                results[f"game {i}"][1] = 50
                print(f"Game {i + 1} finished flawlessly, use !play to start the next game")
            if I == False:
                print(f"Game {i + 1} finished, use !play to start the next game")
        if B == False:
            print(f"Game {i + 1} failed horribly, use !play to start the next game")
        status = "ready"

    if status == "Playing game 5":
        i = 4
        print(f"Have you finished playing your fifth game? Y/N")
        B = YorN()
        if B == False:
            print("Use !update when you finish your game.")
            return 0
        print(f"Your fifth game was {game[i]}, Did you complete your main challenge: {games[game[i]][0]}")
        B = YorN()
        if B == True:
            results[f"game {i}"][0] = 100
            print(f"Did you complete the additional challenge, {games[game[i]][1]}")
            I = YorN()
            if I == True:
                results[f"game {i}"][1] = 50
                print(f"Game {i + 1} finished flawlessly, use !finish to see your results")
            if I == False:
                print(f"Game {i + 1} finished, use !finish to see your results.")
        if B == False:
            print(f"Game {i + 1} failed horribly, use !finish to see your results.") 
        status = "Finished"
               
    progress += 1

    data["status"] = status
    data["games"] = games
    data["results"] = results
    data["progress"] = progress
    x[ID] = data

    with open("database.json", "w") as db:
        json.dump(x, db)
    Score(ID)

def finish(ID):
    data = x[ID]
    progress = data["progress"] 
    score = data["score"]
    games = data["games"]
    status = data["status"]
    game = [element for element in games]
    highscore = data["highscore"]
    highscore_points = highscore["Highscore"]
    highscore_time = highscore["time"]
    cycle = highscore["cycle"]
    n = datetime.datetime.now()
    time = n.strftime("%c")

    if status != "Finished":
        print("Game not in Finished state, use !status.")
        return 0

    Score(ID)

    if highscore_points < score:
        print(f"Good job on finishing your pyramid run.\nthis was your {cycle} run.\nYou got {score} points with the games: {game[0]}, {game[1]}, {game[2]}, {game[3]} & {game[4]}\nWith a score of {score}, you got {highscore_points - score} more points than your previous high score, Congratulations!")
        highscore_points = score
        highscore_time = time
    else:
        print(f"Good job on finishing your pyramid run.\nthis was your {cycle} run.\nYou got {score} points with the games: {game[0]}, {game[1]}, {game[2]}, {game[3]} & {game[4]}\nWith a score of {score}, you got {highscore_points - score} less points than your highscore, Close one!")
    
    cycle += 1
    highscore["time"] = highscore_time
    highscore["Highscore"] = highscore_points
    data["status"] = status
    data["highscore"] = highscore
    x[ID] = data

    with open("database.json", "w") as db:
        json.dump(x, db) 

    ClearUsr(ID)

def profile(ID):
    data = x[ID]
    highscore = data["highscore"]
    highscore_points = highscore["Highscore"]
    highscore_time = highscore["time"]
    cycle = highscore["cycle"]
    print(f"User: {ID}\nYou got your highscore on {highscore_time}, you got {highscore_points} points.\nYou have played a total of {cycle} games of the pyramid.")

def dictionairy(Dict):  
 return sorted(Dict.items(), key = 
             lambda Dc:(Dc[1], Dc[0]))

def leaderboard():
    global x
    Leaderboard = {"Score" : 1501, "Lowest score" : 0}
    PrevScore = 1500
    Dict = {}
    for ID in x:
        Dict[ID] = x[ID]["highscore"]["Highscore"]
    LB = dictionairy(Dict)
    LB.reverse()
    print(LB)

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
            print("You sure you want to clear your current game? Y/N")
            B = YorN()
            if x == True:
                print("Clearing game")
                ClearUsr(ID)
                print("Game cleared...")
                y = 1
            elif x == False:
                print("Roger")
                y = 1
        if x == "!status":
            status(ID) 
        if x == "!update":
            update(ID)
        if x == "!score":
            print("Your current score is: " + str(Score(ID)))
        if x == "!finish":
            finish(ID)
        if x == "!profile":
            profile(ID)
        if x == "!leaderboard":
            leaderboard()

Main() 