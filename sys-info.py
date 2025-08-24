import psutil
import platform
from datetime import datetime

print("""
    ********************************************
    *     ___            ___       __          *
    *    / __|_  _ _____|_ _|_ _  / _|___      *
    *    \__ \ || (_-<___| || ' \|  _/ _ \     *
    *    |___/\_, /__/  |___|_||_|_| \___/     *
    *         |__/                             *
    *                                          *
    * reúna informações do sistema rapidamente * 
    *        Feito por BlackTrace              *
    ********************************************
    """)

def get_size(bytes, sufixo="B"):
    """
    Escala bytes para o formato adequado
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    fator = 1024
    for unidade in ["", "K", "M", "G", "T", "P"]:
        if bytes < fator:
            return f"{bytes:.2f}{unidade}{sufixo}"
        bytes /= fator


print("="*40, "Informações do sistema", "="*40)
uname = platform.uname()
print(f"Sistema: {uname.system}")
print(f"Nome do nó: {uname.node}")
print(f"Lançamento: {uname.release}")
print(f"Versão: {uname.version}")
print(f"Máquina: {uname.machine}")
print(f"Processador: {uname.processor}")

# Hora de inicialização
print("="*40, "Hora de inicialização", "="*40)
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
print(f"Hora de inicialização: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

# Informações da CPU
print("="*40, "Informações CPU", "="*40)
# número de núcleos
print("Núcleos físicos:", psutil.cpu_count(logical=False))
print("Núcleos totais:", psutil.cpu_count(logical=True))
# Frequências da CPU
cpufreq = psutil.cpu_freq()
print(f"Frequência máxima: {cpufreq.max:.2f}Mhz")
print(f"Frequência mínima: {cpufreq.min:.2f}Mhz")
print(f"Frequência atual: {cpufreq.current:.2f}Mhz")
# Uso da CPU
print("Uso da CPU por núcleo:")
for i, porcentagem in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Núcleo {i}: {porcentagem}%")
print(f"Uso total da CPU: {psutil.cpu_percent()}%")

# Informações de memória
print("="*40, "Informações de Memória", "="*40)
# detalhes da memória
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}")
print(f"Disponível: {get_size(svmem.available)}")
print(f"Usada: {get_size(svmem.used)}")
print(f"Percentual: {svmem.percent}%")
print("="*20, "SWAP", "="*20)
# detalhes da memória swap (se existir)
swap = psutil.swap_memory()
print(f"Total: {get_size(swap.total)}")
print(f"Livre: {get_size(swap.free)}")
print(f"Usada: {get_size(swap.used)}")
print(f"Percentual: {swap.percent}%")

# Informações de disco
print("="*40, "Informações de Disco", "="*40)
print("Partições e Uso:")
# todas as partições de disco
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"=== Dispositivo: {partition.device} ===")
    print(f"  Ponto de montagem: {partition.mountpoint}")
    print(f"  Tipo de sistema de arquivos: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
    print(f"  Tamanho total: {get_size(partition_usage.total)}")
    print(f"  Usado: {get_size(partition_usage.used)}")
    print(f"  Livre: {get_size(partition_usage.free)}")
    print(f"  Percentual: {partition_usage.percent}%")
# estatísticas de IO desde a inicialização
disk_io = psutil.disk_io_counters()
print(f"Total lido: {get_size(disk_io.read_bytes)}")
print(f"Total escrito: {get_size(disk_io.write_bytes)}")

# Informações de rede
print("="*40, "Informações de Rede", "="*40)
# todas as interfaces de rede (virtuais e físicas)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"  Endereço IP: {address.address}")
            print(f"  Máscara de rede: {address.netmask}")
            print(f"  IP de Broadcast: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"  Endereço MAC: {address.address}")
            print(f"  Máscara: {address.netmask}")
            print(f"  MAC de Broadcast: {address.broadcast}")
net_io = psutil.net_io_counters()
print(f"Total de Bytes Enviados: {get_size(net_io.bytes_sent)}")
print(f"Total de Bytes Recebidos: {get_size(net_io.bytes_recv)}")


# Informações de GPU
import GPUtil
from tabulate import tabulate
print("="*40, "Detalhes da GPU", "="*40)
gpus = GPUtil.getGPUs()
list_gpus = []
for gpu in gpus:
    gpu_id = gpu.id
    gpu_name = gpu.name
    gpu_load = f"{gpu.load*100}%"
    gpu_free_memory = f"{gpu.memoryFree}MB"
    gpu_used_memory = f"{gpu.memoriausada}MB"
    gpu_total_memory = f"{gpu.totalMemoria}MB"
    gpu_temperature = f"{gpu.temperatura} °C"
    gpu_uuid = gpu.uuid
    list_gpus.append((
        gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
        gpu_total_memory, gpu_temperature, gpu_uuid
    ))

print(tabulate(list_gpus, headers=("id", "nome", "uso", "memória livre", "memória usada", "memória total",
                                   "temperatura", "uuid")))
input("Enter para sair...")
