a=int(input("Birinci sayıyı giriniz: "))
b=int(input("İkinci sayıyı giriniz: "))

print("Birinci sayı: {}, İkinci sayı: {}".format(a,b))

a,b = b,a

print("Sayıların değişmiş değeri \nBirinci sayı: {}, İkinci sayı: {}".format(a,b))