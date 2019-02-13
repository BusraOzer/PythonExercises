#1-100 arasında Pisagor Üçgenini Bulma
def pisagor():
    for x in range(1,100):

         for y in range(1,100):

              for z in range(1,100):

                    if ((z** 2) == (x** 2) + (y**2)) and (x < y):
                        print("Üçgen kenaları: {} {} Hipotenüs {}".format(x,y,z))



print("1-100 arasındaki pisagor üçgenlerini bulalım")
pisagor()
