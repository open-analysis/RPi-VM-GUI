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
def updateDevices(newDevs: dict):

    with open("out.txt", "a") as w:
        w.write(f"Updating Device with {newDevs['name']}\n")    
    
    dev_set = False
    # Check if the device is already in the current list
    for opt_dev in opts_audio_devices:
        # If it's already in the list, update the current item
        if newDevs['name'] == opt_dev.m_name:
            opt_dev.setImg(newDevs['img'])
            opt_dev.setVolume(newDevs['volume'])
            opt_dev.setMute(newDevs['mute'])
            opt_dev.setDefault(newDevs['default'])
            opt_dev.setOutput(newDevs['type'])
            dev_set = True
            with open("out.txt", "a") as w:
                w.write(f"Item {newDevs['name']} already in list\n")
            break
    # Device not found in the list, create a new object & add it
    if not dev_set:
        with open("out.txt", "a") as w:
            w.write(f"Item {newDevs['name']} not found in list\n")    
        aDev = AudioDevice(newDevs['name'], newDevs['img'], newDevs['volume'], newDevs['mute'])
        # Check if it's input/output audio device
        if newDevs['type'] == "in":
            aDev.setOutput(False)
        aDev.setDefault(newDevs['type'])
        opts_audio_devices.append(aDev)

    with open("out.txt", "a") as w:
            w.write(f"\n")

# newProg structure = [program name, program image path, program volume, program mute state]
def updateProgs(newProg):
    updated_programs = []
        
    prog_set = False
    # Check if the program is already in the current list
    for opt_prog in opts_audio_progs:
        # If it's already in the list, update the current item
        if newProg['name'] == opt_prog.m_name:
            opt_prog.setImg(newProg['img'])
            opt_prog.setVolume(newProg['volume'])
            opt_prog.setMute(newProg['mute'])
            updated_programs.append(opt_prog)
            prog_set = True
            break
    # Program not found in the list, create a new object & add it
    if not prog_set:
        aProg = AudioProgram(newProg['name'], newProg['img'], newProg['volume'], newProg['mute'])
        opts_audio_progs.append(aProg)
        updated_programs.append(aProg)
