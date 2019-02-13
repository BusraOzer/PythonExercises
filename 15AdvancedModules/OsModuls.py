import os

print(os.getcwd()) # bulunduğumuz dizinin yolunu söyler
print("-------------------------------")

print(os.listdir()) #bulunduğumuz dizinde klasörleri ve dosyaları listeler
print("-------------------------------")

'''                                                                     
os.mkdir("Deneme1") #"klasör" oluşturmamızı sağlar
os.makedirs("Deneme2/Deneme3/Deneme4") #iç içe klasör oluşturmamızı sağlar'''

'''                                                                     
os.rmdir("Deneme1") # klasör silmemizi sağlar
os.removedirs("Deneme2/Deneme3") #iç içe klasörleri silmemizi sağlar'''

#içine bir tane dizin (veya klasör) verdiğimizde bunun altındaki tüm dizinleri , dosyaları sıralar ve alt dizinlere gidilecek bir yer kalmayana kadar gider
for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("/home/bsr/Desktop"):

    print("Şu anki dizin", klasör_yolu)
    print("Klasörler ", klasör_isimleri)
    print("Dosyalar", dosya_isimleri)
    print("**********************************")

for klasör_yolu, klasör_isimleri, dosya_isimleri in os.walk("/home/bsr/Desktop"):
    for i in dosya_isimleri:
        if(i.endswith(".py")):
           print(i)