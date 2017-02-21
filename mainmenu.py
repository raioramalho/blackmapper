logo1()

import sys
import fileinput
from logo import *
from mainmenudefs import *
from subpowershellmenu import *
from subcommandmenu import *
def mainmenu():
    print ("""
    1 - Powershell vector attacks
    2 - Backdoor'ing exec attacks
    3 - Command vector attacks
    0 - InserKey Informmation
    """)

    menuselect = raw_input(str("Say the option for show: "))

    if menuselect == "0":
        inserkeyinformenu()
    elif menuselect == "1":
        powershellmenu()
    elif menuselect == "2":
        backdorringmenu()
    elif menuselect == "3":
        pranksmenu()
    else:
        os.system('cls')
        logo1()
        print ("Select one valid option!!")
        mainmenu()





