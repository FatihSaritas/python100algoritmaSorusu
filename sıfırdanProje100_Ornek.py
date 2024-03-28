#Örnek 1: Ekrana “Merhaba Dünya” yazdıran python kodu yazınız.
#print('Merhaba Dünya')




#Örnek 2: Girilen kullanıcı ismine göre ekrana “Merhaba Kullanıcı” yazdıran python kodunu yazınız.
#kullanici_isimi = input('Gelen inputa kullanıcı yaz: ')
#print('Merhaba'+ kullanici_isimi)




#Örnek 3: Klavyeden girilen iki sayıyı toplayan ve sonucu ekranda gösteren python kodunu yazınız.
# sayi1= 10
# sayi2 =20

# toplam = (sayi1 + sayi2)

# print('Toplam sayı:',toplam )







#Örnek 4: Klavyeden girilen iki sayıyının ortalamasını bulan ve sonucu ekranda gösteren python kodunu yazınız.
# sayi1 = float(input('Sayi 1 Giriniz: '))
# sayi2 = float(input('Sayi 2 Giriniz: '))

# ortalama = (sayi1 + sayi2)/2

# print('Toplanan Sayıların Ortalaması: ',ortalama)






''''
Örnek 5: Klavyeden girilen vize ve final notuna göre vizenin %40 ve finalin %60 ını alan ve sonucu ekranda gösteren python kodunu yazınız.

vize = float(input('Vize Notunuzu giriniz: '))
final = float(input('Final Notunuzu giriniz: '))

ortalama = int(vize)*0.4 + int(final)*0.6


print(f'Vize ve Finalin ortalaması:{ortalama}')
'''



# #Örnek 6: Klavyeden girilen üç yazılı notunun ortalamasını bulan ekranda gösteren python kodunu yazınız.

# not1 = float(input('1.Notunuzu Giriniz: '))
# not2 = float(input('2.Notunuzu Giriniz: '))
# not3 = float(input('3.Notunuzu Giriniz: '))

# ortlama = float(not1 + not2 + not3)/3

# print(f'Not Ortalaması:{ortlama}')






#Örnek 7: Bir dersin ortalaması girilen öğrencinin o dersten geçip geçmediğini gösteren python kodunu yazınız. (50den büyükse geçti değilse kaldı yazdıran örnek python kodu)


# ortalama_notunuz = int(input('Ortalama Notunuz Kaç: '))
# if ortalama_notunuz >= 50 :
#     print('Geçtinizz Tebrikler...')
# else:
#     print('Üzgünüm Kaldınız....')







#Örnek 8:  Klavyeden girilen sayının tek mi çift mi olduğunu yazdıran python kod örneğini yapınız.
# sayi = float(input('Lütfen Sayı Giriniz: '))

# if sayi %2 == 0:    
#         print('Girilen Sayi Çift')
# else:
#     print('Girilen Sayı Tek')
    
    

#Örnek 9:  Klavyeden girilen sayının pozitif mi negatif mi yoksa sıfır mı olduğunu bulan python kodunu yazınız.
# sayi = int(input('Bir Sayı Giriniz: '))

# if int(sayi) > 0 :
#     print('Sayınız Pozitif',+ sayi)
# elif int(sayi) <0 :
#     print('Sayınız Negatif',+ sayi)
# elif int(sayi) == 0:
#     print('Sayınız sıfır: ',+ sayi)







#Örnek 10:  Klavyeden girilen yaşa göre ehliyet alıp alamayacağını bulan python kodunu yazınız.

# yas_bilgisi = input('Yaş Giriniz: ')
# ehliyet_alma_yası = 18

# if int(yas_bilgisi) >= ehliyet_alma_yası:
#     print('Ehliyet Alabilirsiniz yaşınız:',+ int(yas_bilgisi))
# elif int(yas_bilgisi) < ehliyet_alma_yası :
#     print('Ehliyet alamazsınızz yaşınız:',+ int(yas_bilgisi))





#Örnek 11:  1 den 10 a kadar olan sayıları alt alta yazdıran python kodunu yazınız.
# for i in range(1,10):
#     print(i)




