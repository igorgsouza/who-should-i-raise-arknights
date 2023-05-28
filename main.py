import json

RANK_GRADE = {
    "EX" : 20,
    "S+" : 15,
    "S" : 14,
    "S-": 13,
    "A+" : 12,
    "A" : 11,
    "A-" : 10,
    "B+" : 9,
    "B" : 8,
    "B-" : 7,
    "C+" : 6,
    "C" : 5,
    "C-" : 4,
    "D+" : 3,
    "D" : 2,
    "D-" : 1
}

MAINCLASS_TOTAL = {
    "sniper" : 0,
    "caster" : 0,
    "guard" : 0,
    "defender" : 0,
    "vanguard" : 0,
    "medic" : 0,
    "supporter" : 0,
    "specialist" : 0
}

MAINCLASS_BIG_CHIP = {
    "sniper" : 0,
    "caster" : 0,
    "guard" : 0,
    "defender" : 0,
    "vanguard" : 0,
    "medic" : 0,
    "supporter" : 0,
    "specialist" : 0
}

MAINCLASS_SMALL_CHIP = {
    "sniper" : 0,
    "caster" : 0,
    "guard" : 0,
    "defender" : 0,
    "vanguard" : 0,
    "medic" : 0,
    "supporter" : 0,
    "specialist" : 0
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
    "tactician" : 0,
    "agent":0,
    "incantation" : 0
}

sniper = ["marksman", "flinger", "artilleryman", "spreadshooter", "heavyshooter", "besieger", "deadeye"]
vanguard = ["tactician", "pioneer", "standardbearer", "charger","agent"]
supporter = ["summoner", "decelbinder", "hexer", "abjurer", "bard", "artificer"]
specialist = ["trapmaster", "dollkeeper", "sacrificalspecialist", "pushstroker", "hookmaster", "executor", "merchant", "ambusher"]
medic = ["therapist", "wanderingmedic", "medic", "multitagertmedic", "incantation"]
guard = ["instructor", "reaper", "lord", "liberatorguard", "musha", "dreadnought", "swordmaster", "fighter", "artsfighter", "centurion"]
defender = ["protector", "guardian", "fortress", "juggernaut", "duelist", "artsprotector"]
caster = ["corecaster", "phalanxcaster", "mechaccord", "mysticcaster", "chaincaster", "blastcaster", "splashcaster"]

TO_BUILD = []

CHARACTER_LIST = []

ORDER = 10

def increase_class(name:str):
    if(name == "skill"):
        return
    CLASS_TOTAL[name] += 1
    MAINCLASS_TOTAL[find_mainclass(name)] += 1

def find_mainclass(name:str):
    if name in sniper:
        return "sniper"
    if name in vanguard:
        return "vanguard"
    if name in supporter:
        return "supporter"
    if name in specialist:
        return "specialist"
    if name in medic:
        return "medic"
    if name in guard:
        return "guard" 
    if name in defender:
        return "defender"
    return "caster"


def character_score(classname:str, lvl:int, grade:int, ord:int):
    if(lvl != 4):
        return 0
    val = grade*(1 + 0.1/ord + 0.1/MAINCLASS_TOTAL[find_mainclass(classname)] + 0.1*(lvl-3) + 0.1/max(CLASS_TOTAL[classname],2))
    return "%0.4f" % val

def character_dict(name:str, classname:str, lvl:str, grade:str):
    global ORDER
    dict = {
        "NAME":name,
        "CLASS":classname,
        "LEVEL":int(lvl),
        "GRADE":int(RANK_GRADE[grade]),
        "WEIGHT" : ORDER
    }
    ORDER += 1
    return dict

def main():
    f = open("to_build.txt", "r")
    for l in f:
        line = l
        if(l[-1] == '\n'):
            line = l[:-1]
        if(line[0] != '*'):
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
                if(classname == "skill"):
                    continue
                if(args[2] == '6'):
                    MAINCLASS_BIG_CHIP[find_mainclass(classname)] += 8
                    MAINCLASS_SMALL_CHIP[find_mainclass(classname)] += 5
                if(args[2] == '5'):
                    MAINCLASS_BIG_CHIP[find_mainclass(classname)] += 6
                    MAINCLASS_SMALL_CHIP[find_mainclass(classname)] += 4
                if(args[2] == '4'):
                    MAINCLASS_BIG_CHIP[find_mainclass(classname)] += 5
                    MAINCLASS_SMALL_CHIP[find_mainclass(classname)] += 3

    f.close()

    out = {}

    for ch in CHARACTER_LIST:
        out[ch["NAME"]] = character_score(ch["CLASS"],ch["LEVEL"],ch["GRADE"],ch["WEIGHT"])
    
    out = dict(sorted(out.items(), key=lambda item: float(item[1]), reverse=True))

    with open("output.txt", 'w') as f:
        f.write(json.dumps(out, indent = 4))

    print(MAINCLASS_BIG_CHIP)
    print(MAINCLASS_SMALL_CHIP)


main()