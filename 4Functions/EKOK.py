def ekok(a,b):
     sayac=1
     while (sayac<=(a*b)):
         if (sayac % a == 0 and sayac % b == 0):
             print("Sayının ekok: ", sayac)
             break
         sayac+=1



while True:
        deger = input("çıkmak için 'q' basınız. Devam etmek için 'enter' basınız")
        if(deger=="q"):
            print("Hoşçakalın")
            break
        sayı1 = int(input("Birinci sayıyı giriniz: "))
        sayı2 = int(input("İkinci sayıyı giriniz: "))

        ekok(sayı1, sayı2)