#Örnek 12:  1 den 20 ye kadar olan çift sayıları alt alta yazdıran python kodunu yazınız.

# for i in range(1,21):
#     if i %2 == 0:
#         print(i)








#Örnek 14:  1 den 100 e kadar olan sayılardan aynı anda 3 ve 5 e tam bölünen sayıları alt alta yazdıran python kodunu yazınız.

# for sayilar in range(1,100):
#     if (sayilar) %3 == 0 and (sayilar) %5 == 0 :
#         print(sayilar)






# Örnek 16:  Klavyeden kısa kenar uzunluğu ve uzun kenar uzunluğu girilen
# dikdörtgenin alan ve çevresini hesaplayan python kodunu yazınız.


# kisa = input('Kısa Kenar Uzunluğunu Girin : ')
# uzun = input('Uzun Kenar Uzunluğunu Girin: ')
# alan = int(kisa)*int(uzun)
# cevre = 2*(int(kisa)+int(uzun))
# print("Dikdörtgenin Alanı : {0}".format(alan))
# print("Dikdörtgenin Çevresi : {0}".format(cevre))





#Örnek 17:  Klavyeden girilen bir metnin harflerini alt alta yazdıran python kodunu yazınız.
# metin = input('Bir Metin Griniz: ')
# sayac = 0

# while sayac < len(metin):
#     print(metin[sayac])
#     sayac +=1








#Örnek 18:  Klavyeden girilen iki sayı arasındaki sayıları toplayan python kodunu yazınız.

# toplam = 0
# sayi1 = int(input('1. Sayıyı Giriniz: '))
# sayi2 = int(input('2. Sayıyı Giriniz: '))

# for i in range(sayi1 + 1, sayi2):
#     toplam += i

# '''  
# range(sayi1 + 1, sayi2) 
# ifadesinde +1 eklenmesinin nedeni, döngü içinde sayi1'in dahil olmamasını ve sadece sayi1 + 
# 1 değerinden başlayarak sayi2'ye kadar olan sayıları içermesini sağlamaktır.
# '''

# print(f"{sayi1} ile {sayi2} arasındaki sayıların toplamı : {toplam}")






#Örnek 19:  Klavyeden girilen sayının asal sayı olup olmadığını bulan python kodunu yazınız.

# sayac=0
# sayi=input('Bir Sayı Giriniz: ')
# for i in range(2,int(sayi)):
#   if(int(sayi)%i==0):
#     sayac+=1
#     break
# if(sayac!=0):
#   print("Girilen Sayı Asal Değil")
# else:
#   print("Girilen Sayı Asal")







# Örnek 20:  Klavyeden girilen sayıya kadar olan sayılardan tek sayıların
# toplamını ve çift sayıların toplamını ayrı ayrı bulan python kodunu yazınız.


# sayi = input('Sayı Giriniz: ')
# tekToplam = 0
# ciftToplam= 0

# for i in range(1,int(sayi)):
#     if (i %2 == 0):
#         ciftToplam += i
#     else:
#         tekToplam += i

# print(f'Tek Sayıların Toplamı:{tekToplam}') 
# print(f'çift Sayıların Toplamı:{ciftToplam}')               









# Örnek 21:  Klavyeden maaşı ve zam oranı girilen kişinin zamlı maaşını hesaplayan
# python kodunu yazınız.


# yeniMaas = 0

# maas = input('Maaşınızı girin: ')
# zam = input('Zam oranı (%) gir: ')
# yeniMaas = int(maas)+(int(maas)*int(zam)/100)
# print('Zamlı Maaş:',yeniMaas)







#Örnek 23:  Klavyeden kısa kenar ve uzun kenar uzunluğu girilen 
#dikdörtgenin alanını fonksiyon kullanarak hesaplayan python kodunu yazınız.

# def dikdortgenAlan(genislik,yukseklik):
#     alan = genislik * yukseklik
#     print('Alan:',alan)
#     return alan

# gen = float(input('Genişlik: '))
# yuk = float(input('Yükseklik: '))

