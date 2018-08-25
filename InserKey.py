#Created by Dropping - awak3ned@protonmail.com
#Payloads: x | Original Repo github.com/RamalhoSec/InserKey-tool.git
#Bitcoin = 3DppKRbA9Um3z4wnmVtkqnETnvwsip7WkC

import os
import sys
import string
from mainmenu import *

op = raw_input(str("Deseja limpar os Payloads criados (S/N)?:"))
if op == "S":
    os.system('del out\*.* /s /q')
    arq = open('out\README.md', 'w')
    texto = []
    texto.append('Here is when out-put Gennerated Payloads\n')
    arq.writelines(texto)
    arq.close()
else:
    print("ok")
    

mainmenu()
