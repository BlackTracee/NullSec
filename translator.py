from translate import Translator
print('''
    Translator
 ========================================== 
      ''')
translator= Translator(from_lang=input(" [?] Do idioma que você deseja traduzir: "),to_lang=input(" [?] Para qual idioma você deseja traduzir: "))
translation = translator.translate(input(" 🔴🔴 Digite o texto : "))
print ("    Tradução é : " + translation)
input("Enter para sair...")
