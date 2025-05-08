import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)

style1 = Fore.RED + Back.WHITE + Style.BRIGHT
style2 = Fore.BLACK + Back.RED + Style.DIM

print(style1 + "My Name is Ashok Bhatt")
print(style2 + "My Name is Irfan Ansari")
print("Correct")