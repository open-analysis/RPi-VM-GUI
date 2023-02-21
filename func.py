import vars
import operations as ops

## Open Screens
def openAudioOutputOptions():
    ops.openScreen(vars.audio_out)

def openAudioInputOptions():
    ops.openScreen(vars.audio_in)

def openDefaultOutputScreen():
    ops.openScreen(vars.defaultAudioOutput)

def openDefaultInputScreen():
    ops.openScreen(vars.defaultAudioInput)

def openDefaultAudioOutput():
    ops.openScreen(vars.getDefaultAudioOutput())

def openAudioOutput():
    ops.openScreen(vars.audio_output_opts)

def openDefaultAudioInput():
    ops.openScreen(vars.getDefaultAudioInput())

def openAudioInput():
    ops.openScreen(vars.audio_input_opts)

def openAudioProgs():
    ops.openScreen(vars.audio_progs)


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

## Setting variables
# Audio input default
def setMicropohoneDefault():
    vars.setDefaultAudioInput("speakers")
    ops.openScreen(vars.audio_input_opts)

# Audio out default
def setSpeakersDefault():
    vars.setDefaultAudioOutput("speakers")
    ops.openScreen(vars.audio_output_opts)
def setHeadphonesDefault():
    vars.setDefaultAudioOutput("headphones")
    ops.openScreen(vars.audio_output_opts)

# Audio program 
def setProgSpotify():
    vars.setAudioProg("Spotify")
    ops.openScreen(vars.audio_prog_opts)
def setProgDiscord():
    vars.setAudioProg("Discord")
    ops.openScreen(vars.audio_prog_opts)
def setProgFirefox():
    vars.setAudioProg("Firefox")
    ops.openScreen(vars.audio_prog_opts)