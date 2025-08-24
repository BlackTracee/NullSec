
import nmap
# We import the ipaddress module. We want to use the ipaddress.ip_address(address)
# method to see if we can instantiate a valid ip address to test.
import ipaddress
# We need to create regular expressions to ensure that the input is correctly formatted.
import re


port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

port_min = 0
port_max = 65535



while True:
    ip_add_entered = input("\n\033[92m [*] Insira o endereço IP que deseja escanear: ")
    try:
        ip_address_obj = ipaddress.ip_address(ip_add_entered)
        print("\033[92m [+] Você inseriu um endereço IP válido.")
        break
    except:
        print("\033[91m [-] Você inseriu um endereço IP inválido")


while True:
    print("\033[92m [*] Insira o intervalo de portas que deseja escanear no formato: <int>-<int> (ex seria 60-120)")
    port_range = input("\033[92m [*] Insira o intervalo de portas: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

nm = nmap.PortScanner()
for port in range(port_min, port_max + 1):
    try:
        result = nm.scan(ip_add_entered, str(port))
        port_status = (result['escanear'][ip_add_entered]['tcp'][port]['estado'])
        print(f"Porta {port} é {port_status}")
    except:
       
        print(f"Não é possível escanear a porta {port}.")
