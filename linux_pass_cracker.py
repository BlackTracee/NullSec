import crypt
import time

try:
    # Abre o arquivo de senhas
    password = open("password.txt", 'r')
    
    for passwd in password.readlines():
        passwd = passwd.strip("\n").strip("\r")  # Remove quebras de linha e retornos de carro
        var = crypt.crypt(passwd, "$6$" + "8HOLitkI")  # Criptografa a senha usando SHA-512
        
        # Compara a senha criptografada com o hash alvo
        if var == "$6$8HOLitkI$9HECw2MBzISI1O.RoyJdfugy4VHsTOU4RDTewcFECnZdWLpmtVwNo5a1/hg2kw4Qu74F08eMEwpLdK1eovfEd/":
            print("\033[94m [+] Senha encontrada: ", passwd)
            break
        else:
            print("\033[92m [*] Tentando...")

except KeyboardInterrupt:
    print("\n \033[91m[-] Interrompido pelo teclado")

time.sleep(4)
