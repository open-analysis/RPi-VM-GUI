import vars
import operations as ops

## Open Screens
def openAudioOutputOptions():
    ops.openScreen(vars.audio_out)

def openAudioInputOptions():
    ops.openScreen(vars.audio_in)

def openDefaultOutputScreen():
    ops.openScreen(vars.defaultAudioOutputDevices)

def openDefaultInputScreen():
    ops.openScreen(vars.defaultAudioInputDevices)

def openDefaultAudioOutputDevices():
    ops.openScreen(vars.getDefaultAudioOutputDevice())

def openAudioOutput():
    ops.openScreen(vars.audio_output_opts)

def openDefaultAudioInputDevices():
    ops.openScreen(vars.getDefaultAudioInputDevice())

def openAudioInput():
    ops.openScreen(vars.audio_input_opts)

def openAudioProgs():
    ops.openScreen(vars.audio_progs)


## Setting variables
# Setting device
def setDefaultDevice(name, type):
    print("\t\thello")
    if type == "out":
        vars.setDefaultAudioOutputDevice(name)
        ops.openScreen(vars.audio_output_opts)
    elif type == "in":
        vars.setDefaultAudioInputDevice(name)
        ops.openScreen(vars.audio_input_opts)

# Audio program 
def setCurrProg(name):
    print(name)
    vars.setAudioProg(name)
    ops.openScreen(vars.audio_prog_opts)
    
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
