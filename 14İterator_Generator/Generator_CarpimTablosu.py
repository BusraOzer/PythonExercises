def carpım_tablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield  "{} x {} = {}".format(i,j,i*j)



for i in carpım_tablosu():
    print(i)
#carpım_tablosu fonksiyonu iterable olduğu için döngü içinde kullanabiliyoruz
#hata almadan çalışır 