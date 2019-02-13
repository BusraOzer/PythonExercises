#liste = [i * 3 for i in range(5)] ist comprehension
generator = (i * 3 for i in range(5)) #Böyle bir list comprehension’ı generator objesine çevirmek için [] yerine () kullanıyoruz

iterator=iter(generator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
