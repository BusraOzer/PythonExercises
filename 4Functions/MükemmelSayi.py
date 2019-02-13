print(""" ******************************
Mükemmel Sayı Hesaplama

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
Bu işlemi Fonksiyon kullanarak yapacağız

******************************
 """)




toplam = 0

def mükemmel(sayım):
    i=1
    while (i < sayım):
        if (sayım % i == 0):
            global toplam
            toplam += i
        i+= 1
    return toplam


sayı = int(input("Sayı:"))
deger=mükemmel(sayı)
if (deger == sayı):
    print("sayı mükemmel bir sayıdır.")
else:
    print("sayı mükemmel bir sayı değildir.")