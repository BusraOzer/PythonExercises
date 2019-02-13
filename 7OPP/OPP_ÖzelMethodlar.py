class Kitap():
    def __init__(self,ad,yazar,sayfa,tür):
        self.ad=ad
        self.yazar=yazar
        self.sayfa=sayfa
        self.tür=tür

    def __str__(self):
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}".format(self.ad, self.yazar, self.sayfa,self.tür)

    def __len__(self):
        return self.sayfa

kitap=Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")

print(kitap)
print(len(kitap))

