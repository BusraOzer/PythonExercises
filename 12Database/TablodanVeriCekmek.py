import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()

def verileri_al_1():
    cursor.execute("Select * From kitaplık") # Bütün bilgileri alıyoruz.
    liste = cursor.fetchall() # Veritabanından bilgileri çekmek için fetchall() kullanıyoruz.
    #listede veriler liste içinde demet şeklinde tutuluyor
    print("Kitaplık Tablosunun bilgileri.....")
    for i in liste:
        print(i)
    # con.commit() işlemine gerek yok. Çünkü tabloda herhangi bir güncelleme yapmıyoruz.

def verileri_al_2():
    cursor.execute("Select İsim,Yazar From kitaplık") # Sadece İsim ve Yazar özelliklerini alıyoruz.
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)

def verileri_al_3(yayınevi):
    cursor.execute("Select * From kitaplık where Yayınevi = ?",(yayınevi,)) # Sadece yayınevi ,Everest olan kitapları alıyoruz.
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)


verileri_al_1()
print("\n\n\n")
verileri_al_2()
print("\n\n\n")
verileri_al_3("Everest")
con.close()