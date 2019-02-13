print("""Hadi En Büyük Sayıyı Bulalım :)
**************************************
""")

sayi1=int(input("Birinci sayıyı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz: "))
sayi3=int(input("Üçüncü sayıyı giriniz: "))

eb=sayi1

if (sayi2>eb):
    eb=sayi2

if(sayi3>eb):
    eb=sayi3

print("en büyük sayı: ",eb)

'''
DİĞER YÖNTEM
a =  int(input("a:"))

b = int(input("b:"))

c = int(input("c:"))

if (a >= b and a >= c):
    print("En büyük sayı:",a)
elif (b >= a and b >= c):
    print("En büyük sayı:",b)
elif (c >= a and c >= b):
    print("En büyük sayı:",c)
'''