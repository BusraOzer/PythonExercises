class Yazılımcı ():
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.maaş=maaş
        self.diller=diller

    def bilgileriGöster(self):
        print("""
        Yazılımcı Bilgileri
        İsim= {}
        Soyisim= {}
        Numara= {}
        Maaş= {}
        BildiğiDiller= {}
        
        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))

    def dilEkle(self,yenidil):
            print("Dil ekleniyor.....")
            self.diller.append(yenidil)

    def maasYükselt(self,zam):
            print("Maaş güncelleniyor...")
            self.maaş=self.maaş+zam


yazılımcı1= Yazılımcı("Büşra","Büyüktanır",622303,3500,["Python","C"])
yazılımcı2= Yazılımcı("Tolga","Büyüktanır",119305,6500,["Python","Java"])

yazılımcı1.bilgileriGöster()
yazılımcı2.bilgileriGöster()

yazılımcı1.maasYükselt(500)
yazılımcı1.bilgileriGöster()

yazılımcı2.dilEkle(["Apache Spark/HDFS/Pig/Hadoop","Docker"])
yazılımcı2.bilgileriGöster()