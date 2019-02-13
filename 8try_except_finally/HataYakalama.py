print("""
Bir sayının çift olup olmadığını sorgulayan bir fonksiyon var 
Bu fonksiyon, eğer sayı çift ise return ile bu değeri döndürüyor.
 Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatıyor. 
 Daha sonra, içinde çift ve tek sayılar bulunduran bir liste var.
 Bu işllemleri liste üzerinde gezinerek yapıyor ve ekrana sadece çift sayıları bastırıyor.

""")

def çift_mi(sayı):
    if (sayı % 2 == 0):
        return sayı
    else:
        raise ValueError


liste = [34, 2, 1, 3, 33, 100, 61, 1800]

for i in liste:
    try:
        print(çift_mi(i))
    except ValueError:
        pass # pass deyimi bir blokun hiçbir şey yapmadığı anlamına geliyor. Python'ın hata vermemesi için kullanabilirsiniz.