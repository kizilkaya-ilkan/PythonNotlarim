
from os import X_OK
from typing import List


def faktörelAl(sayi):
    faktörel = 1
    for i in range(1, sayi + 1):
        faktörel = faktörel * i 
    return faktörel

print(faktörelAl(5))



def Hesaplar(*Sayilar,Islem):
    
    if Islem == "+":
        sonuc = 0
        for i in Sayilar:
            sonuc += i
    else:
        sonuc = 0 
        for i in Sayilar:
            sonuc -= i
    return sonuc


print(Hesaplar(1,2,3,4,5,6,Islem="+"))

print("1,2,3,4,5,6,7,8,9,0",sep=" , ")

print("1,2,3,4,5,6,7,8,9,0 " ,end= " Son kısım koyulan \n")

b = "İlkan"

print(*b)

print("Hoş geldiniz {} ".format(b))


dosya =  open("Yazdirma_proje.txt","w") ## print çıktısını dışarı yazdırma ... 

print("İlkan Kızılkaya", file=dosya)



def sayilarinToplami(*sayilar):

    toplam = 0

    for i in sayilar:
        toplam += i

    return toplam

Sayilar = [ x for x in range(1 , 1001)] # 1 DEN BASLAYIP 1000 KADAR OLAN DEGERLERİ SAYILARI GÖNDER.

print(sayilarinToplami(1,2,3,4,5,6,7,8,9,0))

print(sayilarinToplami(*Sayilar))




#Listeler


Ogrenciler = ["İlkan","Umut","Huawei","Casper","A","B","C"]

print(Ogrenciler[0]) # index 0'daki ELemanı getir.


Ogrenciler.remove("Umut") # Umut'adlı şahısı silme işlemi yapıyor 

print(len(Ogrenciler))

for Ogrenci in Ogrenciler:
    print(Ogrenci)

print(Ogrenciler[0:2]) # ilk 2 index'i Al.

print(Ogrenciler[::-1]) # Tersten indexleri yazdırma.


Ogrenciler[5] = "İsim_Değişikligi_Yapıldı."  # index_Değişikligi Yapıldı.

print(Ogrenciler)


AltSinifOgrenciler = ["Delgado","Ronaldo","Hagi"]


belge = open("Belge.txt","w")

print(Ogrenciler + AltSinifOgrenciler, file= belge) # Listeleri Birleştirme.

List = [1,5,3]

List.append(11) # Oluşyurduğumuz Listeye 11 Rakamını ekliyoruz.

print(List)

List.pop()  # Elemanın en sonundakini çıkarıyor.

print(List)

List.sort() # Elemanları Kücükten , Büyüge sıralama işlemi yapıyor...

print(List)

List.sort(reverse= True) # Büyükten , Küçüge sıralama işlemi yapar...

print(List)


user = ["ilkan26", "ilkan98" , "ilkan3111"]
passworld = ["1234","123","12345"]

kullaniciDataVerileri = [user,passworld]


print(kullaniciDataVerileri[0][0],kullaniciDataVerileri[1][0]) ## ortak listeleme yöntemleri



#TUPLE DEĞİŞKENLERİ



a = (1,2,3,4,5,6,7,8,9,"ilkan","Ela","Turkiye")

yenisonuc = tuple(a)

print(yenisonuc)


print(yenisonuc.count("ilkan")) # tuple içinde kaç tane varsa

print(yenisonuc.index(1)) #100 ' index nedir ? bul

print(yenisonuc.__contains__("Turkiye")) # Türkiye Varmı - Yokmu onu kontrol et ?

if "Turkiye" in yenisonuc:  ## yenisonuc içinde  "Türkiye" kelimesini arıyor...
    print("Türkiye Var")
else:
    print("Türkiye Yok")




#Dictionary (Sözlük yapısı)

 
Sözlük = {  # Sözlük = dict() ' olarakta kullanılabilir. 
    
    "İlkan":23 ,
    "Umut":45 ,
    "Buse":27 ,
    "Haydar":24 ,
    "Bonzai":66 ,

        }

