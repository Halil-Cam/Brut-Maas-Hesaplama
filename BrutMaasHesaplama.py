print("------> Brüt Maaş Hesaplama Uygulamasına Hoşgeldiniz <------")
print("\n\n")
maas=int(input("Lütfen Aylık Maaşınızı Giriniz: "))
vergi = 0.15
print("vergi oranı =  ",vergi)
vergi_hesapla = maas*vergi
sonuc = maas - vergi_hesapla
print("Hesaplanan vergi Miktarı = ",vergi_hesapla)
print(f"Aylık Brüt Geliriniz = {sonuc} ")
