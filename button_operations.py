# import operations as ops

# ## Open Screens
# def openAudioOutputOptions():
#     ops.openScreen(audio_out)

# def openAudioInputOptions():
#     ops.openScreen(audio_in)

# def openDefaultOutputScreen():
#     ops.openScreen(defaultAudioOutputDevices)

# def openDefaultInputScreen():
#     ops.openScreen(defaultAudioInputDevices)

# def openDefaultAudioOutputDevices():
#     ops.openScreen(getDefaultAudioOutputDevice())

# def openAudioOutput():
#     ops.openScreen(audio_output_opts)

# def openDefaultAudioInputDevices():
#     ops.openScreen(getDefaultAudioInputDevice())

# def openAudioInput():
#     ops.openScreen(audio_input_opts)

# def openAudioProgs():
#     ops.openScreen(audio_progs)


# ## Setting variables
# # Setting device
# def setDefaultDevice(name, devType):
#     if devType == "out":
#         setDefaultAudioOutputDevice(name)
#         ops.openScreen(audio_output_opts)
#     elif devType == "in":
#         setDefaultAudioInputDevice(name)
#         ops.openScreen(audio_input_opts)
#     ops.setDefaultAudioDevice(name, devType)

# # Audio program 
# def setCurrProg(name):
#     setAudioProg(name)
#     ops.openScreen(audio_prog_out_opts)
    
# ## Audio Device Control
# # Audio input
# def toggleMuteMic():
#     ops.toggleMuteAudioInDevice("in")

# def setMuteAudioInDevice():
#     ops.setMuteDevice(True, "in")

# def setUnmuteAudioInDevice():
#     ops.setMuteDevice(False, "in")

# def incBoostMic():
#     ops.xVolAudioInDevice("5", "in")

# def decBoostMic():
#     ops.xVolAudioInDevice("-5", "in")

# # Audio output
# def toggleMuteAudioOut():
#     ops.toggleMuteAudioOutDevice("out")

# def setMuteAudioOutDevice():
#     ops.setMuteDevice(True, "out")

# def setUnmuteAudioOutDevice():
#     ops.setMuteDevice(False, "out")

# def incVolAudioOut():
#     ops.xVolAudioOutDevice("5", "out")

# def decVolAudioOut():
#     ops.xVolAudioOutDevice("-5", "out")

# ## Audio Program Control
# def toggleMuteAudioOutProgram():
#     ops.toggleMuteProgram("out")

# def setMuteAudioOutProgram():
#     ops.setMuteProgram(True, "out")

# def setUnmuteAudioOutProgram():
#     ops.setMuteProgram(False, "out")

# def incVolAudioOutProgram():
#     ops.xVolProgram("5", "out")

# def decVolAudioOutProgram():
#     ops.xVolProgram("-5", "out")


# frm_main = None
# def setFrmMain(i_frm):
#     global frm_main
#     frm_main = i_frm
# def getFrmMain():
#     global frm_main
#     return frm_main

# default_audio_output = ""
# def setDefaultAudioOutputDevice(name):
#     global default_audio_output
#     default_audio_output = name
# def getDefaultAudioOutputDevice():
#     global default_audio_output
#     return default_audio_output

# default_audio_input = ""
# def setDefaultAudioInputDevice(name):
#     global default_audio_input
#     default_audio_input = name
# def getDefaultAudioInputDevice():
#     global default_audio_input
#     return default_audio_input

# curr_audio_prog = ""
# def setAudioProg(name):
#     global curr_audio_prog
#     curr_audio_prog = name
# def getAudioProg():
#     global curr_audio_prog
#     return curr_audio_prog

def setMute(name:str, mute:bool):
    print(f"Setting mute on {name} to {mute}")

def getMute(name:str, mute:bool):
    print(f"Setting mute on {name} to {mute}")