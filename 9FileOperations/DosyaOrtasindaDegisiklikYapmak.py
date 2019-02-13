with open("dosya4.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(4,"Bebek Büyüktanır \n")
    file.seek(0)
    file.writelines(liste)