# dikdortgenAlan(gen,yuk)






#Örnek 24:  Önceden belirlenen bir liste içerisinde bulunan sayılardan kaç 
# tanesinin 5’in katı olduğunu bulan python kodunu yazınız.

# sayilar = [18,15,22,19,85,32,65,30,95,10,12,20,32,55,34,28,101,5,4,32]

# sayac = 0

# for sayi in sayilar :
#     if sayi %5 == 0 :
#         print(f'{sayi} Sayısı 5 in katıdır.')
#         sayac += 1
        
# print("5'in katı olan sayı adedi: "+ str(sayac))        
#printde string yaı oldugu için sayacı stringe cevirdik yoksa birleştirme yapamazdık.











#Örnek 25:  Klavyeden girilen başlangıç ve bitiş sayıları
# arasında bulunan çift sayıların ortalamasını bulan python kodunu yazınız

# toplam = 0
# sayac = 0

# baslangic = int(input('Başlangıç sayısı: '))
# bitis = int(input('Bitiş sayısı: '))

# for sayi in range(baslangic,bitis+1):
#     if sayi %2 == 0 :
#         toplam = toplam + sayi
#         sayac = sayac + 1

# print('Ortalama:',(toplam/sayac))        
        











#Örnek 27:  Klavyeden girilen başlangıç ve bitiş sayıları arasında 
# bulunan sayıların ortalamasını bulan python kodunu yazınız.

# toplam = 0
# sayac = 0

# baslangic = int(input('Başlangıç yazın:'))
# bitis = int(input('Bitiş yazın:'))

# for sayi in range(baslangic,bitis+1):
#     toplam = toplam + sayi
#     sayac = sayac + 1
    
# print('Ortalaması: ',(toplam/sayac))    











#Örnek 28:  Klavyeden girilen başlangıç ve bitiş sayıları
# arasında bulunan sayıların toplamını bulan python kodunu yazınız.


# toplam=0
# sayac=0
# baslangic = input("Başlangıç Sayısı :")
# bitis = input("Bitiş Sayısı :")
# for sayi in range (int(baslangic), int(bitis)+1):
 
#         toplam=toplam+sayi
#         sayac=sayac+1
# print('Aradaki Sayıların Toplamı:',toplam)
 




#Örnek 31: Python tkinter kütüphanesini kullanarak form 
# pernceresi oluşturan kodunu yazınız.
# import tkinter

# nesne = tkinter.Tk()
# nesne.mainloop()












#Örnek 32:  Python tkinter kütüphanesini kullanarak form 
# pernceresi ve Entry (text kutusu) oluşturan kodunu yazınız.

# from tkinter import *
 
# from tkinter import messagebox

# pencere = Tk()
 
# pencere.title("www.algoritmaornekleri.com")
# pencere.geometry("320x175")
 
# # grid form çizdirme
# uygulama = Frame(pencere)
# uygulama.grid()
 
# L1 = Label(uygulama, text="İfade Girin")
# L1.grid(padx=110, pady=10)
 
# E1 = Entry(uygulama, bd=2)
# E1.grid(padx=100, pady=3)
 
# # formu çiz
# pencere.mainloop()











#Örnek 33:  Python tkinter kütüphanesini kullanarak form pernceresi 
# ve Listbox (Liste kutusu) oluşturan kodunu yazınız.

 
# from tkinter import *
 
# from tkinter import messagebox
 
# pencere = Tk()

# pencere.title("www.algoritmaornekleri.com")
# pencere.geometry("400x300")

# uygulama = Frame(pencere)
# uygulama.grid()

# Lb1 = Listbox(uygulama)
# Lb1.insert(1, "İstanbul")
# Lb1.insert(2, "Ankara")
# Lb1.insert(3, "İzmir")
# Lb1.insert(4, "Kayseri")
# Lb1.insert(5, "Antalya")
# Lb1.grid(padx=110, pady=10)
 
# pencere.mainloop()












#Örnek 34:  Klavyeden girilen üç yazılı notunun ortalamasını 
# bulan python kodunu yazınız.

