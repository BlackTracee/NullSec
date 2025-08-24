import random

tamanho_senha = 12

caracteres = "abcde12345"

senha = ""   

for i in range(tamanho_senha):
    senha += random.choice(caracteres)

print("Senha gerada: {}".format(senha))
input(" [+] Pressione Enter para sair")
