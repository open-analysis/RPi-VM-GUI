import func
import vars

def getAttributes(listName):
    names = [i[0] for i in listName]
    images = [i[1] for i in listName]
    cmds = [i[2] for i in listName]

    return [names, images, cmds]

def device_setter(dev):
    if dev[0] == "in":
        if dev[3] == True:
            vars.setDefaultAudioInputDevice(dev[1])
        return [dev[1], dev[2], lambda: func.setDefaultDevice(dev[1], "in")]
    else:
        if dev[3] == True:
            vars.setDefaultAudioOutputDevice(dev[1])
        return [dev[1], dev[2], lambda: func.setDefaultDevice(dev[1], "out")]

# newDev structure = [device type, device name, device image path, default audio status]
def importDevices(newDevs):
    for dev in newDevs:
        if dev[0] == "in":
            vars.defaultAudioInputDevices.append(device_setter(dev))
        elif dev[0] == "out":
            vars.defaultAudioOutputDevices.append(device_setter(dev))


def program_setter(prog):
    return [prog[0], prog[1], lambda: func.setCurrProg(prog[0])]

# newProgs structure = [program name, program image path]
def importProgs(newProgs):
    for prog in newProgs:
        vars.audio_progs.append(program_setter(prog))