# y1 = float(input('1.Yazılı notu giriniz:'))
# y2 = float(input('2.Yazılı notu giriniz:'))
# y3 = float(input('3.Yazılı notu giriniz:'))

# toplam = (y1 + y2 + y3)
# ortlama = toplam /3 

# print(f'3 Yazılı notunun ortalaması: {ortlama}')











#Örnek 35:  Klavyeden girilen sayının tek sayı mı 
# çift sayı mı olduğunu bulan ve sonucu ekranda gösteren python kodunu yazınız.

# sayi = int(input('Bir sayı giriniz:'))

# if sayi %2 == 0:
#     print('Sayınız Çift sayıdır..')
# else:
#     print('Sayınız tektir.')














#Örnek 36:  Örnek :Bir otoparkın ücret tarifesi aşağıdaki gibidir:
# 1 saate kadar: 5 TL
# 1-5 saat arası: Saat başı 4 TL
# 5 saatten fazla: Saat başı 3 TL
# Buna göre kullanıcının girdiği otoparkta kalınan saat süresine göre ödenecek miktarı bularak ekrana yazdırınız.


# saat = int(input('Kaldığınız süreyi giriniz: '))

# ucret = 0
# if saat <=1:
#     ucret = 5
# elif saat <=5:
#     ucret = saat *4 
# else:
#     ucret = saat * 3
# print('Ödemeniz Gereken ücret:',str(ucret))  






#Örnek 37:  Klavyeden girilen bir ifadeyi ekrana 10 defa yazdıran python kodunu yazınız.

# metin = input('Bir ifade giriniz: ')
# for x in range(10):
#     print(metin)
    
    



#Örnek 38:  Klavyeden girilen bir ifadeyi klavyeden girilen bir sayı
# kadar ekrana yazdıran python kodunu yazınız.    

# metin = input('Bir ifade giriniz: ')
# sayi = int(input('Kaç defa yazdırılsın: '))

# for x in range(sayi):
#     print(metin)








#Örnek 39:  Klavyeden aralarına virgül 
# konularak yazılan tüm sayıları toplayan python kodunu yazınız.

# numaralar = input('Virgül ile sayıları giriniz: ')

# print(f'Girdiğiniz sayılar: {numaralar}')

# numaralar = numaralar.split(",")
# toplam = 0
# for n in numaralar:
#     toplam = toplam + int(n)
# print(f'Girdiğiniz sayıların toplamı:{toplam}')    







#Örnek 40:  Klavyeden aralarına virgül konularak yazılan
# tüm sayıların ortalamasını hesaplayan python kodunu yazınız.

# numaralar = input("Virgül ile sayıları giriniz: ")

# sayilar_listesi = [int(sayi) for sayi in numaralar.split(",")]

# toplam = sum(sayilar_listesi)
# ortalama = toplam / len(sayilar_listesi)

# print(f"Girdiğiniz Sayılar: {sayilar_listesi}")
# print(f"GİRDİĞİNİZ SAYILARIN ORTALMASI: {ortalama:.2f}")
# #.2f ifadesi, bir ondalıklı sayının yalnızca iki basamak sonra virgülden sonra gösterilmesini sağlayan bir formatlama kodudur.
# # Bu, virgülden sonra iki ondalık hane istediğimizi belirtir.








#Örnek 41:  Klavyeden başlangıç değeri, bitiş değeri ve artış miktarı
# girilen sayıları alt alta yazdıran python kodunu yazınız.

# birincisayi = int(input('Başlangıç değerini giriniz: '))
# ikincisayi =int(input('Bitiş değerini giriniz: '))
# adim = int(input('Artış miktarını giriniz: '))

# for i in range(birincisayi,ikincisayi,adim):
#     print(i)




#Örnek 42:  0 dan 100 e kadar olan çift sayıların toplamını hesaplayan ve sonucu 
# yazdıran python kodunu while döngüsü kullanarak yapan kodunu yazınız.
# sayac = 0
# toplam = 0

# while sayac <= 100:
#     sayac = sayac + 2
#     toplam = toplam + sayac
# print(f'0 ile 100 arasında ki çift sayıların toplamı:{toplam}')    







