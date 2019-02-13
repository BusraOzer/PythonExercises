class Çalışan():
    def __init__(self, isim, soyisim, numara, maaş, departman):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maaş = maaş
        self.departman = departman

    def bilgileriGöster(self):
        print("""
        Yazılımcı Bilgileri
        İsim= {}
        Soyisim= {}
        Numara= {}
        Maaş= {}
        Departman= {}

        """.format(self.isim, self.soyisim, self.numara, self.maaş, self.departman))

class Yönetici(Çalışan):
    def __init__(self, isim, soyisim, numara, maaş, departman,kişiSayısı):
        super().__init__(isim,soyisim,numara, maaş, departman) #super fonk. kullanımı
        #isim,soyisim,numara, maaş, departman bilgilerini tekrar almadan Çalışan sınıfından çekiyoruz

        self.kişiSayısı=kişiSayısı

        print("Yönetici sınıfı init fonksiyonu")

    def bilgileriGöster(self):
        print("""
        Yazılımcı Bilgileri
        İsim= {}
        Soyisim= {}
        Numara= {}
        Maaş= {}
        Departman= {}
        Kişi Sayısı= {}

        """.format(self.isim, self.soyisim, self.numara, self.maaş, self.departman, self.kişiSayısı))

    """
       Çalışan sınıfındaki init ve bilgileri göster fonksiyonunu iptal edip kendi içinde kullandık.
       Tekrarlardan kurtulmak için __init__() fonksiyonu için super() fonksiyonunu kullamdık
       """
    def maasYükselt(self,zam):
        print("Maaş güncelleniyor...")
        self.maaş=self.maaş+zam


yazılımcı1 = Yönetici("Büşra", "Büyüktanır", 622303, 3500, "ArGe",0)
yazılımcı2 = Yönetici("Tolga", "Büyüktanır", 119305, 6500, "ProjeYöneticisi",15)

yazılımcı1.bilgileriGöster()
yazılımcı2.bilgileriGöster()

yazılımcı1.maasYükselt(500)
yazılımcı1.bilgileriGöster()
