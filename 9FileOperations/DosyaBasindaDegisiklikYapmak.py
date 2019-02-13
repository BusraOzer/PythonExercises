with open("dosya2.txt","r+",encoding="utf-8") as dosya:

    içerik = dosya.read()
    içerik = "Bekir Berk Büyüktanır \n" + içerik
    dosya.seek(0)
    dosya.write(içerik)
    print(dosya.read())