#Örnek 43:  0 dan 100 e kadar olan tek sayıların toplamını hesaplayan ve 
# sonucu yazdıran python kodunu while döngüsü kullanarak yapan kodunu yazınız.

# sayac = 1
# toplam = 0
# while sayac <= 100:
#     sayac = sayac + 2
#     toplam = toplam + sayac
 
# print(f"0 ile 100 arasındaki tek sayıların toplam:{toplam}")








#Örnek 44:  Klavyeden girilen sayıya kadar olan sayıların toplamını 
# hesaplayan ve sonucu yazdıran 
# python kodunu while döngüsü kullanarak yapan kodunu yazınız.

# toplam = 0
# sayac = 0
# bitis = int(input('Bitiş Değerini Giriniz: '))

# while sayac <= bitis:
#     sayac = sayac + 1
#     toplam = toplam + sayac
# print(f'{bitis},sayısna kadar olan sayıların toplamı... {toplam}')
 
 
 
 
 
 
#Örnek 46:  Klavyeden girilen sayıya kadar olan çift sayıların toplamını hesaplayan 
# ve sonucu yazdıran python kodunu while döngüsü kullanarak yapan kodunu yazınız.

# sayac = 0
# toplam = 0
# bitis=int(input("Bir Sayı Giriniz: "))
# while sayac <= bitis:
#     sayac = sayac + 2
#     toplam = toplam + sayac
 
# print(f"{bitis}, sayısına kadar olan çift sayıların toplamı:{toplam}")
 
#Eğer bunun tek sayı olanlarını bulmak istersek sayac 1 veririz 2,2 ekleyeceginden 
#toplayacagı sayılar hep tek asyı olacak mantıgı anlamışsındır.
 
 
 
 
 
 
 
 
 
 
#Örnek 47:  Klavyeden girilen bir metni 
#harflarine ayıran python programını while döngüsü ile yazdıran kodunu yazınız.

# metin = input('Bir metin giriniz: ')
# sayac = 0
# while sayac < len(metin):
#     print(metin[sayac])
#     sayac = sayac + 1









#Örnek 48:  0 ile 100 arasında 10 tane rastgele tam sayı üreten ve bu sayılardan 
# en büyüğü ile en küçüğünü bulan ve ekranda gösteren python kodunu yazınız.

# import random

# sayilar = []
# for i in range(0, 10):
#     rand = random.randint(0, 100)
#     sayilar.append(rand)
#     print(rand)
 
# minNumber = sayilar[0]
# maxNumber = sayilar[0]
 
# for i in range(0, 10):
#     if minNumber > sayilar[i]:
#         minNumber = sayilar[i]
#     if maxNumber < sayilar[i]:
#         maxNumber = sayilar[i]
 
# print(f"Dizideki En Büyük Değer : {maxNumber} ")
# print(f"Dizideki En Küçük Değer : {minNumber} ")
 
 
 
 
 
 
 
 
#Örnek 49:  Kullanıcının klavyeden kilo bilgisi alınarak kilo 50 ve altında ise 
#zayıfsın, 50-80 arası fitsin, 80 ve üstü ise 
# kilo almışsın şeklinde ekranda yazdıran python kodunu yazınız.

 
# kilo=int(input("Kilonuzu Giriniz: "))
# if kilo<51: print("Zayıfsınız") 
# if (kilo>50 and kilo<80): 
#   print("Normal Kilodasınız") 
# if (kilo > 80):
#   print("Fazla kiolusunuz")







#Örnek 50:  Kullanıcının klavyeden yaş bilgisi alınıp 18 yaşından küçükse çocuk 
# 18-40 yaş arası ise genç, 40-60 yaş arası
#ise orta yaşlı 60 yaştan büyükse yaşlı şeklinde 
# ekrana yazdıran programın python kodlarını yazınız.

# yas = int(input('Yaş Bilgsi Giriniz: '))

# if yas <= 18:
#     print('Çoçuk')
# if 18 < yas <= 40:
#     print('Genç')   
# if  40 < yas < 60 :
#     print('orta yaşlı') 
# if yas >= 60:
#     print('Yaşlı')








