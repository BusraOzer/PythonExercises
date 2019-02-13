import os


with open("pdf_dosyalari.txt", "w", encoding="utf-8") as file:
    for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("/home/bsr"):

        for i in dosya_isimleri:
            if(i.endswith(".pdf")):
               file.write(i)
               file.write("\n")


with open("txt_dosyalari.txt", "w", encoding="utf-8") as file2:
    for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("/home/bsr"):

        for i in dosya_isimleri:
            if(i.endswith(".txt")):
               file2.write(i)
               file2.write("\n")



with open("mp4_dosyalari.txt", "w", encoding="utf-8") as file3:
    for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("/home/bsr"):

        for i in dosya_isimleri:
            if(i.endswith(".mp4")):
               file3.write(i)
               file3.write("\n")
