import sys,os,time, webbrowser
import pyfiglet
os.system("clear")
print("""
███╗   ██╗██╗   ██╗██╗     ██╗     ███████╗███████╗ ██████╗
████╗  ██║██║   ██║██║     ██║     ██╔════╝██╔════╝██╔═══
██╔██╗ ██║██║   ██║██║     ██║     █████╗  ███████╗██║   
██║╚██╗██║██║   ██║██║     ██║     ██╔══╝  ╚════██║██║  
██║ ╚████║╚██████╔╝███████╗███████╗███████╗███████║╚██████╔
╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝ ╚═════╝ 
""")
try:
	def slowprint(s):
		for c in s + '\n' :
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(10 / 100)
	slowprint('\033[91m [*] FODASSE A SOCIEDADE')
	print("---------------------------------------------------")
	input("\n\033[97m [*] Digite para b00T")
	os.system("clear")
	def slowprint(s):
		for c in s + '\n' :
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(10 / 1000)
	slowprint("[*] Inicializando..... ")
	time.sleep(0.3)
	slowprint("\033[91m[*] Não use mal seu poder")
	slowprint("\033[97m[*] Os humanos são os mais vulneráveis")
	time.sleep(0.3)
	slowprint("\033[91m[*] Melhore, não prove")
	time.sleep(0.3)
	slowprint("\033[92m[*] A superpotência precisa ser praticada")
	print("\033[98m[*] Segurança é apenas uma ilusão")
	time.sleep(0.3)
	slowprint("\033[91m[*] Com um grande poder vem uma grande responsabilidade")
	slowprint("\033[92m[*] Não seja uma exceção, seja um exemplo")
	time.sleep(0.4)
	slowprint("\033[93m[*] Aceite o passado, siga em frente")
	slowprint("\033[95m[*] Pessoas boas são sempre mal utilizadas")
	time.sleep(0.3)
	print("\033[97m[*] Governo. Controla nossa mídia... As mídias sociais são falsas")
	slowprint("\033[91m[*] Errar com o orgulho é a pior decisão de todos os tempos")
	time.sleep(0.3)
	slowprint("\033[92m[*] Seja um exemplo diante de um consultor")
	time.sleep(0.3)
	slowprint("\033[91m[*] O tempo não cura nada, apenas nos habitua à situação")
	slowprint("\033[93m[*] Um monstro é melhor que um deus arrogante")
	time.sleep(1)
	slowprint("\033[97m[*] Inicialização concluída :)")
	time.sleep(2)
	os.system("clear")
	def slowprint(s):
		for c in s + '\n' :
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(10 / 100)
	slowprint("\033[92m[*] Ferramenta de partida....")
	time.sleep(0.3)
	os.system("clear")

	running = True
	while running:
		print(pyfiglet.figlet_format('NullSec'))
		print("	\033[97m=========================================================== ")
		slowprint("\t\t\033[91mA privacidade é um mito, assim como a democracia ")
		slowprint("\t\t\tDate: " + time.strftime("%d/%m/%y"))
		print("	\033[97m=========================================================== ")
		print('''\033[92m
		[1] Verificar anonimato
		[2] Localizador de painel de administração
		[3] ARP-Spoofing
		[4] Banner Grabbing
		[5] Ataque DDoS
		[6] E-mail falso
		[7] Criar credenciais falsas
		[8] Hack do Gmail
		[9] Escaneamento de IP
		[10] Quebrador de senhas Linux
		[11] Gerador de senhas
		[12] Scanner de portas Nmap
		[13] DDoS em Wi-Fi
		[14] Ferramenta PDF Exif
		[15] Esteganografia
		[16] Obter senha do Wi-Fi
		[17] Teste de velocidade da internet
		[18] Monitoramento de rede
		[19] Sugira um filme
		[20] Emulador Python
		[21] Calculadora
		[22] Verificação ARP
		[23] SMS Spoofing
		[24] Ataque de Phishing
		[25] Bombardeio de SMS
		[26] Coletar informações de número de telefone
		[27] Localizador de XSS
		[28] Localizador de SQLI
		[29] Shodan
		[30] Informações do sistema
		[31] Netdiscover
		[32] Mudador de MAC
		[33] Criptografia-Descriptografia [GUI]
		[34] Criptografar sua mensagem [CLI]
		[35] Descriptografar sua mensagem [CLI]
		[36] Tradutor
		[37] Emulador de terminal
		[38] OSINT
		[39] Navegador NullSec [GUI]
		[40] Bombardeio de e-mail
		[41] Automação de visualizações em redes sociais
		[42] Motor de busca NullSec
		[43] Google Dorking
		[44] Hack de câmeras de segurança
		[45] Golang para hackers éticos
		[46] Perl para hackers éticos
		[47] Ruby para hackers éticos
		[48] Python para hacking ético
		[49] Bash para hackers éticos
		[50] Sobre esta ferramenta
		[51] Atualizar NullSec
		[00] Sair da ferramenta
		[??] Ajuda
		''')

		select = input("\033[95m [?] Escolha qualquer opção: ")
  
		if select == '1':
			os.system("clear")
			os.system("python amianonymous.py")
			os.system("clear")
		elif select == '2':
			os.system("python admin-panel-finder.py")
			os.system("clear")
		elif select == '3':
			os.system("clear")
			os.system("sudo python arp-spoofing.py")
			os.system("clear")
		elif select == '4':
			os.system("clear")
			os.system("python banner-grabbing.py")
			os.system("clear")
		elif select == '5':
			os.system("python NullSec.py")
			os.system("clear")
		elif select == '6':
			os.system("clear")
			os.system("python fakemail.py")
			os.system("clear")
		elif select == '7':
			os.system("pythonfake-data-generator.py")
			os.system("clear")
		elif select == '8':
			os.system("python hack-gmail.py")
			os.system("clear")
		elif select == '9':
			os.system("python ip-scanner.py")
			os.system("clear")
		elif select == '10':
			os.system("python linux_pass_cracker.py")
			os.system("clear")
		elif select == '11':
			os.system("python pass-gen.py")
			os.system("clear")
		elif select == '12':
			os.system("clear")
			os.system("python nmap_port_scanner.py")
			os.system("clear")
		elif select == '13':
			os.system("python wifi_dos_final.py")
			os.system("clear")
		elif select == '14':
			os.system("python pdf-exif-tool.py")
			os.system("clear")
		elif select == '15':
			os.system("python steganography.py")
			os.system("clear")
		elif select == '16':
			os.system("python get_wifipass.py")
			os.system("clear")
		elif select == '17':
			os.system("python internet-speed-test.py")
			os.system("clear")
		elif select == '18':
			os.system("python network-monitoring.py")
			os.system("clear")
		elif select == '19':
			os.system("clear")
			os.system("python movie-suggesting.py")
			os.system("clear")
		elif select == '20':
			os.system("python terminal-emulator.py")
			os.system("clear")
		elif select == '21':
			os.system("clear")
			os.system("python calculator.py")
		elif select == '22':
			os.system("clear")
			os.system("python arp-verification.py")
			os.system("clear")
		elif select == '23':
			os.system("clear")
			os.system("python fakesms.py")
			os.system("clear")
		elif select == '24':
			os.system("clear")
			os.system("python pyphisher.py")
			time.sleep(100)
			os.system("clear")
		elif select == '25':
			os.system("clear")
			os.system("python bomber.py")
			time.sleep(2)
			os.system("clear")
		elif select == '26':
			os.system("clear")
			os.system("python phone-number-info.py")
			os.system("clear")
		elif select == '27':
			os.system("clear")
			os.system("python xss-vulnerability-finder.py")
			os.system("clear")
		elif select == '28':
			os.system("clear")
			os.system("python sqli-scanner.py")
			os.system("clear")
		elif select == '29':
			os.system("clear")
			os.system("python shodan-api.py")
			os.system("clear")
		elif select == '30':
			os.system("clear")
			os.system("python sys-info.py")
			os.system("clear")
		elif select == '31':
			os.system("clear")
			os.system("netdiscover")
			time.sleep(10)
			input("\033[91m[-] Pressione Enter para sair")
			os.system("clear")
		elif select == '32':
			os.system("clear")
			os.system("python mac-changer.py")
			os.system("clear")
		elif select == '33':
			os.system("clear")
			os.system("python encrypt.py")
			os.system("clear")
		elif select == '34':
			os.system("clear")
			os.system("python encrypt-cli.py")
			os.system("clear")
		elif select == '35':
			os.system("clear")
			os.system("python decrypt-cli.py")
			os.system("clear")
		elif select == '36':
			os.system("clear")
			os.system("python translator.py")
			os.system("clear")
		elif select == '37':
			os.system("clear")
			os.system("python terminal-emulator.py")
			os.system("clear")
		elif select == '38':
			os.system("clear")
			os.system("python osint.py")
			os.system("clear")
		elif select == '39':
			os.system("clear")
			os.system("python NullSec-browser.py")
			os.system("clear")  
		elif select == '40':
			os.system("clear")
			os.system("python email-bomber.py")
			os.system("clear")
		elif select == '41':
			os.system("clear")
			os.system("python automate-social_media-video-views.py")
			os.system("clear")
		elif select == '42':
			os.system("clear")
			os.system("python NullSec-engine.py")
			os.system("clear")
		elif select == '43':
			os.system("clear")
			os.system("python google-dorking.py")
			os.system("clear")
		elif select == '44':
			os.system("clear")
			os.system("python cam-hackers.py")
			os.system("clear")
		elif select == '48':
			os.system("clear")
			url = 'https://github.com/R3DHULK/golang-for-ethical-hackers'   
			webbrowser.open_new_tab(url) 
			os.system("clear")
		elif select == '49':
			os.system("clear")
			url = 'https://github.com/R3DHULK/perl-for-ethical-hackers'   
			webbrowser.open_new_tab(url) 
			os.system("clear")	
		elif select == '50':
			os.system("clear")
			url = 'https://github.com/R3DHULK/ruby-for-ethical-hackers'   
			webbrowser.open_new_tab(url)
			os.system("clear")
		elif select == '51':
			os.system("clear")
			os.system("python python-for-ethical-hacking.py")
			os.system("clear")
		elif select == '52':
			os.system("clear")
			os.system("python bash-for-ethical-hacking.py")
			os.system("clear")
		elif select == '53':
			os.system("clear")
			os.system("python about-tool.py")
			os.system("clear")
		elif select == '54':
			os.system("clear")
			os.system("python update-nullsec.py")
			os.system("clear")
		elif select == '00':
			os.system("clear")
			print("Saindo da ferramenta...")
			time.sleep(1)
			sys.exit()
		else:
			os.system("clear")

except KeyboardInterrupt:
	slowprint("\n\033[91m [-] Saindo.....")
	time.sleep(1)
	os.system("clear")
	slowprint("\033[97m [*] Obrigado, visite novamente...")
	time.sleep(1)
	sys.exit()
