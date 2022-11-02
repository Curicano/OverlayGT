from os import remove
from configparser import ConfigParser
from pyAesCrypt import encryptFile, decryptFile


class Config():
    def __init__(self, directory):
        super().__init__()
        self.file = directory + "\settings."
        self.cfg = ConfigParser()
        self.crypter = Crypter(self.file)

    def read(self) -> list[str]:
        self.crypter.decrypt()
        self.cfg.read(self.file + "ini")
        self.crypter.encrypt()
        return self.cfg

    def write(self):
        self.crypter.decrypt()
        with open(self.file + "ini", "w+") as file:
            self.cfg.write(file)
        self.crypter.encrypt()


class Crypter():
    def __init__(self, file):
        super().__init__()
        self.file = file
        self.password = "0000"
        self.buffer = 512*1024

    def encrypt(self) -> None:
        encryptFile(
            self.file + "ini", self.file + "ccw", self.password, self.buffer)
        remove(self.file + "ini")

    def decrypt(self) -> None:
        decryptFile(
            self.file + "ccw", self.file + "ini", self.password, self.buffer)
        remove(self.file + "ccw")
