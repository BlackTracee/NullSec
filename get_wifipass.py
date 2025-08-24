import subprocess
import os
import re
from collections import namedtuple
import configparser

print('''\033[93m
    ***************************************************************
    *    ___     _ __      ___  __ _ ___                          *
    *   / __|___| |\ \    / (_)/ _(_) _ \__ _ ______              *
    *  | (_ / -_)  _\ \/\/ /| |  _| |  _/ _` (_-<_-<              *
    *   \___\___|\__|\_/\_/ |_|_| |_|_| \__,_/__/__/              *
    *                                                             *
    *   Ferramenta poderosa para obter todas as senhas de Wi-Fi   *
    *   Código de BlackTrace                                      *
    *   GiHub: https://github.com/BlackTracee/NullSec             *
    *                                                             *
    ***************************************************************
''')
                                              
def obter_ssids_salvos_windows():
    """Retorna uma lista de SSIDs salvos em um computador Windows usando o comando netsh"""
    output = subprocess.check_output("netsh wlan show profiles").decode()
    ssids = []
    profiles = re.findall(r"All User Profile\s(.*)", output)
    for profile in profiles:
        ssid = profile.strip().strip(":").strip()
        ssids.append(ssid)
    return ssids


def obter_senhas_wifi_windows(verbose=1):
    """Extrai senhas de Wi-Fi salvas no Windows"""
    ssids = obter_ssids_salvos_windows()
    Profile = namedtuple("Profile", ["ssid", "ciphers", "key"])
    profiles = []
    for ssid in ssids:
        detalhes_ssid = subprocess.check_output(f"""netsh wlan show profile "{ssid}" key=clear""").decode()
        ciphers = re.findall(r"Cipher\s(.*)", detalhes_ssid)
        ciphers = "/".join([c.strip().strip(":").strip() for c in ciphers])
        key = re.findall(r"Key Content\s(.*)", detalhes_ssid)
        try:
            key = key[0].strip().strip(":").strip()
        except IndexError:
            key = "Nenhuma"
        profile = Profile(ssid=ssid, ciphers=ciphers, key=key)
        if verbose >= 1:
            imprimir_perfil_windows(profile)
        profiles.append(profile)
    return profiles


def imprimir_perfil_windows(profile):
    """Exibe um perfil de Wi-Fi do Windows"""
    print(f"{profile.ssid:25}{profile.ciphers:15}{profile.key:50}")


def imprimir_perfis_windows(verbose):
    """Exibe todos os SSIDs extraídos com suas senhas no Windows"""
    print("\033[94m SSID                     CRIPTOGRAFIAS      SENHA")
    obter_senhas_wifi_windows(verbose)


def obter_senhas_wifi_linux(verbose=1):   
    """Extrai senhas de Wi-Fi salvas no Linux usando o diretório /etc/NetworkManager/system-connections/"""
    caminho_conexoes = "/etc/NetworkManager/system-connections/"
    campos = ["ssid", "auth-alg", "key-mgmt", "psk"]
    Profile = namedtuple("Profile", [f.replace("-", "_") for f in campos])
    profiles = []
    for arquivo in os.listdir(caminho_conexoes):
        dados = { k.replace("-", "_"): None for k in campos }
        config = configparser.ConfigParser()
        config.read(os.path.join(caminho_conexoes, arquivo))
        for _, section in config.items():
            for k, v in section.items():
                if k in campos:
                    dados[k.replace("-", "_")] = v
        profile = Profile(**dados)
        if verbose >= 1:
            imprimir_perfil_linux(profile)
        profiles.append(profile)
    return profiles


def imprimir_perfil_linux(profile):
    """Exibe um perfil de Wi-Fi do Linux"""
    print(f"{str(profile.ssid):25}{str(profile.auth_alg):5}{str(profile.key_mgmt):10}{str(profile.psk):50}") 


def imprimir_perfis_linux(verbose):
    """Exibe todos os SSIDs extraídos com suas senhas (PSK) no Linux"""
    print("SSID                     AUTENTICAÇÃO  GERENCIAMENTO-CHAVE  PSK")
    obter_senhas_wifi_linux(verbose)
    
    
def imprimir_todos_perfis(verbose=1):
    if os.name == "nt":
        imprimir_perfis_windows(verbose)
    elif os.name == "posix":
        imprimir_perfis_linux(verbose)
    else:
        raise NotImplemented("O código funciona apenas no Linux ou Windows")
    

print('''\033[91m
    ***************************************************************
    *                                                             *
    *   🔴 AVISO: ESTA FERRAMENTA SÓ COLETA SENHAS                *
    *           QUE FORAM INSERIDAS ANTERIORMENTE NO COMPUTADOR  *
    *           SE A SENHA FOR ALTERADA PELO PROPRIETÁRIO,       *
    *           ESTA FERRAMENTA NÃO PODE AJUDAR A INVADIR A SSID *
    *           OU MOSTRAR RESULTADOS DEPOIS DA MUDANÇA          *
    *                                                             *
    ***************************************************************
''')    

print('''\033[92m
       [*] Hulk começou a capturar SSID, criptografia e senha ...
       
       [!] Hulk encontrou os resultados ::: 
''')

if __name__ == "__main__":
    imprimir_todos_perfis()
input("Pressione Enter para continuar")
