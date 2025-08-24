'''imports'''
import requests
import time

print('''\033[93m
  ___          _      _   __  __        _ _              
 / __| ___  __(_)__ _| | |  \/  |___ __| (_)__ _         
 \__ \/ _ \/ _| / _` | | | |\/| / -_) _` | / _` |        
 |___/\___/\__|_\__,_|_| |_|  |_\___\__,_|_\__,_|        
   /_\  __ __ ___ _  _ _ _| |_  | __(_)_ _  __| |___ _ _ 
  / _ \/ _/ _/ _ \ || | ' \  _| | _|| | ' \/ _` / -_) '_|
 /_/ \_\__\__\___/\_,_|_||_\__| |_| |_|_||_\__,_\___|_|  
                                                         
                                                        ''')
''' INSIRA USERNMAE PARA ENCONTRAR CONTAS '''
try:
	usuario = input('\033[92m{+} Digite o nome de usuário para encontrar contas: ')


	# INSTAGRAM
	instagram = f'https://www.instagram.com/{usuario}'

	# FACEBOOK
	facebook = f'https://www.facebook.com/{usuario}'

	#TWITTER
	twitter = f'https://www.twitter.com/{usuario}'

	# YOUTUBE
	youtube = f'https://www.youtube.com/{usuario}'

	# BLOGGER
	blogger = f'https://{usuario}.blogspot.com'

	# GOOGLE+
	google_plus = f'https://plus.google.com/s/{usuario}/top'

	# REDDIT
	reddit = f'https://www.reddit.com/user/{usuario}'

	# WORDPRESS
	wordpress = f'https://{usuario}.wordpress.com'

	# PINTEREST
	pinterest = f'https://www.pinterest.com/{usuario}'

	# GITHUB
	github = f'https://www.github.com/{usuario}'

	# TUMBLR
	tumblr = f'https://{usuario}.tumblr.com'

	# FLICKR
	flickr = f'https://www.flickr.com/people/{usuario}'

	# STEAM
	steam = f'https://steamcommunity.com/id/{usuario}'

	# VIMEO
	vimeo = f'https://vimeo.com/{usuario}'

	# SOUNDCLOUD
	soundcloud = f'https://soundcloud.com/{usuario}'

	# DISQUS
	disqus = f'https://disqus.com/by/{usuario}'

	# MEDIUM
	medium = f'https://medium.com/@{usuario}'

	# DEVIANTART
	deviantart = f'https://{usuario}.deviantart.com'

	# VK
	vk = f'https://vk.com/{usuario}'

	# ABOUT.ME
	aboutme = f'https://about.me/{usuario}'

	# IMGUR
	imgur = f'https://imgur.com/user/{usuario}'

	# FLIPBOARD
	flipboard = f'https://flipboard.com/@{usuario}'

	# SLIDESHARE
	slideshare = f'https://slideshare.net/{usuario}'

	# FOTOLOG
	fotolog = f'https://fotolog.com/{usuario}'

	# SPOTIFY
	spotify = f'https://open.spotify.com/user/{usuario}'

	# MIXCLOUD
	mixcloud = f'https://www.mixcloud.com/{usuario}'

	# SCRIBD
	scribd = f'https://www.scribd.com/{usuario}'

	# BADOO
	badoo = f'https://www.badoo.com/en/{usuario}'

	# PATREON
	patreon = f'https://www.patreon.com/{usuario}'

	# BITBUCKET
	bitbucket = f'https://bitbucket.org/{usuario}'

	# DAILYMOTION
	dailymotion = f'https://www.dailymotion.com/{usuario}'

	# ETSY
	etsy = f'https://www.etsy.com/shop/{usuario}'

	# CASHME
	cashme = f'https://cash.me/{usuario}'

	# BEHANCE
	behance = f'https://www.behance.net/{usuario}'

	# GOODREADS
	goodreads = f'https://www.goodreads.com/{usuario}'

	# INSTRUCTABLES
	instructables = f'https://www.instructables.com/member/{usuario}'

	# KEYBASE
	keybase = f'https://keybase.io/{usuario}'

	# KONGREGATE
	kongregate = f'https://kongregate.com/accounts/{usuario}'

	# LIVEJOURNAL
	livejournal = f'https://{usuario}.livejournal.com'

	# ANGELLIST
	angellist = f'https://angel.co/{usuario}'

	# LAST.FM
	last_fm = f'https://last.fm/user/{usuario}'

	# DRIBBBLE
	dribbble = f'https://dribbble.com/{usuario}'

	# CODECADEMY
	codecademy = f'https://www.codecademy.com/{usuario}'

	# GRAVATAR
	gravatar = f'https://en.gravatar.com/{usuario}'

	# PASTEBIN
	pastebin = f'https://pastebin.com/u/{usuario}'

	# FOURSQUARE
	foursquare = f'https://foursquare.com/{usuario}'

	# ROBLOX
	roblox = f'https://www.roblox.com/user.aspx?username={usuario}'

	# GUMROAD
	gumroad = f'https://www.gumroad.com/{usuario}'

	# NEWSGROUND
	newsground = f'https://{usuario}.newgrounds.com'

	# WATTPAD
	wattpad = f'https://www.wattpad.com/user/{usuario}'

	# CANVA
	canva = f'https://www.canva.com/{usuario}'

	# CREATIVEMARKET
	creative_market = f'https://creativemarket.com/{usuario}'

	# TRAKT
	trakt = f'https://www.trakt.tv/users/{usuario}'

	# 500PX
	five_hundred_px = f'https://500px.com/{usuario}'

	# BUZZFEED
	buzzfeed = f'https://buzzfeed.com/{usuario}'

	# TRIPADVISOR
	tripadvisor = f'https://tripadvisor.com/members/{usuario}'

	# HUBPAGES
	hubpages = f'https://{usuario}.hubpages.com'

	# CONTENTLY
	contently = f'https://{usuario}.contently.com'

	# HOUZZ
	houzz = f'https://houzz.com/user/{usuario}'

	#BLIP.FM
	blipfm = f'https://blip.fm/{usuario}'

	# WIKIPEDIA
	wikipedia = f'https://www.wikipedia.org/wiki/User:{usuario}'

	# HACKERNEWS
	hackernews = f'https://news.ycombinator.com/user?id={usuario}'

	# CODEMENTOR
	codementor = f'https://www.codementor.io/{usuario}'

	# REVERBNATION
	reverb_nation = f'https://www.reverbnation.com/{usuario}'

	# DESIGNSPIRATION
	designspiration = f'https://www.designspiration.net/{usuario}'

	# BANDCAMP
	bandcamp = f'https://www.bandcamp.com/{usuario}'

	# COLOURLOVERS
	colourlovers = f'https://www.colourlovers.com/love/{usuario}'

	# IFTTT
	ifttt = f'https://www.ifttt.com/p/{usuario}'

	# EBAY
	ebay = f'https://www.ebay.com/usr/{usuario}'

	# SLACK
	slack = f'https://{usuario}.slack.com'

	# OKCUPID
	okcupid = f'https://www.okcupid.com/profile/{usuario}'

	# TRIP
	trip = f'https://www.trip.skyscanner.com/user/{usuario}'

	# ELLO
	ello = f'https://ello.co/{usuario}'

	# TRACKY
	tracky = f'https://tracky.com/user/~{usuario}'
 
	#TIKTOK
	tiktok = f'https://tiktok.com/@{usuario}'

	# BASECAMP
	basecamp = f'https://{usuario}.basecamphq.com/login'


	''' LISTA DE SITES - USE PARA PESQUISA DE NOME DE USUÁRIO '''
	WEBSITES = [
	instagram, facebook, twitter, youtube, blogger, google_plus, reddit,
	wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus, 
	medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
	mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
	goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
	dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground,
	wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages,
	contently, houzz, blipfm, wikipedia, hackernews, reverb_nation, designspiration,
	bandcamp, colourlovers, ifttt, ebay, slack, okcupid, trip, ello, tracky, tiktok, basecamp,
	]


	''' FUNÇÃO DE IMPRESSÃO COLORIDA '''
	def outer_func(colour):
		def inner_function(msg):
			print(f'{colour}{msg}')
		return inner_function


	''' IMPRESSÕES COLORIDAS '''
	GREEN = outer_func('\033[92m')
	YELLOW = outer_func('\033[93m')
	RED = outer_func('\033[91m')


	''' BANNER '''
	def banner():
		('''
	  ___          _      _   __  __        _ _              
	 / __| ___  __(_)__ _| | |  \/  |___ __| (_)__ _         
	 \__ \/ _ \/ _| / _` | | | |\/| / -_) _` | / _` |        
	 |___/\___/\__|_\__,_|_| |_|  |_\___\__,_|_\__,_|        
	   /_\  __ __ ___ _  _ _ _| |_  | __(_)_ _  __| |___ _ _ 
	  / _ \/ _/ _/ _ \ || | ' \  _| | _|| | ' \/ _` / -_) '_|
	 /_/ \_\__\__\___/\_,_|_||_\__| |_| |_|_||_\__,_\___|_|  
															 
	  ''')


	def search():
		GREEN(f'[+] Searching for username:{usuario}')
		time.sleep(0.5)
		print('.......')
		time.sleep(0.5)
		print('.......\n')
		time.sleep(0.5)

		count = 0
		match = True
		for url in WEBSITES:
			r = requests.get(url)

			if r.status_code == 200:
				if match == True:
					GREEN('[+] FOUND MATCHES')
					match = False
				YELLOW(f'\n{url} - {r.status_code} - OK')
				if usuario in r.text:
					GREEN(f'CORRESPONDÊNCIA POSITIVA: Nome de usuário:{usuario} - o texto foi detectado na URL.')
				else:
					GREEN(f'POSITIVE MATCH: Username:{usuario} - \033[91mtext has NOT been detected in url, could be a FALSE POSITIVE.')#
			count += 1

		total = len(WEBSITES)
		GREEN(f'CONCLUÍDO: Um total de {count} PARTIDAS descobertas fora de {total} sites.')



	if __name__=='__main__':
		banner()
		search()
except KeyboardInterrupt:
	print("\n\033[91m[-] Exiting...")
input("[*] Press Enter To Exit")