print(Sözlük["İlkan"]) ## İlkana denk gelen degeri ekrana yazdırıyor...


Uyeler = {"Üyeler":["ilkan","redkit26","Huawei","Everese"],
         "Moderetörler" : ["ilkan","admin26","admin"] 
}

Uyeler["SuperModeratörler"] = {"Veli","Ahmet"} ## Sözlük Yapısına Veri Ekleme işlemi..


Uyeler["Üyeler"].append("Turgut") ## SÖzlük Sonradan Veri ekleme işlemi.

Uyeler["Moderetörler"].remove("admin26") ## Sözlük kısmından admin26'yi çıkardık.




kopyaAL = Uyeler.copy() ## kopyalama işlemi.

Uyeler.pop("Moderetörler") ## Moderetörleri sildi komple..

print(Uyeler["Üyeler"])






KullaniciSayisi = Uyeler.values()  # Uyeler Sözlügündeki İçeriğini  belirliyor.

for kullanici in KullaniciSayisi: 

    print(kullanici)


KullaniciSayisibir = Uyeler.keys() # Uyeler Sözlügündeki AnaBaşlıkları Çıkarmaya Sağlıyor.


for kullanicibir in KullaniciSayisibir: 

    print(kullanicibir)


KullaniciSayisibir = Uyeler.items() # Uyeler Sözlügündeki hepsini Çıkarmaya Sağlıyor.


for i,j in KullaniciSayisibir: 

    print(i,j)





#input fonksiyonları


print (""" 
**** HESAP MAKİNESİ ÖRNEĞİ ****
""")

sayiBir = float(input("Sayi Bir Değerini giriniz:"))
sayiTwo = float(input("Sayi İki Değerini giriniz:"))

print(""" 

Toplamları : {}
Farkları : {}
Çarpımları : {}
Bölümleri : {}

""".format(sayiBir+sayiTwo, sayiBir-sayiTwo,sayiBir*sayiTwo,sayiBir/sayiTwo))


# Çalışma Soruları #

# Üçgenin hipotenusunu bulma işlemi yapılacak.


print("""

**** Hipotenüs Bulma Programı ****

""")


def hipotenüs(a,b):

    sonuc = 0

    sonuc = (a*b)

    return sonuc


Sayibir = float(input("A' kenarını giriniz:"))

Sayiiki = float(input("B kenarını giriniz:"))

print(hipotenüs(sayiBir,sayiTwo))






# Sözlük yapısını kullanarak yapılacak örnek #



print("""

*** Sözlük Yapısı Örnegi ***

""")


Sözlükler = {

"İngilizce:":["Hello","Exit","Delete","Insert","Add","Good"],
"Türkce":["Merhaba","Çıkış","Sİl","Ekleme","Ekle","İyi"]
}

ingilizcekelime = str(input("İngilizce Kelimeyi Giriniz: "))
türkcekelime = str(input("Türkçe Kelimeyi Giriniz: "))

Sözlükler["İngilizce:"].append(ingilizcekelime)
Sözlükler["Türkce"].append(türkcekelime)


ekrancıktısı = Sözlükler.items()

for i,j in ekrancıktısı:
    print(*i,*j)



# Çözüm 2 #


KelimeSatiri = dict()

ing = str(input("İngilizce Kelimeyi giriniz: "))
TR = str(input("Türkçe Kelimeyi giriniz: "))

KelimeSatiri["ingilizce"] = ing
KelimeSatiri["Türkce"] = TR

print(KelimeSatiri)




# VİZE VE FİNAL NOT HESAPLAMA #


def NotGecme(vize,final):

    sonuc =  (0.4 * vize) + (0.6 * final)

    if sonuc > 45:

        print("Ortalamanız {} , Dersi Geçtiniz. ".format(sonuc))

    else:
        
        print("Ortalamanız {} , Malesef Dersten Kaldınız. ".format(sonuc))

    with open("Kaydet.txt", "w") as okuma: # Veriyi kaydetme komutu.

        okuma.writelines("Ogrencinin Başarı Notu {}".format(sonuc))

