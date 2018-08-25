from mainmenu import *
def subbackdorringmenu():
    from mainmenu import mainmenu
    print ("""
        1 - Disable windows 7/8/10 Defender
        2 - Iexplorer Fullscreen page attack
        3 - Paste Jacking Keyboard attack
        4 - Youtube roll fullscreen attack
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
        url= raw_input(str("Digite o link desejado: "))
        f = open('payloads/FullscreenIEpage.ino', 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace("PRANKURL", url)
        f = open('out/OUT-FullscreenIEpage.ino', 'w')
        f.write(newdata)
        f.close()
        os.system("start out/OUT-FullscreenIEpage.ino")


    elif submenuselect == "3":
        jacksite = raw_input(str("Digite o link do Postjack: "))
        f = open('payloads/PasteJackingattack.ino', 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace("JACKSITE", jacksite)
        f = open('out/OUT-PasteJackingattack.ino', 'w')
        f.write(newdata)
        f.close()
        os.system("start out/OUT-PasteJackingattack.ino")
        
     elif submenuselect == "4":
        url= raw_input(str("Digite o link do video desejado: "))
        f = open('payloads/Youtuberollfullpage.ino', 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace("PRANKURL", url)
        f = open('out/OUT-Youtuberollfullpage.ino', 'w')
        f.write(newdata)
        f.close()
        os.system("start out/OUT-Youtuberollfullpage.ino")


    elif submenuselect == "0":
        os.system('cls')
        logo1()
        mainmenu()
    else:
        os.system('cls')
        logo1()
        print ("Select one valid option!!")
        subbackdorringmenu();
