print("HESAP MAKİNESİ")
print("**************************************************")

a = int(input("Birinci sayıyı giriniz: "))
b = int(input("İkinci sayıyı giriniz : "))

print("**************************************************")

print("Toplama işlemi için:   1")
print("Çıkartma işlemi için:  2")
print("Çarpma işlemi için:    3")
print("Bölme işlemi için:     4")

islem=int(input("Yapmak istediğiniz işlem numarasını giriniz: "))

if (islem==1):
    print("Sayıların toplamı: ",a+b)
elif (islem==2):
    print("Sayıların farkı: ",a-b)
elif (islem==3):
    print("Sayıların çarpımı: ",a*b)
elif (islem==4):
    print("Sayıların bölümü: ",a/b)
else:
    print("Geçersiz İşlem!!!!")