#Örnek 51:  Klavyeden girilen iki sayının yine klavyeden girilen aritmetik operatör işaretlerine göre (toplama, çıkarma, çarpma bölme) dört işlem yapan ve sonucu ekranda gösteren python kodunu yazınız.

# sayi1 = int(input('1.Sayi giriniz: '))
# sayi2 = int(input('2.Sayi giriniz: '))

# sec = input('Seçiminiz yapınız (+,-,*,/): ')

# if sec == '+':
#     print(sayi1,'+',sayi2,'=',sayi1+sayi2)

# if sec == '-':
#     print(sayi1,'-',sayi2,'=',sayi1-sayi2)    
    

# if sec == '*':
#     print(sayi1,'*',sayi2,'=',sayi1*sayi2)    


# if sec == '/':
#     print(sayi1,'/',sayi2,'=',sayi1/sayi2)    








#Örnek 52:  Klavyeden girilen bir sayının rakamlarının toplamını bulan ve ekranda gösteren python kodunu yazınız.

# sayi = int(input("Bir Sayı Giriniz: "))
# toplam = 0

# while sayi > 0:
#     birler_basamagi = sayi % 10
#     toplam += birler_basamagi
#     sayi //= 10

# print("Girilen Sayının Rakamları Toplamı:", toplam)









#Örnek 53:  Program çalıştırıldığı anda o anın tarih ve saat bilgilerini ekrana yazdıran python kodunu yazınız.


# import time
# print (time.ctime())








#Örnek 54:  Şu anki sistemin tarihini ekrana yazdıran python kodunu yazınız.


# import time
# print (time.strftime("%d/%m/%Y"))









#Örnek 55:  Klavyeden Fahrenheit cinsinden girilen sıcaklığı Dereceye çeviren python kodunu yazınız.


# f=float(input("Sıcaklığı F cinsinden giriniz: "))
# c=(f-32)/1.8
# print(f, "F = ", c,"C'dir")









#Örnek 56:  Klavyeden bir kenar uzunluğu girilen karenin alanını ve çevresini bulan ve ekrana yazdıran python kodunu yazınız.

# kenar = int(input('Bir kenar uzunlugu giriniz: '))
# cevre = kenar*4
# alan = kenar**2
# print('karenin çevreesi: ',cevre)
# print('karenin alanı: ',alan)








#Örnek 57:  Klavyeden girilen saniye değerinin kaç saat kaç dakika ve kaç saniye olduğunu bulan python kodunu yazınız

# saniye = int(input('Saniye giriniz: '))
# saat = saniye //3600 #1 saat 3600 saniye eşittir
# saniye = saniye%3600
# dakika = saniye // 60
# saniye = saniye%60

# print('Girdiğiniz saniyenin saat dönüşümü:',saat,'sa',dakika,'dk',saniye,'sn')











#Örnek 58:  Klavyeden boy ve kilo bilgileri girilen kişinin beden kitle endeksini hesaplayan python kodunu yazınız




# boy=float(input("Boyunuzu giriniz(m): "))
# kilo=float(input("Kilonuzu giriniz(kg): "))
# bki=kilo/(boy**2)
# print("Beden Kitle İndeksi Değeriniz:",round(bki,2))
#Round cıktının 25.340583 olmasını filtreler son 2 basamagı gösterir.








#Örnek 59:  Klavyeden girilen iki sayıdan büyük olanı bulan ve ekranda gösteren python kodunu yazınız.


# -*- coding: utf-8 -*-

# a=int(input("1. Sayıyı Giriniz: "))
# b=int(input("2. Sayıyı Giriniz: "))
# if a>b:
#  print("Birinci sayı büyük!")
# elif b>a:
#   print("İkinci sayı büyük!")
# else:
#   print("İki sayı eşit")







#Örnek 60:  Klavyeden girilen not ortalamasına göre kişinin takdir teşekkür normal geçme yada sınıf tekrarı yapması gerektiğini gösteren python kodunu yazınız.



