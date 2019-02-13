with open("mailler.txt", "r", encoding="utf-8") as file:
    liste=[]
    for satır in file:
        if (satır.find("@")!=-1):
            liste.append(satır)


    for i in liste:
        i = i[:-1]
        if(i.endswith("gmail.com")==True or i.endswith("hotmail.com")==True or i.endswith("yahoo.com")==True ):
            print(i)