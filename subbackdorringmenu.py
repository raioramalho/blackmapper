from mainmenu import *
def subbackdorringmenu():
    from mainmenu import mainmenu
    print ("""
        1 - EDIT
        2 - EDIT
        3 - EDIT
        0 - Back to frist select menu
        """)

    submenuselect = raw_input(str("Say the option for show: "))

    if submenuselect == "1":
        print ("Edit ok")


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