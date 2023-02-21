import vars
import utils
import build

def openScreen(list):
    frm_main = vars.getFrmMain()
    names, images, cmds = utils.getAttributes(list)
    frm_main = build.moveFolder(frm_main, names, images, cmds)
    frm_main.pack()
    vars.setFrmMain(frm_main)

def toggleMuteAudioOutDevice():
    print(f"Toggling mute device {vars.default_audio_output}")

def incVolAudioOutDevice(inc):
    print(f"Increasing volume on device {vars.default_audio_output} by {inc}")

def decVolAudioOutDevice(dec):
    print(f"Decreasing volume on device {vars.default_audio_output} by {dec}")


def toggleMuteAudioInDevice():
    print(f"Toggling mute device {vars.default_audio_input}")

def incVolAudioInDevice(inc):
    print(f"Increasing volume on device {vars.default_audio_input} by {inc}")

def decVolAudioInDevice(dec):
    print(f"Decreasing volume on device {vars.default_audio_input} by {dec}")


def toggleMuteProgram():
    prog = vars.getAudioProg()
    print(f"Toggling mute Program {prog}")

def setMuteProgram(mute):
    prog = vars.getAudioProg()
    print(f"Setting Program {prog} mute {mute}")

def incVolProgram(inc):
    prog = vars.getAudioProg()
    print(f"Increasing volume on Program {prog} by {inc}")

def decVolProgram(dec):
    prog = vars.getAudioProg()
    print(f"Decreasing volume on Program {prog} by {dec}")