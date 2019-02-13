import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tablo_oluştur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")
    con.commit()
def deger_ekle():
    cursor.execute("INSERT INTO kitaplık VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',261)")
    con.commit()

#Kullanıcıdan Veri Alma
def kullanıcı_deger_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()

isim = input("İsim:")
yazar = input("Yazar:")
yayınevi = input("Yayınevi:")
sayfa_sayısı =  int(input("Sayfa Sayısı:"))


kullanıcı_deger_ekle(isim,yazar,yayınevi,sayfa_sayısı)


# deger_ekle() mevcut bilgiyi tabloya ekler



con.close()