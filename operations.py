import vars
import utils
import build

def openScreen(list):
    frm_main = vars.getFrmMain()
    names, images, cmds = utils.getAttributes(list)
    frm_main = build.moveFolder(frm_main, names, images, cmds)
    frm_main.pack()
    vars.setFrmMain(frm_main)

def toggleMuteDevice(devName):
    print(f"Muting device {devName}")

def incVolDevice(devName, inc):
    print(f"Increasing volume on device {devName} by {inc}")

def decVolDevice(devName, dec):
    print(f"Decreasing volume on device {devName} by {dec}")
