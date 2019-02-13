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

class Yönetici(Çalışan): #Çalışan sınıfı özellik ve fonksiyonlarını kullanıyor
    def maasYükselt(self,zam):
        print("Maaş güncelleniyor...")
        self.maaş=self.maaş+zam


yazılımcı1 = Yönetici("Büşra", "Büyüktanır", 622303, 3500, "ArGe")
yazılımcı2 = Yönetici("Tolga", "Büyüktanır", 119305, 6500, "ArGe")

yazılımcı1.bilgileriGöster()
yazılımcı2.bilgileriGöster()

yazılımcı1.maasYükselt(500)
yazılımcı1.bilgileriGöster()
