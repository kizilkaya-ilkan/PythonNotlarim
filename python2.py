sayilar = [x for x in range(1,100_001) if x % 2 == 0 and x % 3 == 0]

print(str(sayilar))


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


#ATM UYGULAMASI

def Kullbilgi():
    
    KullaniciBilgi = {
        "Ad" : "İlkan",
        "Soyad" : "Kızılkaya",
        "Yaş" : "23",
        "Para" : 2000,
       
    }
    print(KullaniciBilgi)

def Money(Anapara , Ekleme):

    Kalanbakiye = 2000

    if Ekleme == 0:
        Kalanbakiye -=  Anapara
        print("Hesapta Kalan Para = {}".format(Kalanbakiye))
    elif Anapara == 0:
        Kalanbakiye +=  Ekleme
        print("Hesapta Kalan Para = {}".format(Kalanbakiye))

işlem = int(input("1-ParaÇekme \n2-Para Yatırma \n3-Kart Bilgileri \n4-Kart iade\nSeçilen işlem: "))
if işlem == 4:
    print("Kart iadesi yapılıyor.")
elif işlem  == 1:
    cekilenPara = int(input("Çekilecek Para Belirtiniz: "))
    Money(cekilenPara,0)
elif işlem  == 2:
    yatırılanpara = int(input("Yatıralacak Para Belirtiniz: "))
    Money(0,yatırılanpara)
elif işlem  == 3:
    print(Kullbilgi())


