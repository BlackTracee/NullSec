try:
    from googlesearch import search
except ImportError:
    print("Nenhum módulo chamado 'google' encontrado")
 
print('''
    ************************************************
    *   _  _ _   _ _     _  _  _ ___ ___ ___       *
    *  | \| | | | | |   | \| |/ _ \ __| __| |      *
    *  | .` | |_| | |__ | .` | (_) \__ \ _|| |__   *
    *  |_|\_|\___/|____||_|\_|\___/|___/___|____|  *
    *                                              *
    *                NullSec Tool                  *
    *             BY: BlakcTrace	               *
    *                                              *
    ************************************************
''')
try:
	# to search
	query = input("\033[92m [*] Pesquise aqui: ")
	for j in search(query, tld="co.in", num=10, stop=10, pause=2):
		print("")
		print(j)
except KeyboardInterrupt:
	print("\033[91m\n [-] Ctrl+C detectado")
input("\n[-] Enter To Exit")
