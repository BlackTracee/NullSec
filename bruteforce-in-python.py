import random
import pyautogui
import os
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLOPMNQRSTUVWXYZ@#$*!-_=+&%0123456789"

allchar=list(chars)

pwd = pyautogui.password(" Digite uma senha: ")
sample_pwd = " "
try:
	while(sample_pwd != pwd):
		sample_pwd = random.choices(allchar, k=len(pwd))
	
		print("<==========================="+ str(sample_pwd)+ "==================================>")
	
		if (sample_pwd == list(pwd)):
			print(" [+] Sua senha É: "+ "".join(sample_pwd))
			break
except KeyboardInterrupt:
	print("\n [-] Ctrl+C detectado.....Saindo")
input(" [+] Enter para sair...")
