#!/usr/bin/env python

import subprocess

print(r'''   
  __  __   _   ___     ___ _  _   _   _  _  ___ ___ ___ 
 |  \/  | /_\ / __|__ / __| || | /_\ | \| |/ __| __| _ \
 | |\/| |/ _ \ (_|___| (__| __ |/ _ \| .` | (_ | _||   /
 |_|  |_/_/ \_\___|   \___|_||_/_/ \_\_|\_|\___|___|_|_\
                                                         ''' )

try:
    interface = input("\033[92m [*] Por favor, especifique a interface: ")
    novo_mac = input("\033[92m [*] Por favor, especifique o novo MAC: ")

    print(" [!] Alterando o ENDEREÇO MAC da interface " + interface + " para " + novo_mac)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + novo_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)
except KeyboardInterrupt:
    print("\n\033[91m [-] Saindo....")

input("\n [+] Pressione Enter para sair")
