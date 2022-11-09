import json

RANK_GRADE = {
    "S+" : 30,
    "S" : 28,
    "S-": 26,
    "A+" : 24,
    "A" : 22,
    "A-" : 20,
    "B+" : 18,
    "B" : 16,
    "B-" : 14,
    "C+" : 12,
    "C" : 10,
    "C-" : 8,
    "D+" : 6,
    "D" : 4,
    "D-" : 2
}

CLASS_TOTAL = {
    "splashcaster" : 0,
    "blastcaster" : 0,
    "chaincaster" : 0,
    "mysticcaster" : 0,
    "mechaccord" : 0,
    "phalanxcaster" : 0,
    "corecaster" : 0,
    "artsprotector" : 0,
    "duelist" : 0,
    "juggernaut" : 0,
    "fortress" : 0,
    "guardian" : 0,
    "protector" : 0,
    "centurion" : 0,
    "artsfighter" : 0,
    "fighter" : 0,
    "swordmaster" : 0,
    "dreadnought" : 0,
    "musha" : 0,
    "liberatorguard" : 0,
    "lord" : 0,
    "reaper" : 0,
    "instructor" : 0,
    "multitagertmedic" : 0,
    "medic" : 0,
    "wanderingmedic" : 0,
    "therapist" : 0,
    "flinger" : 0,
    "marksman" : 0,
    "artilleryman" : 0,
    "spreadshooter" : 0,
    "heavyshooter" : 0,
    "besieger" : 0,
    "deadeye" : 0,
    "ambusher" : 0,
    "merchant" : 0,
    "executor" : 0,
    "hookmaster" : 0,
    "pushstroker" : 0,
    "sacrificalspecialist" : 0,
    "dollkeeper" : 0,
    "trapmaster" : 0,
    "artificer" : 0,
    "bard" : 0,
    "abjurer" : 0,
    "hexer" : 0,
    "decelbinder" : 0,
    "summoner" : 0,
    "charger" : 0,
    "standardbearer" : 0,
    "pioneer" : 0,
    "tactician" : 0
}

TO_BUILD = []

CHARACTER_LIST = []

def increase_class(name:str):
    CLASS_TOTAL[name] = CLASS_TOTAL[name] + 1

def character_score(classname:str, lvl:int, grade:int):
    if(CLASS_TOTAL[classname] != 1):
        return lvl*grade/CLASS_TOTAL[classname]
    return lvl*grade/2

def character_dict(name:str, classname:str, lvl:str, grade:str):
    dict = {
        "NAME":name,
        "CLASS":classname,
        "LEVEL":int(lvl),
        "GRADE":int(RANK_GRADE[grade])
    }
    return dict

def main():
    f = open("to_build.txt", "r")
    for l in f:
        line = l
        if(l[-1] == '\n'):
            line = l[:-1]
        TO_BUILD.append(line)
    f.close()

    f = open("tierlist.txt", "r")
    classname = ""
    for l in f:
        if(l[0] == "#"):
            classname = l[1:-2]
        else:
            increase_class(classname)
            args = l.split("|")
            if(args[2][-1] == '\n'):
                args[2] = args[2][:-1]
            print(args)
            if(args[1] in TO_BUILD):
                CHARACTER_LIST.append(character_dict(args[1], classname, args[2], args[0]))
    f.close()

    out = {}

    for ch in CHARACTER_LIST:
        out[ch["NAME"]] = character_score(ch["CLASS"],ch["LEVEL"],ch["GRADE"])
    
    out = dict(sorted(out.items(), key=lambda item: item[1], reverse=True))

    with open("output.txt", 'w') as f:
        f.write(json.dumps(out, indent = 4))

main()