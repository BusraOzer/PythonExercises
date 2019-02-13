with open("futbolcular.txt","r",encoding="utf-") as file:
    liste = file.readlines()
    gs_listesi=[]
    fb_listesi=[]
    bjk_listesi=[]
    for i in liste:
        i = i[:-1]
        liste2 = i.split(",")
        takım=liste2[1]

        if (takım =="Galatasaray"):
            gs_listesi.append(i)
        elif (takım =="Fenerbahçe"):
            fb_listesi.append(i)
        elif(takım =="Beşiktaş"):
            bjk_listesi.append(i)

with open("fb.txt","w",encoding="utf-") as fb:
    for i in fb_listesi:
        fb.write(i)
        fb.write("\n")

with open("gs.txt","w",encoding="utf-") as gs:
    for i in gs_listesi:
        gs.write(i)
        gs.write("\n")

with open("bjk.txt","w",encoding="utf-") as bjk:
    for i in bjk_listesi:
        bjk.write(i)
        bjk.write("\n")