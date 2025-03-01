from db import conectar
from colorama import Fore,init
import os
init(autoreset=True)

os.system("cls")
conn=conectar()
if conn:
    print(Fore.GREEN+"✅ test passed DB...")
else:
    print(Fore.RED+"❌ test error...")