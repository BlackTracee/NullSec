import sys, time

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)

try:
    executando = True
    print("Calculadora")
    print("================================")
    
    while executando:
        slowprint("\033[95m 1 = Adição")
        slowprint("\033[95m 2 = Subtração")
        slowprint("\033[95m 3 = Multiplicação")
        slowprint("\033[95m 4 = Divisão")
        slowprint("\033[95m 5 = Sair do programa")
        
        cmd = int(input("\n\033[92m [*] Escolha uma opção: "))
        
        if cmd == 1:
            slowprint("\n Adição")
            print("================================")
            primeiro = int(input(" [+] Digite o primeiro número: "))
            segundo = int(input(" [*] Digite o segundo número: "))
            resultado = primeiro + segundo
            slowprint("\n\033[93m OH! É fácil de calcular")
            print(f"O resultado de {primeiro} + {segundo} = {resultado}\n")
            
        elif cmd == 2:
            slowprint("\n Subtração")
            print("================================")
            primeiro = int(input(" [*] Digite o primeiro número: "))
            segundo = int(input(" [*] Digite o segundo número: "))
            resultado = primeiro - segundo
            slowprint("\n\033[93m OH! É fácil de calcular")
            print(f"O resultado de {primeiro} - {segundo} = {resultado}\n")
            
        elif cmd == 3:
            slowprint("\n Multiplicação")
            print("================================")
            primeiro = int(input(" [*] Digite o primeiro número: "))
            segundo = int(input(" [*] Digite o segundo número: "))
            resultado = primeiro * segundo
            slowprint("\n\033[93m OH! É fácil de calcular")
            print(f"O resultado de {primeiro} x {segundo} = {resultado}\n")
            
        elif cmd == 4:
            slowprint("\n Divisão")
            print("================================")
            primeiro = int(input(" [*] Digite o primeiro número: "))
            segundo = int(input(" [*] Digite o segundo número: "))
            slowprint("\n\033[93m OH! É fácil de calcular")
            resultado = primeiro / segundo
            print(f"O resultado de {primeiro} ÷ {segundo} = {resultado}\n")
            
        elif cmd == 5:
            slowprint("\n ***NullSec deseja um bom dia! :D ***")
            executando = False
            
        else:
            slowprint("Você está fora de si? Huh!")
            
except ZeroDivisionError:
    print("Divisão por 0 é infinita")
    
except KeyboardInterrupt:
    slowprint("\n [-] Saindo...")

time.sleep(0.4)
