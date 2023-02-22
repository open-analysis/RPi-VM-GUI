import utils

devices = [
    ["in", "microphone", "", True],
    ["out", "speakers", "", False],
    ["in", "test input", "", False],
    ["out", "headphones", "", True],
]

programs = [
    ["Spotify", ""],
    ["Firefox", ""],
    ["Discord", ""],
    ["Civ6", ""],
]

def start():
    print("Importing...")
    utils.importDevices(devices)
    utils.importProgs(programs)