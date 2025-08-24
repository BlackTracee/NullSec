import socket,sys,time

logo = '''\033[92m
	  ___                            ___          _    _             
	 | _ ) __ _ _ _  _ _  ___ _ _   / __|_ _ __ _| |__| |__  ___ _ _ 
	 | _ \/ _` | ' \| ' \/ -_) '_| | (_ | '_/ _` | '_ \ '_ \/ -_) '_|
	 |___/\__,_|_||_|_||_\___|_|    \___|_| \__,_|_.__/_.__/\___|_|  
																	
                    coded by Sumalya Chatterjee
'''
print(logo)
try:
	def slowprint(s):
		for c in s + '\n' :
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(10. / 100)
	def ban_grab(host, port, delay) :
		'''
		Esta função pega três parâmetros de main() para processar e obter o banner da porta solicitada
		Possui uma condição específica para porta HTTP que torna este programa mais flexível do que outros simples
		agarradores de faixas

		:param host:        : Pergunte a NullSec um endereço IP ou URL
		:param port:         Porta solicitada pela NullSec
		:param delay:      ATRASO DE TEMPO PARA PESQUISA
		:return:                 None
		'''
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           
		try :
			s.settimeout(delay)
			if port == 80 :                                           
				s.connect((str(host), port))
				GET = 'GET / HTTP/1.1\nHost: '+ str(host) +'\n\n'       
				s.sendall(str.encode(GET))
				banner = s.recvfrom(512)                                

			else :
				s.connect((str(host), port))                           
				banner = s.recvfrom(512)

			banner = banner[0]
			banner = banner.splitlines()                           
			for line in banner:
				line = str(line)
				line = line.replace('\'','')                           
				print(line[1::])

		except Exception as er :
			slowprint('\033[91m Error : ' + str(er))                              

		finally :
			s.close()                                               

	def user_input(msg) :                                               
		while True :
			try :
				return input(msg)
			except KeyboardInterrupt :
				slowprint('\033[91m [-] NullSec não permite que você saia agora!')

	def main() :
		host = user_input('\033[92m [+] Pergunte a NullSec um IP ou URL : ')                      
		port = int(user_input('\033[92m [+] Pergunte  a NullSec uma porta : '))
		if port < 1 or port > 65535 :
			slowprint('\033[91m [+] Entrada inválida para porta\nDefault set 80')
			port = 80
		delay = int(user_input('\033[92m [+] Insira o atraso : '))
		if delay < 0 or delay > 100 :
			slowprint('\033[91m [-] Entrada inválida para atraso\nDefault set 5')
			delay = 5
		print('='*30 + 'Banner' +'='*30)
		ban_grab(host, port, delay)                                  
	if __name__ == '__main__' :
		main()
except KeyboardInterrupt:
	slowprint(' [-] Saindo....')
