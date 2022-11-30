import os,sys
from platform import platform
def cleaning():
     if sys.platform.startswith("win"):
        os.system("cls")
     elif sys.platform.startswith("darwin"):
            os.system("clear")
     elif sys.platform.startswith("linux"):
            os.system("clear")
cleaning()
