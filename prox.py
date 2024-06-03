import os
os.system("pip3 install termcolor")
os.system("pip3 install colorama")
os.system("pip3 install ascii_magic")
os.system("pip3 install pillow")
os.system("pip3 install tabulate")
import colorama
from colorama import Fore
import subprocess
from colorama import Back
import tabulate
import re
import sys
import time
import subprocess
import termcolor
from termcolor import colored
from time import sleep
from PIL import ImageEnhance
from ascii_magic import AsciiArt

def ascii_banner():
    try:
        my_art = AsciiArt.from_url('https://i.postimg.cc/Jhbhr2hT/Screenshot-2024-04-21-at-05-13-59-e21459f8019688f030e3fd2ddf70830b-jpg-JPEG-Image-338-600-pixels.png')
    except OSError as e:
        print(f'Could not load the image, server said: {e.code} {e.msg}')
    my_art.to_terminal()

def clear_screen():
    subprocess.run('clear' if os.name == 'posix' else 'cls')
    
def main():
    clear_screen()
    ascii_banner()
    print("\n")
    print(Fore.RED + "                                   ██▓    ▓█████ ▄▄▄       ██ ▄█▀  ██████ ▓█████ ▓█████  ██ ▄█▀" + Fore.RESET)
    print(Fore.RED + "                                  ▓██▒    ▓█   ▀▒████▄     ██▄█▒ ▒██    ▒ ▓█   ▀ ▓█   ▀  ██▄█▒ " + Fore.RESET)
    print(Fore.RED + "                                  ▒██░    ▒███  ▒██  ▀█▄  ▓███▄░ ░ ▓██▄   ▒███   ▒███   ▓███▄░ " + Fore.RESET)
    print(Fore.RED + "                                  ▒██░    ▒▓█  ▄░██▄▄▄▄██ ▓██ █▄   ▒   ██▒▒▓█  ▄ ▒▓█  ▄ ▓██ █▄ " + Fore.RESET)
    print(Fore.RED + "                                  ░██████▒░▒████▒▓█   ▓██▒▒██▒ █▄▒██████▒▒░▒████▒░▒████▒▒██▒ █▄" + Fore.RESET)
    print(Fore.RED + "                                  ░ ▒░▓  ░░░ ▒░ ░▒▒   ▓▒█░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░░░ ▒░ ░░░ ▒░ ░▒ ▒▒ ▓▒" + Fore.RESET)
    print(Fore.RED + "                                  ░ ░ ▒  ░ ░ ░  ░ ▒   ▒▒ ░░ ░▒ ▒░░ ░▒  ░ ░ ░ ░  ░ ░ ░  ░░ ░▒ ▒░" + Fore.RESET)
    print(Fore.RED + "                                    ░ ░      ░    ░   ▒   ░ ░░ ░ ░  ░  ░     ░      ░   ░ ░░ ░ " + Fore.RESET)
    print(Fore.RED + "                                      ░  ░   ░  ░     ░  ░░  ░         ░     ░  ░   ░  ░░  ░   " + Fore.RESET)
    print("                                       \033[91m-----------------\033[96mProxy Scraper\033[91m-----------------\033[0m")

    print(" ")
    option = input("   \033[0mType \033[95mSTART\033[0m) : ")
    if option == "START":
        subprocess.run(["git", "clone", "https://github.com/AnonCatalyst/LuminaProxy.git"])
        os.chdir("LuminaProxy")
        clear_screen()
        ascii_banner()
        print(colored("INSTALLING DEPENDENCIES...", 'red', attrs=['reverse', 'blink', 'bold']))
        os.system("python3 install.py")
        subprocess.run(["python3", "lumina.py"])
    

if __name__ == "__main__":
    main()
