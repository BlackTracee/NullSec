import re
import os
import time
import platform
import base64

print("[*] Verificando módulos necessários...")
if platform.system().startswith("Linux"):
    try:
        import requests
    except ImportError:
        os.system("python3 -m pip install requests -q -q -q")
        import requests
    try:
        import termcolor
    except ImportError:
        os.system("python3 -m pip install termcolor -q -q -q")
        import termcolor
    try:
        from pystyle import *
    except:
        os.system("python3 -m pip install pystyle")
        from pystyle import *
    try:
        import colorama
    except ImportError:
        os.system("python3 -m pip install colorama")
        import colorama

elif platform.system().startswith("Windows"):
    try:
        import requests
    except ImportError:
        os.system("python -m pip install requests -q -q -q")
        import requests
    try:
        import termcolor
    except ImportError:
        os.system("python -m pip install termcolor -q -q -q")
        import termcolor
    try:
        from pystyle import *
    except:
        os.system("python -m pip install pystyle")
        from pystyle import *
    try:
        import colorama
    except ImportError:
        os.system("python -m pip install colorama")
        import colorama

colorama.deinit()
banner = Center.XCenter("""
                _______ _    _  _______     ____  __  __ ____
               / /  ___/ \  | |/ / ____|   / ___||  \/  / ___\\
              | || |_ / _ \ | ' /|  _| ____\___ \| |\/| \___ \| |
             < < |  _/ ___ \| . \| |__|_____|__) | |  | |___) )>>
              | ||_|/_/   \_\_|\_\_____|   |____/|_|  |_|____/
                            
""")

def check_net1():
    print(termcolor.colored("[*] Verificando conexão com a Internet...", 'cyan'))
    url = "https://www.google.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        print(termcolor.colored("[*] Conectado à Internet!", 'green'))
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
        menu()
    except (requests.ConnectionError, requests.Timeout) as exception:
        print(termcolor.colored("[*] Sem conexão com a Internet.", 'red'))

def menu():
    ans = True
    while ans:
        print(termcolor.colored("""
      1. Uso
      2. Enviar SMS
      3. Sair
      """, 'yellow'))
        ans = input(termcolor.colored("Escolha uma opção: ", 'cyan'))
        if ans == "1":
            print("\033c")
            usage1()
        elif ans == "2":
            print("\033c")
            main_check1()
        elif ans == "3":
            print("\033c")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            print(termcolor.colored("\n Obrigado por usar o Fake-SMS! Até mais.", 'red'))
            ans = None
        else:
            print(termcolor.colored("\n Opção inválida, tente novamente.", 'red'))

def usage1():
    print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
    print(termcolor.colored('''
      \n    1. O código do país deve ser sem o +
    2. Exemplo de código do país: 55 (Brasil)
    3. O número deve começar sem 0
    4. Exemplo completo: 5511998765432

    ..........ATENÇÃO: Só é permitido **1 SMS por dia**...........

      ''', 'magenta'))

def main_check1():
    print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
    x = input(termcolor.colored("\n[*] Digite o número de telefone: ", 'green'))
    y = input(termcolor.colored("\n[*] Digite sua mensagem: ", 'blue'))
    message = base64.b64decode('aHR0cHM6Ly90ZXh0YmVsdC5jb20vdGV4dA=='.encode('ascii')).decode('ascii')
    resp = requests.post(f'{message}', {
        'phone': x,
        'message': y,
        'key': 'textbelt',
    })
    print(termcolor.colored("\n[*] Enviando mensagem...", 'yellow'))
    time.sleep(2)
    z = str(resp.json())
    n = 'False'
    if re.search(n, z):
        print(termcolor.colored('\n[ X ] Mensagem NÃO enviada! Tente novamente mais tarde ou use uma VPN.',
                                'red'))
    else:
        print(termcolor.colored('\n[ ✔ ] Mensagem enviada com sucesso!', 'green'))

def op():
    try:
        if platform.system().startswith("Windows"):
            os.system("cls")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            check_net1()
        elif platform.system().startswith("Linux"):
            print("\033c")
            check_net1()
        else:
            print(termcolor.colored("Use apenas Windows ou Linux!", 'red'))
    except KeyboardInterrupt:
        print(termcolor.colored("\nVocê pressionou CTRL+C. Saindo...", 'red'))
        quit()

op()
input("Pressione ENTER para sair...")
