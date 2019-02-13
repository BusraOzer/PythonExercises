
with open("dosya5.txt","r",encoding="utf-8") as file:
    file.seek(5)
    içerik = file.read(10)
    print(içerik)
    print(file.tell())

    file.seek(0)
    içerik2 = file.read(6)
    print(içerik2)
    print(file.tell())

