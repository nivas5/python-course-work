'''
                >>>> print(help("modules")) ("math") ("random") <<<<
                ------------------------------
import logic

logic.login()
logic.menu()
-----------------------------

********************
import logic as lg   ### AS means ALIAS. HERE, LG is LOGIC.

lg.login()
lg.menu()
********************
-----------------------------

from logic import menu,data

menu()
print(data)
-----------------------------

from logic import *

menu()
login()
print(data)
-----------------------------
'''
import logic as lg   ### AS means ALIAS. HERE, LG is LOGIC.

if lg.login():
    
    lg.menu()
