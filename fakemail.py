import pyperclip
import requests
import random
import string
import time
import sys
import re
import os

# API do serviço de e-mail temporário
API = 'https://www.1secmail.com/api/v1/'

# Lista de domínios disponíveis
domainList = ['1secmail.com', '1secmail.net', '1secmail.org']
domain = random.choice(domainList)

# Função para "digitar" o texto devagar
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

try:
    # Banner ASCII
    def banner():
        print(r'''                                                                               
            ▄████  ██   █  █▀ ▄███▄   █▀▄▀█ ██   ▄█ █     
            █▀   ▀ █ █  █▄█   █▀   ▀  █ █ █ █ █  ██ █     
            █▀▀    █▄▄█ █▀▄   ██▄▄    █ ▄ █ █▄▄█ ██ █     
            █      █  █ █  █  █▄   ▄▀ █   █ █  █ ▐█ ███▄  
             █        █   █   ▀███▀      █     █  ▐     ▀ 
              ▀      █   ▀              ▀     █           
                    ▀                        ▀                   
              
        ''')

    # Gerar nome de usuário aleatório
    def generateUserName():
        name = string.ascii_lowercase + string.digits
        username = ''.join(random.choice(name) for i in range(10))
        return username

    # Extrair login e domínio do e-mail
    def extract():
        getUserName = re.search(r'login=(.*)&', newMail).group(1)
        getDomain = re.search(r'domain=(.*)', newMail).group(1)
        return [getUserName, getDomain]

    # Função para sobrescrever a linha de status no terminal
    def print_statusline(msg: str):
        last_msg_length = len(print_statusline.last_msg) if hasattr(print_statusline, 'last_msg') else 0
        print(' ' * last_msg_length, end='\r')
        print(msg, end='\r')
        sys.stdout.flush()
        print_statusline.last_msg = msg

    # Deletar a caixa de e-mail
    def deleteMail():
        url = 'https://www.1secmail.com/mailbox'
        data = {
            'action': 'deleteMailbox',
            'login': f'{extract()[0]}',
            'domain': f'{extract()[1]}'
        }

        print_statusline("Apagando sua caixa de e-mail - " + mail + '\n')
        req = requests.post(url, data=data)

    # Checar se chegaram novos e-mails
    def checkMails():
        reqLink = f'{API}?action=getMessages&login={extract()[0]}&domain={extract()[1]}'
        req = requests.get(reqLink).json()
        length = len(req)
        if length == 0:
            print_statusline("\033[91m Sua caixa de entrada está vazia. Verificando novamente a cada 5 segundos...")
        else:
            idList = []
            for i in req:
                for k, v in i.items():
                    if k == 'id':
                        mailId = v
                        idList.append(mailId)

            x = 'e-mails' if length > 1 else 'e-mail'
            print_statusline(f"\033[92m Você recebeu {length} {x}. (Caixa será verificada automaticamente a cada 5 segundos.)")

            # Criar pasta "All Mails" se não existir
            current_directory = os.getcwd()
            final_directory = os.path.join(current_directory, r'All Mails')
            if not os.path.exists(final_directory):
                os.makedirs(final_directory)

            # Salvar os e-mails em arquivos .txt
            for i in idList:
                msgRead = f'{API}?action=readMessage&login={extract()[0]}&domain={extract()[1]}&id={i}'
                req = requests.get(msgRead).json()
                for k, v in req.items():
                    if k == 'from':
                        sender = v
                    if k == 'subject':
                        subject = v
                    if k == 'date':
                        date = v
                    if k == 'textBody':
                        content = v

                mail_file_path = os.path.join(final_directory, f'{i}.txt')

                with open(mail_file_path, 'w', encoding="utf-8") as file:
                    file.write("De: " + sender + '\n' +
                               "Para: " + mail + '\n' +
                               "Assunto: " + subject + '\n' +
                               "Data: " + date + '\n' +
                               "Conteúdo: " + content + '\n')

    # Início do programa
    banner()
    userInput1 = input("\n \033[94m[+] Deseja usar um nome de usuário personalizado? (Y/N): ").capitalize()

    try:
        if userInput1 == 'Y' or userInput1 == 'y':
            userInput2 = input("\n \033[90m[+] Digite o nome de usuário desejado: ")
            newMail = f"{API}?login={userInput2}&domain={domain}"
            reqMail = requests.get(newMail)
            mail = f"{extract()[0]}@{extract()[1]}"
            pyperclip.copy(mail)
            slowprint("\n \033[93m Seu e-mail temporário é " + mail + " (Copiado para a área de transferência.)\n")
            slowprint(f"\033[95m ---------------------------- | Caixa de entrada de {mail}| ----------------------------\n")
            while True:
                checkMails()
                time.sleep(5)

        if userInput1 == 'N' or userInput1 == 'n':
            newMail = f"{API}?login={generateUserName()}&domain={domain}"
            reqMail = requests.get(newMail)
            mail = f"{extract()[0]}@{extract()[1]}"
            pyperclip.copy(mail)
            print("\n \033[92mSeu e-mail temporário é " + mail + " (Copiado para a área de transferência.)\n")
            print(f"\033[91m ---------------------------- | Caixa de entrada de {mail} | ----------------------------\n")
            while True:
                checkMails()
                time.sleep(5)

    except KeyboardInterrupt:
        deleteMail()
        print("\n\033[98m Programa interrompido")
        os.system('cls' if os.name == 'nt' else 'clear')

except KeyboardInterrupt:
    slowprint("\n\033[91m [-] Saindo....")
time.sleep(2)
