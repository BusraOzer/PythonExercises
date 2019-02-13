def fonksiyon(işlem_adı):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def çarpma(*args):
        çarpım = 1
        for i in args:
            çarpım *= i
        return çarpım

    if işlem_adı == "toplama":
        return toplama
    elif işlem_adı == "çarpma":
        return çarpma
    else:
        return print("İşlem Geçersiz....")


print("İşlemler : toplama ve çarpma ")
işlem=input("Yapmak istediğiniz işlemi giriniz: ")

fonksiyon2 = fonksiyon(işlem) # çağırdığımız fonksiyon return olarak fonksiyon geri döndürdüğü için fanksiyon2 değişkeni fonksiyon olur

print(fonksiyon2(3,5))
