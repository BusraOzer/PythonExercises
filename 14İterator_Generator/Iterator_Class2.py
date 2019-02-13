class Kare():

    def __init__(self,max=0):
        self.max=max
        self.kuvvet=0

    def __iter__(self):
        return self

    def __next__(self):
        sonuc=0
        if (self.kuvvet<=self.max):
            sonuc=self.kuvvet**2

            self.kuvvet+=1
            return sonuc
        else:
            self.kuvvet = 0
            raise StopIteration

kare=Kare(5)

for i in kare:
    print(i)