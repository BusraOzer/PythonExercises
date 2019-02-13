from PIL import Image,ImageFilter

image = Image.open("kus.jpg")
#image.save("kus2.jpg") # resimi yeniden kaydetme
#image.rotate(180).save("kus3.jpg") # resmi döndürme
#image.convert(mode="L").save("kus4.jpg") #resmin rengini değiştirme

'''
# resmim boyutunu değiştirme
degiştir =(960,600)
image.thumbnail(degiştir)
image.save("kus5.jpg")
'''

#image.filter(ImageFilter.GaussianBlur(5)).save("kus6.jpg") #resmi bulanıklaştırma

'''
#resim kırpma işlemi
image2 =Image.open("atatürk.jpg")
kırpılacak_alan=(340,0,950,600)
image2.crop(kırpılacak_alan).save("yeni.jpg")
'''
