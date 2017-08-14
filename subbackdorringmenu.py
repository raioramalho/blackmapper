from mainmenu import *
def subbackdorringmenu():
    from mainmenu import mainmenu
    print ("""
        1 - Disable windows 7/8/10 Defender
        2 - EDIT
        3 - EDIT
        0 - Back to frist select menu
        """)

    submenuselect = raw_input(str("Say the option for show: "))

    if submenuselect == "1":
        data= "RamalhoSec"
        f = open('payloads/Disable-winDefender.ino', 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace("CREDS", data)
        f = open('out/OUT-Disable-winDefender.ino', 'w')
        f.write(newdata)
        f.close()
        os.system("start out/OUT-Disable-winDefender.ino")


    elif submenuselect == "2":
        print ("Edit ok")


    elif submenuselect == "3":
        print ("Edit ok")


    elif submenuselect == "0":
        os.system('cls')
        logo1()
        mainmenu()
    else:
        os.system('cls')
        logo1()
        print ("Select one valid option!!")
        subbackdorringmenu();
