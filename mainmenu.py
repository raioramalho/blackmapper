import os
import sys
import fileinput
from logo import *
from mainmenudefs import *
from subpowershellmenu import *
from subbackdorringmenu import *
from subcommandmenu import *
logo1()
def mainmenu():
    print ("""
    1 - [OK]Powershell vector attacks
    2 - [OK]Backdoor'ing vector attacks
    3 - [OK]Command vector attacks
    4 - [X]Linux vector attacks
    5 - [X]Android vector attacks
    6 - [X]OSX vector attacks
    0 - [OK]InserKey Informmation
    """)

    menuselect = raw_input(str("Say the option for show: "))

    if menuselect == "0":
        inserkeyinformenu()
    elif menuselect == "1":
        powershellmenu()
    elif menuselect == "2":
        backdorringmenu()
    elif menuselect == "3":
        commandmenu()
    else:
        os.system('cls')
        logo1()
        print ("Select one valid option!!")
        mainmenu()





