# fonksiyon kullanarak girilen 2 sayı için dört işlem yapma


def toplama (a,b):
    return (a+b)

def çıkartma (a,b):
    return (a-b)

def çarpma (a,b):
    return(a*b)

def bölme (a,b):
    return(a/b)

a = int(input("Birinci sayıyı giriniz: "))
b = int(input("İkinci sayıyı giriniz : "))

print("**************************************************")

print("Toplama işlemi için:   1")
print("Çıkartma işlemi için:  2")
print("Çarpma işlemi için:    3")
print("Bölme işlemi için:     4")

islem=int(input("Yapmak istediğiniz işlem numarasını giriniz: "))

if (islem==1):
    print("Sayıların toplamı: ",toplama(a,b))
elif (islem==2):
    print("Sayıların farkı: ",çıkartma(a,b))
elif (islem==3):
    print("Sayıların çarpımı: ",çarpma(a,b))
elif (islem==4):
    print("Sayıların bölümü: ",bölme(a,b))
else:
    print("Geçersiz İşlem!!!!")