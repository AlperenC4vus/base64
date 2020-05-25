#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, base64, time
#from csc.txtl import *
###############################################
# ------------------------------------------- #
#                KOD ALPEREN ÇAVUŞ            #
#                BASİT KODLAR İLE             #
#                BASE64 ŞİFRELEYİCİ           #
#                    VE ÇÖZÜCÜ                #
#   Github > https://github.com/TheAlperencv/ #
# ------------------------------------------- #
###############################################









name = input("\033[1;33m İsmini girermisisin > ")

abc = name.encode()
nerepla = base64.b64encode(abc)

print(f"{name} >>>>>>> {nerepla}")


def logo():

    time.sleep(2)
    asac = """\033[1;32m
    \t\t\t\t\t\t###############################################
    \t\t\t\t\t\t# ------------------------------------------- #
    \t\t\t\t\t\t#                KOD ALPEREN ÇAVUŞ            #          
    \t\t\t\t\t\t#                BASE64 ŞİFRELEYİCİ           #
    \t\t\t\t\t\t#                VE   DEŞİFRELEYİCİ           #
    \t\t\t\t\t\t#   Github > https://github.com/TheAlperencv/ #
    \t\t\t\t\t\t#   İnstagram :> @viper.py                    #
    \t\t\t\t\t\t# ------------------------------------------- #
    \t\t\t\t\t\t###############################################"""
a = 1
yol = os.getcwd()

cavus = os.name
if  cavus == "nt":
    p = str("\\")
else:
    p = str("/")
yesil = "\033[1;32m"
print("\n")

logo()
    
print("yardim ya da help yazarak menüyü görebilirsin")
while (a == 1):
    alperen = input(f"{yol} > ")

    if alperen == "help" or alperen == "yardim":
        print("""
[ + ]ŞİFRELE[ + ]
[ + ]  ÇÖZ  [ + ]
[ + ] ÇIKIŞ [ + ]       
        """)
    elif alperen == "1" or alperen == "01":

        try:
            apeli = input("\033[1;32mDosya gir > ")
            
            #time.sleep(2)
            isim = input("\033[1;32mDosyanın çıkış ismini gir ör:alperen.txt > ")

            with open(apeli) as f: #apeli'yi "f" olarak aç
                klm = f.read().encode("utf-8") #f'yi oku ve encode et

                als = str(base64.b64encode(klm)) #Dosyaya yazılabilmesi için string'e dönüştür

                dos = open(f"{isim}", "w") #Şifrelenmiş dosyayı yeni bir dosyaya yaz
                dos.write(als) # als'yi dos'a yaz

                f.close() # f'yi kapat

                dos.close() # dos'u kapat
                print("\033[1;33m[ + ]Dosya şuraya kaydedildi > {}\033[1;32m" .format(isim))
        except BaseException as sss: #Eğer dosya yok ya da base hatası olursa hatayı yakala
            print("Hata > ", sss)
    elif alperen == "2" or alperen == "02": #İŞlem 2
        try:
            apeli = input("\033[1;32mDosya gir > ") #Deşifrelenecek dosyayı seç
            
            isim = input("\033[1;32mDosyanın çıkış ismini gir ör:alperen.txt > ") #Deşifrelenmiş dosyayı yeni bir dosyaya yaz

            with open(apeli) as f: #Apeli'yi f olarak aç ve read kipinde devam et
                klm = f.read()

                ada = klm[1:] #1.Karakteri boşsay diğerlerini al

                aca = base64.b64decode(ada).decode() #Daha anlaşılabilir olması için aca'yi decode et

                dos = open(f"{isim}", "w") #Yeni dosyayı .M.K.A uzantılı olarak kayıt et
                dos.write(aca) #ve dos'u yaz

                f.close()

                dos.close()
            print("\033[1;33m[ + ]Dosya şu isimde kaydedildi > {}\033[1;32m" .format(isim))
        except BaseException as sss:
            print("Hata > ", sss)
    elif alperen == "3" or alperen == "03":
        print("\033[1;0m çıkılıyor...")
        break
    elif alperen.startswith("cd"):
        veri = alperen[3:].strip()

        try:
            os.chdir(veri)
        except OSError:
            print("İlgili klasöre giriş yapılamadı")
    elif alperen == "ls":
        for i in os.listdir():

            print(i, sep="\n")

    
    else:
        print(" \033[1;31m[ \033[1;33m\"{}\" \033[1;31mgeçerli bir komut değil yardim & help yazarak varolan kullabileceğin komutları kullanabilirsin\033[1;32m ]" .format(alperen))
