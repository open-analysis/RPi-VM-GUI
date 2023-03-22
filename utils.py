import button_operations as button_ops

def getAttributes(listName):
    names = [i[0] for i in listName]
    images = [i[1] for i in listName]
    cmds = [i[2] for i in listName]

    return [names, images, cmds]

def device_setter(dev):
    if dev[0] == "in":
        if dev[3] == True:
            button_ops.setDefaultAudioInputDevice(dev[1])
        return [dev[1], dev[2], lambda: button_ops.setDefaultDevice(dev[1], "in")]
    else:
        if dev[3] == True:
            button_ops.setDefaultAudioOutputDevice(dev[1])
        return [dev[1], dev[2], lambda: button_ops.setDefaultDevice(dev[1], "out")]

# newDev structure = [device type, device name, device image path, default audio status]
def importDevices(newDevs):
    print(newDevs)
    if newDevs[0] == "in":
        button_ops.defaultAudioInputDevices.append(device_setter(newDevs))
    elif newDevs[0] == "out":
        button_ops.defaultAudioOutputDevices.append(device_setter(newDevs))

def removeDevice(device):
    currList = None
    if device[0] == "in":
        currList = button_ops.defaultAudioInputDevices
    elif device[0] == "out":
        currList = button_ops.defaultAudioOutputDevices
    
    for dev in currList:
        if dev[1] == device[1]:
            currList.remove(dev)
            break

def program_setter(prog):
    return [prog[0], prog[1], lambda: button_ops.setCurrProg(prog[0])]

# newProgs structure = [program name, program image path]
def importProgs(newProgs):
    button_ops.audio_progs.append(program_setter(newProgs))

def removeProgs(program):
    for prog in button_ops.audio_progs:
        if prog[0] == program:
            button_ops.audio_progs.remove(prog)
            break