# ortalama=float(input("Not ortalamanızı giriniz: "))
# if ortalama>=85:
#  print("Takdir Belgesi Alamaya Hak Kazandınız!")
# elif ortalama>=70:
#  print("Teşekkür Belgesi Alamaya Hak Kazandınız!")
# elif ortalama>=50:
#  print("Sınıfı Geçtiniz")
# else:
#  print("Sınıf tekrarı...")





# #Örnek 63:  Klavyeden girilen bölünen ve bölen sayılarına göre bölen sayının sıfır olup olmadığını kontrol eden ve ona göre sonuç yada uyarı veren python kodunu yazınız


# bolum=int(input("Bölünecek sayıyı giriniz: "))
# bolen=int(input("Bölen sayıyı giriniz "))
# if bolen!=0:
#  print("Sonuç: ", bolum/bolen)
# else:
#  print("Sıfıra bölme işlemi yapılamaz!")







#Örnek 64:  Klavyeden 1 ile 5 arasında bir değer giren ve bu değeri yazı ile yazdıran bu değerlerin dışında bir değer girildiğinde uyarı mesajı veren python kodunu yazınız.



# deger=int(input("1...5 arasında değer giriniz: "))
# if deger<1:
#  print("Değer çok küçük...")
# elif deger==1:
#  print("Bir")
# elif deger==2:
#  print("İki")
# elif deger==3:
#  print("Üç")
# elif deger==4:
#  print("Dört")
# elif deger==5:
#  print("Beş")
# else:
#  print("Değer çok büyük...")
# print("Tamamlandı...")









#Örnek 65:  Klavyeden girilen bir sayının 2 ve 3 e veya sadece 2 ye veya sadece 3 e tam bölünüp bölünmediğini yada hiç birine bölünmediğini kontrol eden python kodunu yazınız.

# print("-----Girilen Sayının 2 ve 3'e Bölünme Durumu----")
# sayi=int(input("Sayı Giriniz: "))
# if sayi%2==0 and sayi%3==0:
#  print("Girdiğiniz sayı 2 ve 3'e tam bölünüyor.")
# if sayi%2==0 and sayi%3!=0:
#  print("Girdiğiniz sayı sadece 2'ye tam bölünür.")
# if sayi%3==0 and sayi%2!=0:
#  print("Girdiğiniz sayı sadece 3'e tam bölünür.")
# if sayi%2!=0 and sayi%3!=0:
#  print("Girdiğiniz sayı 2 ve 3'e tam bölünmez.")







#Örnek 66:  0 dan 30’a kadar olan sayılardan 2 ve 3 bölünenleri ekranda sıralayan programın python kodlarını yazınız.



# a=0
# while(a<30):
#   a=a+1
#   if (a%2==0):
#     print(a, "2'ye bölünür")
#   if (a%3==0):
#     print(a, "3'e bölünür")








#Örnek 67:  Klayeden girilen beş adet sayının toplamını bulan ve bulunan toplamın tek sayımı yoksa çift sayı mı olduğunu bulan python kodunu yazınız.



# sayi1=int(input("Birinci sayıyı giriniz:"))
# sayi2=int(input("İkinci sayıyı giriniz:"))
# sayi3=int(input("Üçüncü sayıyı giriniz:"))
# sayi4=int(input("Dördüncü sayıyı giriniz:"))
# sayi5=int(input("Beşinci sayıyı giriniz:"))
 
# topla=sayi1+sayi2+sayi3+sayi4+sayi5
# print("Sayıların Toplamı:",topla)
 
# if(topla%2==0):
#     print("Sayıların Toplamı Çift")
# else:
#     print("Sayıların toplamı Tek")







#Örnek 69:  Klavyeden girilen beş tane sayıdan en büyüğünü bulup ekranda gösteren python kodunu yazınız.

