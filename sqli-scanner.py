import requests

print('''\033[92m
  ___  ___  _     ___   ___      _          _           
 / __|/ _ \| |   |_ _| |   \ ___| |_ ___ __| |_ ___ _ _ 
 \__ \ (_) | |__  | |  | |) / -_)  _/ -_) _|  _/ _ \ '_|
 |___/\__\_\____||___| |___/\___|\__\___\__|\__\___/_|  
                                                                      
	coded by BlackTracee
	Github Page : https://github.com/BlackTracee
''')

def scan(url):
  payloads = ["' OR 1=1; --", "' OR '1'='1"]

  for payload in payloads:
    r = requests.get(url + payload)
    if r.status_code == 200:
      print(f"\033[92m [+] Possível vulnerabilidade de injeção de SQL encontrada em {url}\n")
    else:
      print("\033[91m [-] Vulnerabilidade não encontrada\n")
      break

scan(input("\033[92m [*] Insira a URL: "))

# scan("http://safe.com/page?id=1")

input(" [+] Enter para sair...")
