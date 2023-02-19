import func

frm_main = None
def setFrmMain(i_frm):
    global frm_main
    frm_main = i_frm
def getFrmMain():
    global frm_main
    return frm_main

default_audio_output = None
def setDefaultAudio(listName):
    global default_audio_output
    default_audio_output = listName

def getDefaultAudio():
    global default_audio_output
    return default_audio_output

audio_out = [["Set output", "", func.openDefaultsScreen],
             ["Audio options", "", func.openAudio],
             ["", "", None],
             ["", "", None],
             ["", "", None],
             ["", "", None]]

defaultAudio =  [["Headphones", "", func.setHeadphonesDefault],
                 ["Speakers", "", func.setSpeakersDefault],
                 ["", "", None],
                 ["", "", None],
                 ["", "", None],
                 ["", "", None]]

headphones_opts = [["Mute", "", func.muteHeadphones],
                   ["Inc Vol", "", func.incVolHeadphones],
                   ["Dec Vol", "", func.decVolHeadphones],
                   ["", "", None],
                   ["", "", None],
                   ["", "", None]]
default_audio_output = headphones_opts

speaker_opts = [["Mute", "", func.muteSpeakers],
                ["Inc Vol", "", func.incVolSpeakers],
                ["Dec Vol", "", func.decVolSpeakers],
                ["", "", None],
                ["", "", None],
                ["", "", None]]

mic_opts = [["Mute", "", func.muteMic],
            ["Inc Boost", "", func.incBoostMic],
            ["Dec Boost", "", func.decBoostMic],
            ["", "", None],
            ["", "", None],
            ["", "", None]]