vize = float(input("Vize Notunu giriniz: "))
final = float(input("Final Notunu giriniz: "))


print(NotGecme(vize,final))




# FOR DÖNGÜLERİ ÖRNEKLERİ

GirilenDegerlerr = int(input("Bir rakam giriniz: "))

Rakamlar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

Rakamlar.append(GirilenDegerlerr)

Sonuclaar = []

for x in Rakamlar:

    Sonuclaar.append(x **2)

    print(*Sonuclaar)




SinavSonucları = [(50,47),(70,70),(100,10),(45,65)]


for v,j in SinavSonucları:

    print(v,j)


playList = {  # Sözlük Yapısı 
"Mustafa Sandal": "Ayabenzer",
"Tarkan" : "DuduDilleri",
"Gaye Su Akyol" : "Mendilinin Yeşili", 
"Metin Işık" : "Ağla Gözüm"
}




for Sanatcilar in playList.keys():

    print(Sanatcilar)



#While DÖngüsü #


a = 10

while (a> 0):
    print(a)
    a -= 1



huawei = ["İlkan","Kızılkaya",3,4,5,6]

uzunlukHesaplamaMetodu = len(huawei)

sayac = 0

while uzunlukHesaplamaMetodu > sayac:
    print(huawei[sayac])
    sayac += 1


#Random Uygulaması

import random


turasayisi = 0
yazısayisi = 0

parayüzeyi = ["YAZI","TURA"]

GirilenDegişken = int(input("Para Kaç Kere Atılsın ? "))


while 0 < GirilenDegişken:

    GirilenDegişken -= 1

    randomSonucuGelenSayisi = random.choice(parayüzeyi)
    
    if randomSonucuGelenSayisi == "TURA":
        turasayisi +=1
        
    else:
        yazısayisi +=1
      

print("Toplam Atılan Zar Sayısı = {} , Toplam Gelen Tura Sayısı = {} , Toplam Gelen Yazı Sayısı = {}".format(GirilenDegişken,turasayisi,yazısayisi))



#FOR DÖNGÜLERİ ÖRNEKLERİ KULLANIMI

    

sayacii = 0

for x in  range(10_000): # 1 den başlayıp , 10.000 kadar gidiyor.

    print(x)

while sayacii<1000: # 1 den başlayıp , 10.000 kadar gidiyor.

  print(sayacii)

  sayacii +=1


for y in range(0,10_000,5): # 0'dan baslayıp 10.000 kadar 5 er artıyor...

        print(y)

for j in range(20,10_000): # 20 den baslayıp , 10.000 kadar gidiyor.

    print(j)
    


# ASAL SAYI ÖRNEGİ


degerGirisi = int(input("Bir değer giriniz."))

asalSayiCiktisi = [2]

asalOlmayanCiktiSayisi = []

total = 1

for asal in range(2,degerGirisi+1):

    if asal % 2 == 1:

        asalSayiCiktisi.append(asal)

        total +=1

    else:

        asalOlmayanCiktiSayisi.append(asal)

asalOlmayanCiktiSayisi.pop(0)

print("Asal Olan Sayılar {} , Asal Olmayan Çıktı Sayısı {} , Total Çıktı Sayısı {}".format(asalSayiCiktisi,asalOlmayanCiktiSayisi,total))




# 1 -den 100.000 kadar degerleri hem 2 ye hemde 3 e bölünebilenleri yazılacak.


ikiveüc = []

for i in range(1,100_000):

    if i % 2 == 0 and i % 3 == 0:

        ikiveüc.append(i)
    else:
        continue
    
print(ikiveüc)



# pozitif tam sayi faktör al 

sonuc = 1
pozitifSayi = int(input("Bir Pozitif Sayi Giriniz: "))

if pozitifSayi < 0:

    print("Hatalı giriş")
else:
    for k in range(pozitifSayi+1):
            if(k == 0):
                continue
            else:
                sonuc = sonuc * k
print("Girilen Pozitif Sayi = {} , Faktörel sonucu = {} ".format(pozitifSayi,sonuc))





    
        






    






