# a=int(input("Birinci sayıyı giriniz:"))
# b=int(input("İkinci sayıyı giriniz:"))
# c=int(input("Üçüncü sayıyı giriniz:"))
# d=int(input("Dördüncü sayıyı giriniz:"))
# e=int(input("Beşinci sayıyı giriniz:"))
# print("--------------------------")
# if a>b and a>c and a>d and a>e:
#     print("En büyük sayı:",a)
# elif b>c and b>d and b>e:
#     print("En büyük sayı:",b)
# elif c>d and c>e:
#     print("En büyük sayı:",c)
# elif d>e:
#     print("En büyük sayı:",d)
# else:
#     print("En büyük sayı:",e)







#Örnek 71:  Klavyeden 0 rakamı girilene kadar girilen tüm sayıların kaç tane olduğunu ve bu sayıların toplamını bulan ve ekranda gösteren python kodunu yazın
# toplam = 0
# sayac = 0
# sayi = int(input("Bir Sayı Giriniz (0-çıkış): "))

# while sayi != 0:
#     toplam = toplam + sayi
#     sayac = sayac + 1
#     sayi = int(input("Bir Sayı Giriniz (0-çıkış): "))

# print("Girilen", sayac, "sayının toplamı:", toplam)








#Örnek 72:  Klavyeden 0 rakamı girilene kadar girilen tüm sayıların kaç tane olduğunu ve bu sayıların ortalamasını bulan ve ekranda gösteren python kodunu yazınız.,

# toplam=0
# sayac=0
# sayi=int(input("Bir Sayı Giriniz 0-çıkış:"))
# while sayi!=0:
#     sayi=int(input("Bir Sayı Giriniz 0-çıkış:"))
#     toplam=toplam+sayi
#     sayac=sayac+1
 
# ortalama=toplam/sayac    
# print ("Girilen ",sayac," sayının ortalaması:",ortalama)






#Örnek 73:  Klavyeden girilen taban ve üs değerine göre o sayının üssünü hesaplayan ve sonucu ekranda gösteren python kodunu y



# import math
 
# taban=int(input("Taban Değerini Giriniz: "))
# us=int(input("Üs Değerini Giriniz: "))
 
# usAl=math.pow(taban,us)
 
# print("Girmiş olduğunuz değerlerin üssü = ",usAl)








#Örnek 74:  Klavyeden girilen bir sayının karekökünü bulan ve ekranda gösteren python kodunu yazınız

# import math
 
# sayi1=int(input("Sayıyı giriniz: "))
 
# kareKok=math.sqrt(sayi1)
 
# print ("Girilen Sayının Karekökü =" ,kareKok)






#Örnek 78:  Daha önceden belirlenmiş bir liste içerisinden rastgele bir sayı seçen ve ekranda gösteren python kodunu yazınız.

# import random
 
# liste=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# sayi=random.choice(liste)
# print (sayi)

#choice seç demek 








#Örnek 80:  Klavyeden girilen yıl ve o yılın ayının takvimini ekranda gösteren python kodunu yazını

# print("Oluşturmak istediğiniz yılı ve kaçıncı ayı olduğunu giriniz")
# yil = int(input("Seneyi Giriniz: "))
# ay = int(input("Ayı Giriniz: "))
 
# #Takvim modülünü ekliyoruz.
# import calendar
# #Son olarak da buraya takvim görüntüleme kodunu ekliyoruz.
# print(calendar.month(yil, ay))




#Örnek 82:  Klavyeden girilen bir ismin klavyeden girilen bir sayı kadar yan yana yazdıran python kodunu yazınız.

# isim=input("İsim Giriniz:")
# sayi=int(input("Kaç defa yazılsın:"))
# print((isim+" ") *sayi)






#Örnek 84:  Klavyeden girilen 3 tane açının toplamının 180 olup olmadığını kontrol eden ve üçgen oluşturup oluşturmadığını kontrol eden python kodunu yazınız



# sayi1=int(input("Birinci Açıyı Giriniz:"))
# sayi2=int(input("İkinci Açıyı Giriniz:"))
# sayi3=int(input("üçüncü Açıyı Giriniz:"))
 
# toplam=sayi1+sayi2+sayi3
 
# if(toplam==180):
#     print("Bu açılar üçgen oluşturur")
# else:
#     print("Bu açılar üçgen oluşturmaz")





