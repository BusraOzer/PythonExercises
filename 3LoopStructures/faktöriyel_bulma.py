print(""" ******************************
Faktöriyel Hesaplama

Çıkmak için "q" Basınız...

******************************
 """)
while True:
    girilen_deger = input("Sayıyı Giriniz, Çıkmak için 'q' Basınız: ")
    if (girilen_deger=="q"):
        print("Hoşçakalın")
        break
    girilen_deger = int(girilen_deger)
    faktoriyel=1

    for i in range(2, girilen_deger+1):
        faktoriyel*=i

    print("Faktoriyel: ",faktoriyel)
