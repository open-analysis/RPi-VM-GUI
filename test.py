import utils

devices = [
        {"type": "in", "name": "microphone", "img": "", "default": True},
        {"type": "out", "name": "speakers", "img": "", "default": False},
        {"type": "in", "name": "test input", "img": "", "default": False},
        {"type": "out", "name": "headphones", "img": "", "default": True},
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
        {"name":"spotify", "img":""},
        {"name":"Firefox", "img":""},
        {"name":"Discord", "img":""},
        {"name":"Civ6", "img":""},
        {"name":"Risk of Rain 2", "img":""},
        {"name":"TitanFall 2", "img":""}]
programs2=[
    {"name":"Prog1", "img":""},
    {"name":"Prog2", "img":""},
    {"name":"Prog3", "img":""},
    {"name":"Prog4", "img":""},
    {"name":"Prog5", "img":""},
    {"name":"Prog6", "img":""},
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
    #for prog in programs1:
    #    utils.importProgs(prog)
    #for prog in programs2:
    #    utils.importProgs(prog)
