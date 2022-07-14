#   Handling import weirdness
import sys, os
from time import sleep
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
#   Imports
from Modules.WriteCode import AutoText

a = AutoText()
sleep(5)
a.file = 'H:\\Dokumenty\\GitHub\\PYTHON_VENV\\AnimateCode\\to_read'
a.Write(1)
