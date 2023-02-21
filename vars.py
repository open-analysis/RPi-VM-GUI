import func

frm_main = None
def setFrmMain(i_frm):
    global frm_main
    frm_main = i_frm
def getFrmMain():
    global frm_main
    return frm_main

# Needs to be set by the incoming data
default_audio_output = "Headphones"
def setDefaultAudioOutput(name):
    global default_audio_output
    default_audio_output = name
def getDefaultAudioOutput():
    global default_audio_output
    return default_audio_output

default_audio_input = "Microphone"
def setDefaultAudioInput(listName):
    global default_audio_input
    default_audio_input = listName
def getDefaultAudioInput():
    global default_audio_input
    return default_audio_input

curr_audio_prog = ""
def setAudioProg(name):
    global curr_audio_prog
    curr_audio_prog = name
def getAudioProg():
    global curr_audio_prog
    return curr_audio_prog

top = [["speakers", "", func.openAudioOutputOptions], 
       ["microphone", "", func.openAudioInputOptions],
       ["", "", None],
       ["", "", None],
       ["", "", None],
       ["", "", None]]

audio_out = [["Set output", "", func.openDefaultOutputScreen],
             ["Audio options", "", func.openAudioOutput],
             ["Audio Mixer", "", func.openAudioProgs],
             ["", "", None],
             ["", "", None],
             ["", "", None]]

audio_in =  [["Set input", "", func.openDefaultInputScreen],
             ["Audio options", "", func.openAudioInput],
             ["", "", None],
             ["", "", None],
             ["", "", None],
             ["", "", None]]

#########################                  These kinds of functions (setting variables) are going to be a problem
defaultAudioOutput =  [["Headphones", "", func.setHeadphonesDefault],
                       ["Speakers", "", func.setSpeakersDefault],
                       ["", "", None],
                       ["", "", None],
                       ["", "", None],
                       ["", "", None]]

#########################                  These kinds of functions (setting variables) are going to be a problem
defaultAudioInput =  [["Microphone", "", func.setMicropohoneDefault],
                       ["", "", None],
                       ["", "", None],
                       ["", "", None],
                       ["", "", None],
                       ["", "", None]]

audio_output_opts = [["Mute", "", func.toggleMuteAudioOut],
                     ["Inc Vol", "", func.incVolAudioOut],
                     ["", "", None],
                     ["", "", None],
                     ["Dec Vol", "", func.decVolAudioOut],
                     ["", "", None]]

audio_input_opts = [["Mute", "", func.toggleMuteMic],
                    ["Inc Boost", "", func.incBoostMic],
                    ["", "", None],
                    ["", "", None],
                    ["Dec Boost", "", func.decBoostMic],
                    ["", "", None]]

#########################        This is temporary
audio_progs = [["Spotify", "", func.setProgSpotify],
               ["Discord", "", func.setProgDiscord],
               ["Firefox", "", func.setProgFirefox],
               ["", "", None],
               ["", "", None],
               ["", "", None]]

audio_prog_opts = [["Toggle Mute", "", func.toggleMuteAudioProgram],
                   ["Mute", "", func.setMuteAudioProgram],
                   ["Inc Vol", "", func.incVolAudioProgram],
                   ["", "", None],
                   ["Unmute", "", func.setUnmuteAudioProgram],
                   ["Dec Vol", "", func.decVolAudioProgram]]
