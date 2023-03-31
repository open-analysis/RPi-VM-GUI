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
    server.updateQueue(f"device {button_ops.default_audio_output} mute toggle")

def incVolAudioOutDevice(inc):
    server.updateQueue(f"device {button_ops.default_audio_output} volume {inc}")

def decVolAudioOutDevice(dec):
    server.updateQueue(f"device {button_ops.default_audio_output} volume {dec}")


def toggleMuteAudioInDevice():
    server.updateQueue(f"device {button_ops.default_audio_input} mute toggle")

def incVolAudioInDevice(inc):
    server.updateQueue(f"device {button_ops.default_audio_input} volume {inc}")

def decVolAudioInDevice(dec):
    server.updateQueue(f"device {button_ops.default_audio_input} volume {dec}")


def toggleMuteProgram():
    prog = button_ops.getAudioProg()
    server.updateQueue(f"program {prog} mute toggle")

def setMuteProgram(mute):
    prog = button_ops.getAudioProg()
    server.updateQueue(f"program {prog} mute {mute}")

def incVolProgram(inc):
    prog = button_ops.getAudioProg()
    server.updateQueue(f"program {prog} volume {inc}")

def decVolProgram(dec):
    prog = button_ops.getAudioProg()
    server.updateQueue(f"program {prog} volume {dec}")
