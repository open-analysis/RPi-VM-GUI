import button_operations as button_ops

def getAttributes(listName):
    names = [i[0] for i in listName]
    images = [i[1] for i in listName]
    cmds = [i[2] for i in listName]

    return [names, images, cmds]

def device_setter(dev):
    if dev['type'] == "in":
        if dev['default'] == True:
            button_ops.setDefaultAudioInputDevice(dev['name'])
        return [dev['name'], dev['img'], lambda: button_ops.setDefaultDevice(dev['name'], "in")]
    else:
        if dev['default'] == True:
            button_ops.setDefaultAudioOutputDevice(dev['name'])
        return [dev['name'], dev['img'], lambda: button_ops.setDefaultDevice(dev['name'], "out")]

# newDev structure = [device type, device name, device image path, default audio status]
def importDevices(newDevs):
    if newDevs['type'] == "in":
        button_ops.defaultAudioInputDevices.append(device_setter(newDevs))
    elif newDevs['type'] == "out":
        button_ops.defaultAudioOutputDevices.append(device_setter(newDevs))

def removeDevice(device):
    currList = None
    if device['type'] == "in":
        currList = button_ops.defaultAudioInputDevices
    elif device['type'] == "out":
        currList = button_ops.defaultAudioOutputDevices
    for dev in currList:
        if dev[0] == device['name']:
            currList.remove(dev)
            break

def program_setter(prog):
    return [prog['name'], prog['img'], lambda: button_ops.setCurrProg(prog['name'])]

# newProgs structure = [program name, program image path]
def importProgs(newProgs):
    button_ops.audio_progs.append(program_setter(newProgs))

def removeProgs(program):
    for prog in button_ops.audio_progs:
        if prog[0] == program['name']:
            button_ops.audio_progs.remove(prog)
            break
