# Programa Python para testar
# velocidade da internet
import os
import speedtest

os.system("clear")  # Limpa a tela
try:
    print('''
  ___                  _   _____       _           
 / __|_ __  ___ ___ __| | |_   _|__ __| |_ ___ _ _ 
 \__ \ '_ \/ -_) -_) _` |   | |/ -_|_-<  _/ -_) '_|
 |___/ .__/\___\___\__,_|   |_|\___/__/\__\___|_|  
     |_|                                           
    
    ''')
    st = speedtest.Speedtest()

    opcao = int(input(''' [*] Qual velocidade você deseja testar:

 1) Velocidade de Download

 2) Velocidade de Upload

 3) Ping

 [+] Sua escolha: '''))

    print("\n [+] Processando seu comando.... \n\t Por favor, aguarde....\n")

    if opcao == 1:
        print(" [*] Sua velocidade de download é", st.download())

    elif opcao == 2:
        print(" [*] Sua velocidade de upload é", st.upload())

    elif opcao == 3:
        servernames = []
        st.get_servers(servernames)
        print(" [*] Seu resultado de ping é", st.results.ping)

    else:
        print(" [+] Por favor, insira uma opção válida!")

except KeyboardInterrupt:
    print("\n [-] CTRL + C detectado....Saindo...\n")

input("\n Pressione Enter para sair")
