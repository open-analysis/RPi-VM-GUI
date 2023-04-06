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
    server.updateQueue(f"device${name}${devType}$setDefault")

def toggleMuteAudioOutDevice(dir):
    server.updateQueue(f"device${button_ops.default_audio_output}${dir}$mute$toggle")

def setMuteDevice(mute, dir):
    server.updateQueue(f"device${button_ops.default_audio_output}${dir}$mute${mute}")

def xVolAudioOutDevice(change, dir):
    server.updateQueue(f"device${button_ops.default_audio_output}${dir}$volume${change}")

def toggleMuteAudioInDevice(dir):
    server.updateQueue(f"device${button_ops.default_audio_input}${dir}$mute$toggle")

def xVolAudioInDevice(change, dir):
    server.updateQueue(f"device${button_ops.default_audio_input}${dir}$volume${change}")

def toggleMuteProgram(dir):
    prog = button_ops.getAudioProg()
    server.updateQueue(f"program${prog}${dir}$mute$toggle")

def setMuteProgram(mute, dir):
    prog = button_ops.getAudioProg()
    server.updateQueue(f"program${prog}${dir}$mute${mute}")

def xVolProgram(change, dir):
    prog = button_ops.getAudioProg()
    server.updateQueue(f"program${prog}${dir}$volume${change}")
    
