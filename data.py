class Audio():
    m_name = ""
    m_img = ""
    m_volume = 0
    m_mute = True


    def __init__(self, name="", img="", volume=0, mute=False):
        self.m_name = name
        self.m_img = img
        self.m_volume = volume
        self.m_mute = mute

    def setName(self, name:str):
        self.m_name = name

    def setImg(self, img:str):
        self.m_img = img

    def setVolume(self, volume:int):
        self.m_volume = volume

    def setMute(self, mute:bool):
        self.m_mute = mute
        print(f"Mute: {self.m_mute}")

    def getName(self) -> str:
        return self.m_name
    
    def getImg(self) -> str:
        return self.m_img

    def getVolume(self) -> int:
        return self.m_volume

    def getMute(self) -> bool:
        return self.m_mute


class AudioDevice(Audio):
    m_default_device = False
    m_output = True

    def __init__(self, name="", img="", volume=0, mute=False):
        super().__init__(name=name, img=img, volume=volume, mute=mute)

    def setDefault(self, is_default):
        self.m_default_device = is_default

    def toggleDefault(self):
        self.m_default_device = not self.m_default_device

    def setOutput(self, is_output):
        self.m_output = is_output

    def getDefault(self) -> bool:
        return self.m_default_device

    def getOutput(self) -> bool:
        return self.m_output

class AudioProgram(Audio):

    def __init__(self, name="", img="", volume=0, mute=False):
        super().__init__(name=name, img=img, volume=volume, mute=mute)

        
