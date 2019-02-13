def not_hesapla(satır):

    satır=satır[:-1] # satırlar arasında ki boşluğu ortadan kaldırıyor
    liste = satır.split(",") #herbir elemanı virgüle göre parçala ve her satırı listeye at

    #bir satır içindeki verileri parça parça değişkenlerde tuttuk
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)


    if (son_not>=90):
        harf = "AA"

    elif (son_not>=85):
        harf = "BA"

    elif (son_not>=80):
        harf = "BB"

    elif (son_not>=75):
        harf = "CB"

    elif (son_not>=70):
        harf = "CC"

    elif (son_not>=65):
        harf = "DC"

    elif (son_not>=60):
        harf = "DD"

    elif (son_not>=55):
        harf = "FD"

    else:
        harf = "FF"

    return isim +"=" + harf + "\n"




with open("sinif.txt","r",encoding="utf-8") as file:

    eklenecekler_listesi=[]
    geçenler_listesi=[]
    kalanlar_listesi=[]
    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))

    print(eklenecekler_listesi)

    for i in eklenecekler_listesi:
        i = i[:-1]
        liste = i.split("=")
        
        isim=liste[0]
        harf=liste[1]

        if (harf == "FF"):
            kalanlar_listesi.append(i)
        else:
            geçenler_listesi.append(i)


    with open ("notlar.txt","w",encoding="utf-8") as file2:
        for i in eklenecekler_listesi:
            file2.write(i)


    with open ("gecenler.txt","w",encoding="utf-8") as geçen:
        for i in geçenler_listesi:
            geçen.write(i)
            geçen.write("\n")

    with open ("kalanlar.txt","w",encoding="utf-8") as kalan:
        for i in kalanlar_listesi:
            kalan.write(i)
            kalan.write("\n")
