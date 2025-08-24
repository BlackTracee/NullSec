from crypto import senha_descriptografar
from getpass import getpass
import sys, time

try:
    def impressao_lenta(texto):
        for c in texto + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(100 / 1000)  # 0.1 segundos por caractere

    impressao_lenta("\033[92m [*] Descriptografar sua Mensagem :")
    print("=================================")

    def descriptografar():
        mensagem = input("\n\033[92m [*] Digite a Mensagem Criptografada: ")
        senha = getpass("\033[92m [*] Digite a Senha (a senha ficará oculta): ")
        descriptografado = senha_descriptografar(token=mensagem, senha=senha)
        print("\n\033[92m [*] Mensagem Descriptografada: ", descriptografado)

    if __name__ == "__main__":
        descriptografar()

except KeyboardInterrupt:
    impressao_lenta("\n\033[91m [-] Saindo...")

input("Pressione Enter para Sair")
