from crypto import password_encrypt
from getpass import getpass
import sys, time

try:
    def slowprint(s):
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(100 / 1000)

    slowprint("\033[92m [*] Criptografar Sua Mensagem :")
    print("=================================")

    def encrypt():
        message = input("\n\033[92m [*] Digite a mensagem para criptografar: ")
        password = getpass("\033[92m [*] Digite uma senha (a senha ficará oculta): ")
        repeated_password = getpass("\033[92m [*] Repita sua senha (a senha ficará oculta): ")

        if password != repeated_password:
            print("ERRO: As senhas não coincidem")
            return

        encrypted = password_encrypt(message=message, password=password)

        print(encrypted)

    if __name__ == "__main__":
        encrypt()

except KeyboardInterrupt:
    slowprint("\n\033[91m [-] Saindo...")

input(" Pressione Enter para sair")
