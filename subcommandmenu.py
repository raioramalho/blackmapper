from mainmenu import *
def subcommandmenu():
    print ("""
        1 - Payload local dns poisoning
        2 - Password allusrpass changer
        3 - edit
        0 - Back to frist select menu
        """)

    submenuselect = raw_input(str("Say the option for show: "))

    if submenuselect == "1":
        print ("local dns poisoning ok")
        targetip = raw_input(str("Digite o ip alvo : "))
        print (targetip)
        targetlink = raw_input(str("Digite o link desejado : "))
        print (targetlink)

        f = open('payloads/Localdns-poising.ino', 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace("IPDLVR", targetip).replace("LINKDLVR", targetlink)
        f = open('out/OUT-Localdns-poising.ino', 'w')
        f.write(newdata)
        f.close()
        os.system("start out/OUT-Localdns-poising.ino")


    elif submenuselect == "2":
        print("user pass changer ok");
        newpass = raw_input(str("Digite a senha desejada : "))
        print (newpass)

        f = open('payloads/Passlusrchanger.ino', 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace("NEWPASS", newpass)
        f = open('out/OUT-Passlusrchanger.ino', 'w')
        f.write(newdata)
        f.close()
        os.system("start out/OUT-Passlusrchanger.ino")


    elif submenuselect == "3":
        print ("edit ok")



    elif submenuselect == "0":
        os.system('cls')
        logo1()
        mainmenu()
    else:
        os.system('cls')
        logo1()
        print ("Select one valid option!!")
        subcommandmenu();
