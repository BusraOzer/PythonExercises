file=open("dosya3.txt","r",encoding="utf-8")


liste=file.readlines()

print("Hoşgeldin Bebeğim :) {}".format(liste[2]),)

file.close()

# öndeden içine veri eklediğimiz okuma.txt dosyasından readlines() fonksiyonu ile okuma yaptık
#readlines() fonksiyonu dosyanın tüm satırılarını bir şeklinde döner
