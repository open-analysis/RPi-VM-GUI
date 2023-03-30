import button_operations as button_ops
import utils
import build
import server

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

def setDefaultAudioDevice(name, devType):
    server.updateQueue(f"device setDefault {name} {devType}")

def toggleMuteAudioOutDevice():
    server.updateQueue(f"device mute toggle {button_ops.default_audio_output}")

def incVolAudioOutDevice(inc):
    server.updateQueue(f"device volume {inc} {button_ops.default_audio_output}")

def decVolAudioOutDevice(dec):
    server.updateQueue(f"device volume {dec} {button_ops.default_audio_output}")


def toggleMuteAudioInDevice():
    server.updateQueue(f"device mute toggle {button_ops.default_audio_input}")

def incVolAudioInDevice(inc):
    server.updateQueue(f"device volume {inc} {button_ops.default_audio_input}")

def decVolAudioInDevice(dec):
    server.updateQueue(f"device volume {dec} {button_ops.default_audio_input}")


def toggleMuteProgram():
    prog = button_ops.getAudioProg()
    server.updateQueue(f"program mute toggle {prog}")

def setMuteProgram(mute):
    prog = button_ops.getAudioProg()
    server.updateQueue(f"program mute {mute} {prog}")

def incVolProgram(inc):
    prog = button_ops.getAudioProg()
    server.updateQueue(f"program volume {inc} {prog}")

def decVolProgram(dec):
    prog = button_ops.getAudioProg()
    server.updateQueue(f"program volume {dec} {prog}")
