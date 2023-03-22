import utils

devices = [
    ["in", "microphone", "", True],
    ["out", "speakers", "", False],
    ["in", "test input", "", False],
    ["out", "headphones", "", True],
]

# programs = [
#     ["Spotify", ""],
#     ["Firefox", ""],
#     ["Discord", ""],
#     ["Civ6", ""],
# ]

# Len = 9
# programs = [
#     ["Spotify", ""],
#     ["Firefox", ""],
#     ["Discord", ""],
#     ["Civ6", ""],
#     ["Risk of Rain 2", ""],
#     ["TitanFall 2", ""],
#     ["Prog1", ""],
#     ["Prog2", ""],
#     ["Prog3", ""],
# ]

# # Len = 12
# programs = [
#     ["Spotify", ""],
#     ["Firefox", ""],
#     ["Discord", ""],
#     ["Civ6", ""],
#     ["Risk of Rain 2", ""],
#     ["TitanFall 2", ""],
#     ["Prog1", ""],
#     ["Prog2", ""],
#     ["Prog3", ""],
#     ["Prog4", ""],
#     ["Prog5", ""],
#     ["Prog6", ""],
# ]

# Len = 12
programs1 = [
    ["Spotify", ""],
    ["Firefox", ""],
    ["Discord", ""],
    ["Civ6", ""],
    ["Risk of Rain 2", ""],
    ["TitanFall 2", ""]]
programs2=[
    ["Prog1", ""],
    ["Prog2", ""],
    ["Prog3", ""],
    ["Prog4", ""],
    ["Prog5", ""],
    ["Prog6", ""],
]


# Len = 22
# programs = [
#     ["Spotify", ""],
#     ["Firefox", ""],
#     ["Discord", ""],
#     ["Civ6", ""],
#     ["Risk of Rain 2", ""],
#     ["TitanFall 2", ""],
#     ["Prog1", ""],
#     ["Prog2", ""],
#     ["Prog3", ""],
#     ["Prog4", ""],
#     ["Prog5", ""],
#     ["Prog6", ""],
#     ["Prog7", ""],
#     ["Prog8", ""],
#     ["Prog9", ""],
#     ["Prog10", ""],
#     ["Prog11", ""],
#     ["Prog12", ""],
#     ["Prog13", ""],
#     ["Prog14", ""],
#     ["Prog15", ""],
#     ["Prog16", ""],
# ]

def start():
    print("Importing...")
    for dev in devices:
        utils.importDevices(dev)
    for prog in programs1:
        utils.importProgs(prog)
    for prog in programs2:
        utils.importProgs(prog)
