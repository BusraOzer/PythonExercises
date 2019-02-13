def kare_al():

    for i in range(1,6):
        yield i**2




generator=kare_al()

iterator=iter(generator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) # iterator elemanı bittiği için stopIteration hatası verdi