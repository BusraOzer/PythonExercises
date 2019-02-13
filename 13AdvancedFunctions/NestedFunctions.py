def fonksiyon(*args):  # args : (1,2,3,4,5,6)

    def topla(args):  # (1,2,3,4,5,6)
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    print(topla(args))


fonksiyon(1, 2, 3, 4, 5, 6)