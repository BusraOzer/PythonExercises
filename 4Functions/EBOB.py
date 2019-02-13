
def ebob(a,b):

   if (a>b):
       sayac=a
   else:
       sayac=b

   while (sayac>0):

       if (a % sayac == 0 and b % sayac == 0):
           print("Sayının ebob: ",sayac)
           break
       sayac=sayac-1
       if(sayac==1):
           print("Bu sayılar aralarında asaldır")

while True:
        deger = input("çıkmak için 'q' basınız. Devam etmek için 'enter' basınız")
        if(deger=="q"):
            print("Hoşçakalın")
            break
        sayı1 = int(input("Birinci sayıyı giriniz: "))
        sayı2 = int(input("İkinci sayıyı giriniz: "))

        if((sayı1==0) or (sayı2 ==0)):
            print("Sayının ebob: 0")

        elif(sayı1==1):
            print("Sayının ebob: ",sayı2)

        elif(sayı2==1):
            print("Sayının ebob: ",sayı1)

        else:
            ebob(sayı1,sayı2)
