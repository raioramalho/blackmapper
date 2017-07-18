import os
import sys
import fileinput
from logo import *
from mainmenu import *
from mainmenudefs import *
from subpowershellmenu import *
from subcommandmenu import *


def powershellmenu():
    os.system('cls')
    logo1()
    subpowershellmenu();



def backdorringmenu():
    os.system('cls')
    logo1()
    print ("Edit OK");



def commandmenu():
    os.system('cls')
    logo1()
    subcommandmenu()












def inserkeyinformenu():
    os.system('cls')
    logo1()
    print ("""
    Scripts for Arduino leonardo Using teeOnArdu lib like a RubberDucky From hak5
    The Arduino Leonardo uses the ATmega 32U4 chip, which has the ability to emulate a USB HID keyboard,
    and with that it has the property to execute any command once inserted into a USB port on the target machine.
    Payloads are being developed based on teensy microcontroller codes.
    The attacks are diverse, from a simple backdoor to a sotisficado attack of social engineering
    My payloads can have a bug's
    The IDE for This project is in download topic with all Dependences !

    README
    https://github.com/RamalhoSec/InserKey

    Compatible Boards:
    Leonardo - need a reset button, for send the sktech!!
    Leonardo Micro - need a reset button, for send the sktech!!
    Leonardo Pro Micro - need a reset button, for send the sktech!!
    Leonardo CJMCU Beetle - need a reset button, for send the sktech!!
    Leonardo Tiny USB ATMEGA32U4 - need a reset button, for send the sktech!!
    Teensy 2.0
    Teensy 2.0++
    Teensy 3.0
    Teensy 3.1+

    """);
