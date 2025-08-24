import csv
from faker import Faker
import datetime
import os

os.system("clear")
print('''
 ****************************************************
 *  _        _   _      ___     _         ___ _     *
 * | |   ___| |_( )___ | __|_ _| |_____  |_ _| |_   *
 * | |__/ -_)  _|/(_-< | _/ _` | / / -_)  | ||  _|  *
 * |____\___|\__| /__/ |_|\__,_|_\_\___| |___|\__|  *
 *                                                  *
 *        Ferramenta de Geração de Arquivos Falsos  *
 *       (suporta qualquer formato de arquivo)      *                           
 *       https://github.com/BlackTracee             *
 *                                                  *
 ****************************************************
''')

try:
    def datagenerate(records, headers):
        fake = Faker('pt_BR')   # Alterado para gerar dados brasileiros
        fake1 = Faker('en_GB')  # Mantido para gerar telefones no formato UK
        with open(input(" [+] DIGITE O NOME DO ARQUIVO PARA SALVAR A SAÍDA : "), 'wt') as csvFile:
            print("\n [+] Gerando dados falsos....\n [*] Aguarde...\n")
            writer = csv.DictWriter(csvFile, fieldnames=headers)
            writer.writeheader()
            for i in range(records):
                full_name = fake.name()
                FLname = full_name.split(" ")
                Fname = FLname[0]
                Lname = FLname[1] if len(FLname) > 1 else "Silva"  # Caso não tenha sobrenome
                domain_name = "@gmail.com"
                userId = Fname + "." + Lname + domain_name
            
                writer.writerow({
                        "Email": userId,
                        "Prefixo": fake.prefix(),
                        "Nome": fake.name(),
                        "Data de Nascimento": fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1, 1)),
                        "Telefone": fake1.phone_number(),
                        "Email Alternativo": fake.email(),
                        "Endereço": fake.address(),
                        "CEP": fake.postcode(),
                        "Cidade": fake.city(),
                        "Estado": fake.state(),
                        "País": fake.country(),
                        "Ano": fake.year(),
                        "Hora": fake.time(),
                        "Link": fake.url(),
                        "Texto": fake.word(),
                        })
    
    if __name__ == '__main__':
        records = 10000
        headers = ["Email", "Prefixo", "Nome", "Data de Nascimento", "Telefone", "Email Alternativo",
                   "Endereço", "CEP", "Cidade", "Estado", "País", "Ano", "Hora", "Link", "Texto"]
        datagenerate(records, headers)
        print("\n [*] A geração de dados falsos foi concluída! \n")
    else:
        print(" [!] Falha ao gerar dados! ")
except KeyboardInterrupt:
    print("\n [-] Ctrl + C Detectado.........Saindo\n")

input(" Pressione Enter para sair ")
os.system("clear")
