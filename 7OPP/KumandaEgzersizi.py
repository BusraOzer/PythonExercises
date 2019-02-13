import time
import random

class Kumanda():
    def __init__(self,tv_durumu="Kapalı",tv_ses=0,kanal_listesi=["Trt"],kanal="trt"):
        self.tv_durumu=tv_durumu
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal

    def tv_ac(self):
        if(self.tv_durumu=="Açık"):
            print("Televizyon zaten açık")
        else:
            print("Televizyon açılıyor")
            self.tv_durumu="Açık"

    def tv_kapat(self):
        if (self.tv_durumu == "Kapalı"):
            print("Televizyon zaten kapalı")
        else:
            print("Televizyon kapanıyor")
            self.tv_durumu = "Kapalı"

    def ses_ayarları(self):
        while True:
            cevap = input(" Sesi arttırmak için '+' \n Sesi azaltmak için '-' \n Çıkmak için '*' Basınız")

            if (cevap == "+"):
                if (self.tv_ses!=31):
                    self.tv_ses+=1
                    print("Ses: ",self.tv_ses)
                else:
                    print("Ses en yüksek seviyede")

            elif (cevap == "-"):
                if (self.tv_ses!=0):
                    self.tv_ses-=1
                    print("Ses: ",self.tv_ses)
                else:
                    print("Ses en düşük seviyede")

            elif (cevap=="*"):
                break

    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi")

    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("Şuanki kanal: ",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv Durumu: {}\n Tv Ses: {}\n Kanal Listesi: {}\n Şuanki Kanal: {} ".format(self.tv_durumu,self.tv_ses,self.kanal_listesi,self.kanal)


kumanda = Kumanda()
print(""""
Televizyon Uygulaması

1. Tv Aç

2. Tv Kapat

3. Ses Açma

4. Kanal Açma

5.Kanal Sayısını Öğrenme

6.Rastgele Kanal Seçme

7.Televizyon Bilgileri

Çıkmak için 'q' Basınız


""")

while True:
    işlem = input("İşlemi Seçiniz: ")

    if (işlem=="q"):
        print("Program Sonlandırılıyor...")
        break

    elif (işlem =="1"):
        kumanda.tv_ac()

    elif (işlem=="2"):
        kumanda.tv_kapat()

    elif(işlem =="3"):
        kumanda.ses_ayarları()

    elif(işlem=="4"):
        kanal_isimleri = input ("Kanal isimlerini ',' virgül ile ayırarak giriniz:")

        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif(işlem=="5"):
        print("Kanal sayısı: ",kumanda.__len__())

    elif (işlem=="6"):
        kumanda.rastgele_kanal()
    elif (işlem=="7"):
        print("Kumanda Bilgileri\n",kumanda.__str__())

    else:
        print("İşleminiz geçersidir")
