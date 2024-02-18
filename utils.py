from menu_options import opts_audio_devices, opts_audio_progs
from data import AudioDevice, AudioProgram

"""
Device Format
    {
        type: output/input
        name: dev name
        img: <>
        default: T/F
        volume: 0-100
        mute: T/F
    }

Program Format
    {
        name: prog name
        img: <>
        volume: 0-100
        mute: T/F
    }
"""

def getAttributes(listName):
    names = [i[0] for i in listName]
    images = [i[1] for i in listName]
    cmds = [i[2] for i in listName]

    return [names, images, cmds]

# newDev structure = [device type, device name, device image path, default audio status, device volume, device mute status]
def updateDevices(newDevs):
    updated_devices = []
    devices_to_remove = []
    for dev in newDevs:
        dev_set = False
        # Check if the device is already in the current list
        for opt_dev in opts_audio_devices:
            # If it's already in the list, update the current item
            if dev['name'] == opt_dev.m_name:
                opt_dev.setImg(dev['img'])
                opt_dev.setVolume(dev['vol'])
                opt_dev.setMute(dev['mute'])
                opt_dev.setDefault(dev['default'])
                opt_dev.setOutput(dev['type'])
                updated_devices.append(opt_dev)
                dev_set = True
                break
        # Device not found in the list, create a new object & add it
        if not dev_set:
            aDev = AudioDevice(dev['name'], dev['img'], dev['vol'], dev['mute'])
            # Check if it's input/output audio device
            if dev['type'] == "in":
                aDev.setOutput(False)
            aDev.setDefault(dev['type'])
            opts_audio_devices.append(aDev)
            updated_devices.append(aDev)
        
    # Check for any devices that were removed
    for dev in opts_audio_devices:
        updated = False
        for updated_dev in updated_devices:
            if dev.m_name == updated_dev.m_name:
                updated = True
                break
        
        if not updated:
            devices_to_remove.append(dev)

    # finally remove the devices from list
    for dev in devices_to_remove:
        opts_audio_devices.remove(dev)

# newProgs structure = [program name, program image path, program volume, program mute state]
def updateProgs(newProgs):
    updated_programs = []
    programs_to_remove = []
    for prog in newProgs:
        prog_set = False
        # Check if the program is already in the current list
        for opt_prog in opts_audio_progs:
            # If it's already in the list, update the current item
            if prog['name'] == opt_prog.m_name:
                opt_prog.setImg(prog['img'])
                opt_prog.setVolume(prog['vol'])
                opt_prog.setMute(prog['mute'])
                updated_programs.append(opt_prog)
                prog_set = True
                break
        # Program not found in the list, create a new object & add it
        if not prog_set:
            aProg = AudioProgram(prog['name'], prog['img'], prog['vol'], prog['mute'])
            opts_audio_progs.append(aProg)
            updated_programs.append(aProg)
        
    # Check for any programs that were removed
    for prog in opts_audio_progs:
        updated = False
        for updated_prog in updated_programs:
            if prog.m_name == updated_prog.m_name:
                updated = True
                break
        
        if not updated:
            programs_to_remove.append(prog)

    # finally remove the programs from list
    for prog in programs_to_remove:
        opts_audio_progs.remove(prog)

