import socket
from sys import modules
import time
import threading
from queue import Queue

logo = '''
    ___________   _____                                 
   |_   _| ___ \ /  ___|                                
     | | | |_/ / \ `--.  ___ __ _ _ __  _ __   ___ _ __ 
     | | |  __/   `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
    _| |_| |     /\__/ / (_| (_| | | | | | | |  __/ |   
    \___/\_|     \____/ \___\__,_|_| |_|_| |_|\___|_|   
                      	
'''
print(logo)
print("Espere, estamos construindo o código...") 

socket.setdefaulttimeout(0.25)  # Define tempo máximo de espera para conexão
lock = threading.Lock()

ip_address = input('Endereço IP ou URL do site: ')
host = socket.gethostbyname(ip_address)
print('Digitalizando o endereço IP:', host)

def scan(porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = sock.connect((host, porta))
        with lock:
            print(porta, 'aberta')
        con.close()
    except:
        pass

def execute():
    while True:
        worker = queue.get()
        scan(worker)
        queue.task_done()
      
queue = Queue()
start_time = time.time()
   
# Cria 100 threads para escanear portas
for x in range(100):
    thread = threading.Thread(target=execute)
    thread.daemon = True
    thread.start()
   
# Adiciona portas de 1 a 499 na fila de trabalho
for worker in range(1, 500):
    queue.put(worker)
   
queue.join()

print('Tempo gasto:', time.time() - start_time)
print("Obrigado por usar nossa ferramenta :>")
input("Aperte Enter para continuar: ")
