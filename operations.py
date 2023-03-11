import button_operations as button_ops
import utils
import build

def openScreen(list):
    frm_main = button_ops.getFrmMain()
    names, images, cmds = utils.getAttributes(list)
    frm_main = build.moveFolder(frm_main, names, images, cmds)
    frm_main.pack()
    button_ops.setFrmMain(frm_main)

def openScreenExt(names, images, cmds, start):
    frm_main = button_ops.getFrmMain()
    build.destroyWidgets(frm_main)
    frm_main = build.buildWidgets(names, images, cmds, start)
    frm_main.pack()
    button_ops.setFrmMain(frm_main)

def toggleMuteAudioOutDevice():
    print(f"Toggling mute device {button_ops.default_audio_output}")

def incVolAudioOutDevice(inc):
    print(f"Increasing volume on device {button_ops.default_audio_output} by {inc}")

def decVolAudioOutDevice(dec):
    print(f"Decreasing volume on device {button_ops.default_audio_output} by {dec}")


def toggleMuteAudioInDevice():
    print(f"Toggling mute device {button_ops.default_audio_input}")

def incVolAudioInDevice(inc):
    print(f"Increasing volume on device {button_ops.default_audio_input} by {inc}")

def decVolAudioInDevice(dec):
    print(f"Decreasing volume on device {button_ops.default_audio_input} by {dec}")


def toggleMuteProgram():
    prog = button_ops.getAudioProg()
    print(f"Toggling mute Program {prog}")

def setMuteProgram(mute):
    prog = button_ops.getAudioProg()
    print(f"Setting Program {prog} mute {mute}")

def incVolProgram(inc):
    prog = button_ops.getAudioProg()
    print(f"Increasing volume on Program {prog} by {inc}")

def decVolProgram(dec):
    prog = button_ops.getAudioProg()
    print(f"Decreasing volume on Program {prog} by {dec}")