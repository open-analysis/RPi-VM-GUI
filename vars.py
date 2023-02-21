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
curr_audio_prog = ""
def setAudioProg(name):
    global curr_audio_prog
    curr_audio_prog = name
def getAudioProg():
    global curr_audio_prog
    return curr_audio_prog

top = [["speakers", "", func.openAudioOptions], 
       ["microphone", "", func.openMics],
       ["", "", None],
       ["", "", None],
       ["", "", None],
       ["", "", None]]

audio_out = [["Set output", "", func.openDefaultsScreen],
             ["Audio options", "", func.openAudio],
             ["Audio Mixer", "", func.openAudioProgs],
             ["", "", None],
             ["", "", None],
             ["", "", None]]

defaultAudio =  [["Headphones", "", func.setHeadphonesDefault],
                 ["Speakers", "", func.setSpeakersDefault],
                 ["", "", None],
                 ["", "", None],
                 ["", "", None],
                 ["", "", None]]

headphones_opts = [["Mute", "", func.toggleMuteHeadphones],
                   ["Inc Vol", "", func.incVolHeadphones],
                   ["", "", None],
                   ["", "", None],
                   ["Dec Vol", "", func.decVolHeadphones],
                   ["", "", None]]
default_audio_output = headphones_opts

speaker_opts = [["Mute", "", func.toggleMuteSpeakers],
                ["Inc Vol", "", func.incVolSpeakers],
                ["", "", None],
                ["", "", None],
                ["Dec Vol", "", func.decVolSpeakers],
                ["", "", None]]

mic_opts = [["Mute", "", func.toggleMuteMic],
            ["Inc Boost", "", func.incBoostMic],
            ["", "", None],
            ["", "", None],
            ["Dec Boost", "", func.decBoostMic],
            ["", "", None]]

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
