from PyQt5.QtCore import QDir
from ..basic_game import BasicGame


class arma3Game(BasicGame):

    Name = "Arma 3 Support Plugin"
    Author = "BrandonM4"
    Version = "1.0.0a"

    GameName = "Arma 3"
    GameShortName = "arma3"
    GameBinary = "arma3.exe"
    GameDataPath = "Expansion\Addons"
    GameSaveExtension = "sav"
    GameSteamId = 107410

