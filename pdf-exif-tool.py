import pikepdf
import sys
import os

# Ler o arquivo PDF
os.system("clear")
print(''' 
  ___ ___  ___   _____  _____ ___   _____ ___   ___  _    
 | _ \   \| __| | __\ \/ /_ _| __| |_   _/ _ \ / _ \| |  v. 1. O 
 |  _/ |) | _|  | _| >  < | || _|    | || (_) | (_) | |__ 
 |_| |___/|_|   |___/_/\_\___|_|     |_| \___/ \___/|____|
          c 0 d e   f       0         
                        r        m    BlackTrace     
                        
           https://github.com/BlackTracee                  
''')  
print("")

try:                                                     
    pdf = pikepdf.Pdf.open(input(" [*] Digite o nome do PDF: "))
    print("")    
    docinfo = pdf.docinfo
    for key, value in docinfo.items():
        print(key, ":", value)
        print("")
except KeyboardInterrupt:
    print("\n [-] Ctrl+C detectado----\n [-] Saindo....\n")
