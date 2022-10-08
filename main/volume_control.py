from ctypes import POINTER, cast
from pycaw.pycaw import (
    AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume)
from comtypes import CLSCTX_ALL


class V(AudioUtilities):
    def __init__(self):
        super().__init__()

    def get_speakers(self):
        self.devices = AudioUtilities.GetSpeakers()
        self.interface = self.devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = cast(self.interface, POINTER(IAudioEndpointVolume))
        self.value = round((self.volume.GetMasterVolumeLevelScalar())*100)
        return self.value

    def get_sessions(self):
        self.sess = self.GetAllSessions()
        return self.sess

    def set_volume_speakers(self, value):
        self.get_speakers()
        self.volume.SetMasterVolumeLevelScalar(value/100, None)

    def set_volume_sessions(self, value, name):
        self.get_sessions()
        for i in range(self.sess.__len__()):
            if self.sess[i].Process and self.sess[i].Process.name() == name:
                volume = self.sess[i]._ctl.QueryInterface(ISimpleAudioVolume)
                volume.SetMasterVolume(value/100, None)
                break
            else:
                continue

    def get_volume_speakers(self):
        self.get_speakers()
        value = round((self.volume.GetMasterVolumeLevelScalar())*100)
        return value

    def get_volume_session(self, name):
        self.get_sessions()
        for i in range(self.sess.__len__()):
            if self.sess[i].Process and self.sess[i].Process.name() == name:
                volume = self.sess[i]._ctl.QueryInterface(
                    ISimpleAudioVolume)
                value = round((volume.GetMasterVolume())*100)
                return value
            else:
                continue
