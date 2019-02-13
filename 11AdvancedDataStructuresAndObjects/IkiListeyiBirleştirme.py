isim=["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisim=["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

yeni=[]
veri=""

for i in isim:
    sayac = 1
    for j in soyisim:
        if(sayac==1):
            veri=i+ " " + j
            yeni.append(veri)
            sayac+=1
            soyisim.pop(0)
        else:
            break
yeni.sort()

for i in yeni:
    print(i)


"""
YADA 
isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

liste = list(zip(isim,soyisim)) #iki listeyi birleştiriyor demet veri tipinde tutuyor

liste.sort()

for i,j in liste:
    print(i,j)
"""