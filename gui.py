import shutil
import sys
import models
from constant import *

main = models.Menu(None, MAINMENU)

telmenu = models.Menu(main, TELMENU)

main.show_menu()
