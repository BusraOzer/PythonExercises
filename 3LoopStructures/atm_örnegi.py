print(""" ******************************
Atm Örneği 

1 -> Bakiye Sorgulama

2 -> Para Yatırma

3 -> Para Çekme

Programdan Çıkmak İçin "q" Basınız
******************************
 """)


Mevcut_Bakiye=1000

while True:
    islem=input("İşlemi Seçiniz: ")

    if (islem=="q"):
        print("Yine Bekleriz")
        break
    elif (islem=="1"):
        print("Mevcut Bakiyeniz: {}".format(Mevcut_Bakiye))
    elif (islem=="2"):
        Yatırılacak_Para=int(input("Yatırmak İstediğiniz Miktarı Giriniz: "))
        Mevcut_Bakiye=Mevcut_Bakiye+Yatırılacak_Para
    elif (islem=="3"):
        Cekilecek_Miktar=int(input("Çekmek istediğiniz Miktarı Giriniz"))
        if (Cekilecek_Miktar>Mevcut_Bakiye):
            print("Böyle bir işlem gerçekleştiremezsiniz!")
            continue
        Mevcut_Bakiye=Mevcut_Bakiye-Cekilecek_Miktar
    else:
        print("Yanlış seciç yaptınız!")