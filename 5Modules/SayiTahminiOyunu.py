import time #time modülünü programımıza dahil ettik
import random #random modülünü programımıza dahil ettik
print("""****************************

Sayı Tahmin Oyununa Hoşgeldiniz

1 ile 40 arasında(1 ve 40 dahil) rastgele tahmin edin.
****************************""")
tahmin_hakkı = 7 #oyuncunun 7 defa tahmin hakkı olsun
rastgele_sayı = random.randint(1,40) # random modülündeki randint fonksiypnu ile 1-40 arasında sayı üretiyor

while True:
    tahmin =  int(input("Tahmininiz:"))

    if (tahmin == rastgele_sayı):
        print("Sayı Sorgulanıyor....")
        time.sleep(1) # time modülündeki sleep fonksiyonu ile programımız 1 sn bekliyor
        print("Tebrikler!")
        print("Sayı",rastgele_sayı)
        break
    elif(tahmin < rastgele_sayı):
        print("Sayı Sorgulanıyor....")
        time.sleep(1)
        tahmin_hakkı -= 1
        print("Lütfen daha yüksek bir sayı söyleyin.")
        print("Tahmin Hakkı:",tahmin_hakkı)
    else:
        print("Sayı Sorgulanıyor....")
        time.sleep(1)
        tahmin_hakkı -= 1
        print("Lütfen daha düşük bir sayı söyleyin.")
        print("Tahmin Hakkı:",tahmin_hakkı)
    if (tahmin_hakkı == 0 ):
        print("Tahmin Hakkınız Bitti. Üzgünüz")
        print("Sayımız:",rastgele_sayı)
        break



