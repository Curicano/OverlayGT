from os import remove
from configparser import ConfigParser
from pyAesCrypt import encryptFile, decryptFile
from random import randrange


class Config():
    def __init__(self):
        super().__init__()
        self.file = "settings.ini"
        self.cfg = ConfigParser()
        self.crypter = Crypter()

    def read(self) -> list[str]:
        self.crypter.decrypt()
        self.cfg.read(self.file, encoding="utf-8")
        self.crypter.encrypt()

    def write(self):
        self.crypter.decrypt()
        with open(self.file, "w+", encoding="utf-8") as file:
            self.cfg.write(file)
        self.crypter.encrypt()


class Crypter():
    ccw_ext = ".ccw"
    ini_ext = ".ini"

    def __init__(self):
        super().__init__()
        self.file = "settings"
        self.password = "0000"
        self.buffer = 512*1024

    def encrypt(self) -> None:
        encryptFile(
            self.file + self.ini_ext, self.file + self.ccw_ext, self.password, self.buffer)
        remove(self.file + self.ini_ext)

    def decrypt(self) -> None:
        decryptFile(
            self.file + self.ccw_ext, self.file + self.ini_ext, self.password, self.buffer)
        remove(self.file + self.ccw_ext)
