print(""" ******************************
Sisteme Hoşgeldiniz
******************************
 """)

Kullanıcı_adi="bbuyuktanir"
Kullanıcı_sifre=12345
giris_kontrolü=3

while True:
    isim = input("Kullanıcı Adınızı Giriniz: ")
    şifre = int(input("Kullanıcı Şifrenizi Giriniz: "))

    if (Kullanıcı_adi!=isim and Kullanıcı_sifre==şifre):
        print("Kullanıcı Adınız Yanlış!")
        giris_kontrolü-=1

    elif (Kullanıcı_adi!=isim and Kullanıcı_sifre!=şifre):
        print("Kullanıcı Adınız ve Şifreniz Yanlış!")
        giris_kontrolü-=1

    elif (Kullanıcı_adi == isim and Kullanıcı_sifre != şifre):
        print("Kullanıcı Şifreniz Yanlış!")
        giris_kontrolü -= 1

    else:
        print("Sisteme Hoşgeldiniz")
        break

    if(giris_kontrolü==0):
        print("Sisteme Giriş Hakkınız Bitti")
        break