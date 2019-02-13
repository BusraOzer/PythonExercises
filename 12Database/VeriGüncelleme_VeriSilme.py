import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()

def verileri_al():
    cursor.execute("Select * From kitaplık")
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)

def verigüncelle(yeni_yayınevi,eski_yayınevi):
    cursor.execute("Update kitaplık set Yayınevi = ? where Yayınevi =  ?",(yeni_yayınevi,eski_yayınevi))
    con.commit()


def verilerisil(yazar):
    cursor.execute("Delete  From kitaplık where Yazar = ?",(yazar,))
    con.commit()


while(True):
    print('''
    Çıkmak içim "q" basınız
    1)  yayınevi güncelleme işlemi 
    2)  yazara göre silme
    
    ''')
    giris= input("seçiminizi yapınız: ")

    if (giris=="q"):
        print("Hoşçakalın :)")
        break

    if (giris=="1"):
        eski=input("Eski yayın evini giriniz: ")
        yeni = input("Yeni yayın evini giriniz: ")
        verigüncelle(yeni,eski)
        verileri_al()

    if (giris=="2"):
        yazar=input("silmel istediğiniz yazar ismini giriniz: ")
        verilerisil(yazar)
        verileri_al()
con.close()