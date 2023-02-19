import vars
import operations as ops

## Open Screens
def openAudioOptions():
    ops.openScreen(vars.audio_out)

def openDefaultsScreen():
    ops.openScreen(vars.defaultAudio)

def setHeadphonesDefault():
    vars.setDefaultAudio(vars.headphones_opts)

def openDefaultAudio():
    ops.openScreen(vars.getDefaultAudio())

def openAudio():
    ops.openScreen(vars.getDefaultAudio())

def openMics():
    ops.openScreen(vars.mic_opts)


## Audio Control
# Microphone
def toggleMuteMic():
    ops.toggleMuteDevice("microphone")

def incBoostMic():
    ops.incVolDevice("microphone", 5)

def decBoostMic():
    ops.decVolDevice("microphone", 5)

# Speakers
def toggleMuteSpeakers():
    ops.toggleMuteDevice("speakers")

def incVolSpeakers():
    ops.incVolDevice("speakers", 5)

def decVolSpeakers():
    ops.decVolDevice("speakers", 5)

# Headphones
def toggleMuteHeadphones():
    ops.toggleMuteDevice("Headphones")

def incVolHeadphones():
    ops.incVolDevice("Headphones", 5)

def decVolHeadphones():
    ops.decVolDevice("Headphones", 5)


## Setting variables
# Audio out default
def setSpeakersDefault():
    vars.setDefaultAudio(vars.speaker_opts)