import operations as ops

## Open Screens
def openAudioOutputOptions():
    ops.openScreen(audio_out)

def openAudioInputOptions():
    ops.openScreen(audio_in)

def openDefaultOutputScreen():
    ops.openScreen(defaultAudioOutputDevices)

def openDefaultInputScreen():
    ops.openScreen(defaultAudioInputDevices)

def openDefaultAudioOutputDevices():
    ops.openScreen(getDefaultAudioOutputDevice())

def openAudioOutput():
    ops.openScreen(audio_output_opts)

def openDefaultAudioInputDevices():
    ops.openScreen(getDefaultAudioInputDevice())

def openAudioInput():
    ops.openScreen(audio_input_opts)

def openAudioProgs():
    print(f"Opening Audio Progs screen {audio_progs}")
    ops.openScreen(audio_progs)


## Setting variables
# Setting device
def setDefaultDevice(name, devType):
    if devType == "out":
        setDefaultAudioOutputDevice(name)
        ops.openScreen(audio_output_opts)
    elif devType == "in":
        setDefaultAudioInputDevice(name)
        ops.openScreen(audio_input_opts)
    ops.setDefaultAudioDevice(name, devType)

# Audio program 
def setCurrProg(name):
    setAudioProg(name)
    ops.openScreen(audio_prog_opts)
    
## Audio Device Control
# Audio input
def toggleMuteMic():
    ops.toggleMuteAudioInDevice()

def incBoostMic():
    ops.incVolAudioInDevice(5)

def decBoostMic():
    ops.decVolAudioInDevice(5)

# Audio output
def toggleMuteAudioOut():
    ops.toggleMuteAudioOutDevice()

def incVolAudioOut():
    ops.incVolAudioOutDevice(5)

def decVolAudioOut():
    ops.decVolAudioOutDevice(5)

## Audio Program Control
def toggleMuteAudioProgram():
    ops.toggleMuteProgram()

def setMuteAudioProgram():
    ops.setMuteProgram(True)

def setUnmuteAudioProgram():
    ops.setMuteProgram(False)

def incVolAudioProgram():
    ops.incVolProgram(5)

def decVolAudioProgram():
    ops.decVolProgram(5) 


frm_main = None
def setFrmMain(i_frm):
    global frm_main
    frm_main = i_frm
def getFrmMain():
    global frm_main
    return frm_main

default_audio_output = ""
def setDefaultAudioOutputDevice(name):
    global default_audio_output
    default_audio_output = name
def getDefaultAudioOutputDevice():
    global default_audio_output
    return default_audio_output

default_audio_input = ""
def setDefaultAudioInputDevice(name):
    global default_audio_input
    default_audio_input = name
def getDefaultAudioInputDevice():
    global default_audio_input
    return default_audio_input

curr_audio_prog = ""
def setAudioProg(name):
    global curr_audio_prog
    curr_audio_prog = name
def getAudioProg():
    global curr_audio_prog
    return curr_audio_prog

top = [["Audio Out", "", openAudioOutputOptions], 
       ["Audio In", "", openAudioInputOptions],
       ["", "", None],
       ["", "", None],
       ["", "", None],
       ["", "", None]]

defaultAudioOutputDevices =  []

defaultAudioInputDevices =  []

audio_progs = []

audio_out = [["Set output", "", openDefaultOutputScreen],
             ["Audio options", "", openAudioOutput],
             ["Audio Mixer", "", openAudioProgs],
             ["", "", None],
             ["", "", None],
             ["", "", None]]

audio_in =  [["Set input", "", openDefaultInputScreen],
             ["Audio options", "", openAudioInput],
             ["", "", None],
             ["", "", None],
             ["", "", None],
             ["", "", None]]

audio_output_opts = [["Mute", "", toggleMuteAudioOut],
                     ["Inc Vol", "", incVolAudioOut],
                     ["", "", None],
                     ["", "", None],
                     ["Dec Vol", "", decVolAudioOut],
                     ["", "", None]]

audio_input_opts = [["Mute", "", toggleMuteMic],
                    ["Inc Boost", "", incBoostMic],
                    ["", "", None],
                    ["", "", None],
                    ["Dec Boost", "", decBoostMic],
                    ["", "", None]]

audio_prog_opts = [["Toggle Mute", "", toggleMuteAudioProgram],
                   ["Mute", "", setMuteAudioProgram],
                   ["Inc Vol", "", incVolAudioProgram],
                   ["", "", None],
                   ["Unmute", "", setUnmuteAudioProgram],
                   ["Dec Vol", "", decVolAudioProgram]]
