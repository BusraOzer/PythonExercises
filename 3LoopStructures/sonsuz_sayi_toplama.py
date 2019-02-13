print(""" ******************************
Girilen Sayıların Toplamını Hesaplama

Çıkmak için "q" Basınız...

******************************
 """)
toplam = 0
sayi = input("Değer Giriniz: ")
while True:
    if (sayi=="q"):
        print("Hoşçakalın")
        break
    sayi = int(sayi)
    toplam = toplam + sayi
    sayi = input("Değer Giriniz: ")
print("Girdiğiniz sayıların toplamı:",toplam)