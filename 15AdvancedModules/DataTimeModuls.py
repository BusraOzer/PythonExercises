from datetime import datetime
import locale

şu_an = datetime.now() #şuanki zamanı alma
print("Tarih:", şu_an)
print("Yıl: ",şu_an.year)
print("Ay: ",şu_an.month)
print("Gün: ",şu_an.day)
print("Saat: ",şu_an.hour)
print("Dakika: ",şu_an.minute)
print("Saniye: ",şu_an.second)
print("Salise: ",şu_an.microsecond)
print("---------------------------")
print(datetime.ctime(şu_an)) # Tarihi süslü gösterme
print("---------------------------")
print(datetime.strftime(şu_an,"%Y" " %B")) # '%' ifadesiyle yıl ay vs gösterme

'''timestamp() ve fromtimestamp()
Şu anki zamanı saniye cinsinden bulmak için, datetime objemizi (şu_an objesi) timestamp() fonksiyonumuza gönderebiliriz. 
Aynı zamanda saniye cinsinden verilmiş bir zamanı da fromtimestamp fonksiyonuyla datetime objesine çevirebiliriz.'''

print("---------------------------")
tarih=datetime(2023,10,29)  #Belli iki tarih arasındaki farkı bulmak
fark=tarih-şu_an
print(fark)
print("Gün: ",fark.days)
print("Saniye: ",fark.seconds)


