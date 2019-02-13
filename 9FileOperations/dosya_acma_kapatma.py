dosya = open("dosya1.txt","w",encoding="utf-8")
# "w" sıfırdan dosya açma, her açılışta bilgileri sıfırlar
dosya.write("Tolga Büyüktanır \n")
dosya.close()
dosya = open("dosya1.txt","a",encoding="utf-8")
# "a" var olan dosyayı hiçbir işlem yapmadan açmak
dosya.write("Büşra Büyüktanır \n")
dosya.close()
