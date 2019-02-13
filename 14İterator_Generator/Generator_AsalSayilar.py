def asal_sayılar():
    for sayı in range(2, 1001):
        i = 2
        say = 0
        while (i < sayı):
            if (sayı % i == 0):
                say += 1
            i += 1
        if (say == 0):
            yield sayı


generator=asal_sayılar()

iterator=iter(generator)

print(next(iterator))