class Audio():
    m_focused_audio = None
    m_name = ""
    m_volume = 0
    m_mute = True


    def __init__(self, name="", volume=0, mute=False):
        self.m_name = name
        self.m_volume = volume
        self.m_mute = mute

    def setName(self, name:str):
        self.m_name = name

    def setVolume(self, volume:int):
        self.m_volume = volume

    def setMute(self, mute:bool):
        self.m_mute = mute
        print(f"Mute: {self.m_mute}")

    def getName(self) -> str:
        return self.m_name

    def getVolume(self) -> int:
        return self.m_volume

    def getMute(self) -> bool:
        return self.m_mute


class AudioDevice(Audio):
    def __init__(self, name="", volume=0, mute=False):
        super().__init__(name=name)

    def setDefault(self):
        pass

class AudioProgram(Audio):

    def __init__(self, name="", volume=0, mute=False):
        super().__init__()

        
