from process_interface import ProcessInterface
from infobox import InfoBoxClass
from JSONMethods import JSON
from OptionsMenu import Options
import os, sys

process = ProcessInterface()
info = InfoBoxClass
options = Options
Jayson = JSON

fileName = "DS3C_Savedata"
jsonData = {}
sendToDir = os.getenv('APPDATA')
path = "./"

fonts = []
import matplotlib.font_manager as fm
for f in fm.fontManager.ttflist:          # lists all font families
    fonts.append(f.name)

ontop = False
ontop2 = False
firstclick = True

fileName = "DS3C_Savedata"
actualData = 0
colourCodeFont = "white"
colourCodeBack = "green"
txtFont = "Comic Sans MS"


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try: 
        # PyInstaller creates a temp folder and stores path in _MEIPASS             # thanks stackoverflow :)
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)