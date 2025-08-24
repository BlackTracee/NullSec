import os
import sys
import socket
import datetime
import time
import psutil

ARQUIVO = os.path.join(os.getcwd(), "informacoes_rede.log")

# criando arquivo de log no diretório atual
# getcwd pega o diretório de trabalho atual
# função os.path.join define o caminho

try:
    def ping():
        # para testar ping em um IP específico
        try:
            socket.setdefaulttimeout(3)
            # se houver interrupção de dados por 3 segundos, 
            # a parte except será executada

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # AF_INET: família de endereços
            # SOCK_STREAM: tipo TCP

            host = "8.8.8.8"
            porta = 53

            endereco_servidor = (host, porta)
            s.connect(endereco_servidor)

        except OSError as erro:
            return False
            # retorna False em caso de interrupção de conexão

        else:
            s.close()
            # fecha a conexão após comunicação com o servidor
            return True


    def calcular_tempo(inicio, fim):
        # calcula o tempo de indisponibilidade e converte em segundos
        diferenca = fim - inicio
        segundos = float(str(diferenca.total_seconds()))
        return str(datetime.timedelta(seconds=segundos)).split(".")[0]


    def primeira_verificacao():
        # verifica se o sistema já estava conectado à internet

        if ping():
            conectado = "\n \033[92m✔️✔️✔️ CONEXÃO ADQUIRIDA\n"
            print(conectado)
            hora_conexao = datetime.datetime.now()
            msg_conexao = " \033[92m✔️✔️✔️ Conexão adquirida em: " + \
                str(hora_conexao).split(".")[0]
            print(msg_conexao)

            with open(ARQUIVO, "a") as arquivo:
                # escreve no arquivo de log
                arquivo.write(conectado)
                arquivo.write(msg_conexao)

            return True

        else:
            nao_conectado = "\n\033[91m ❌❌❌ CONEXÃO NÃO ADQUIRIDA\n"
            print(nao_conectado)

            with open(ARQUIVO, "a") as arquivo:
                arquivo.write(nao_conectado)
            return False


    def principal():
        # função principal que chama outras funções
        inicio_monitoramento = datetime.datetime.now()
        msg_inicio = "\033[92m [+] Monitoramento iniciado em: " + \
            str(inicio_monitoramento).split(".")[0]

        if primeira_verificacao():
            print(msg_inicio)
        else:
            while True:
                if not ping():
                    time.sleep(1)
                else:
                    primeira_verificacao()
                    print(msg_inicio)
                    break

        with open(ARQUIVO, "a") as arquivo:
            arquivo.write("\n")
            arquivo.write(msg_inicio + "\n")

        while True:
            # loop infinito monitorando a conexão
            if ping():
                time.sleep(5)
            else:
                hora_desconexao = datetime.datetime.now()
                msg_falha = "\033[91m ❌❌❌ Desconectado em: " + str(hora_desconexao).split(".")[0]
                print(msg_falha)

                with open(ARQUIVO, "a") as arquivo:
                    arquivo.write(msg_falha + "\n")

                while not ping():
                    time.sleep(1)

                hora_reconexao = datetime.datetime.now()
                msg_reconexao = "\033[92m Reconectado em: " + str(hora_reconexao).split(".")[0]

                tempo_indisponivel = calcular_tempo(hora_desconexao, hora_reconexao)
                msg_indisponibilidade = " \033[92mA conexão ficou indisponível por: " + tempo_indisponivel

                print(msg_reconexao)
                print(msg_indisponibilidade)

                with open(ARQUIVO, "a") as arquivo:
                    arquivo.write(msg_reconexao + "\n")
                    arquivo.write(msg_indisponibilidade + "\n")


    def impressao_lenta(texto):
        for c in texto + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.1)

    impressao_lenta(" \n\033[93m Pressione Ctrl+C para iniciar o monitoramento de rede")
    impressao_lenta(" \n\033[91m Pressione Ctrl+C duas vezes para sair da ferramenta")
    principal()

except KeyboardInterrupt:
    impressao_lenta("\n\033[90m [*] Ctrl+C detectado....Entrando no modo de monitoramento de rede.... ")

# Monitoramento de tráfego de rede
ATRASO_ATUALIZACAO = 1 # em segundos
try:
    def obter_tamanho(bytes):
        """
        Retorna tamanho em formato legível
        """
        for unidade in ['', 'K', 'M', 'G', 'T', 'P']:
            if bytes < 1024:
                return f"{bytes:.2f}{unidade}B"
            bytes /= 1024

    io = psutil.net_io_counters()
    bytes_enviados, bytes_recebidos = io.bytes_sent, io.bytes_recv

    impressao_lenta("\n \033[92m      [+] Monitoramento da rede em andamento: ")
    time.sleep(2)

    while True:
        time.sleep(ATRASO_ATUALIZACAO)
        io_novo = psutil.net_io_counters()
        envio, recebimento = io_novo.bytes_sent - bytes_enviados, io_novo.bytes_recv - bytes_recebidos

        print(f"Upload: {obter_tamanho(io_novo.bytes_sent)}   "
              f", Download: {obter_tamanho(io_novo.bytes_recv)}   "
              f", Velocidade Upload: {obter_tamanho(envio / ATRASO_ATUALIZACAO)}/s   "
              f", Velocidade Download: {obter_tamanho(recebimento / ATRASO_ATUALIZACAO)}/s      ", end="\r")

        bytes_enviados, bytes_recebidos = io_novo.bytes_sent, io_novo.bytes_recv

except KeyboardInterrupt:
    impressao_lenta("\n\n\033[91m [-] Ctrl+C detectado.....Saindo.....")    

time.sleep(2)
