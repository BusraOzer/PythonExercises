#local değişkenler sdc fonksiyınlar ve classlar içinde tanımlanan değişkenlerdir


a=3 #global değişken
b=5 #global değişken

def fonk1 ():
    a = 2 #local değişken, yapılan işlem sadece fonksiyon içinde geçerli olur
    print(a)

def fonk2 ():
    global b #local değişkni global yapıyoruz, yapılan işlemler kalıcı olur
    b = 12
    print(b)

fonk1()
print("****************************")
print(a)
print("****************************")
fonk2()
print("****************************")
print(b)
