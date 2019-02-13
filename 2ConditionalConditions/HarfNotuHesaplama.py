
kontrol1 =1
while(kontrol1 ==1):
  vize1=int(input("1.vize notunu giriniz: "))
  if(vize1<0):
      print("Lütfen geçerli bir değer giriniz!!!")
      kontrol1=1

  else:
      kontrol1=0


kontrol2 =1
while(kontrol2 ==1):
  vize2=int(input("2.vize notunu giriniz: "))
  if(vize2<0):
      print("Lütfen geçerli bir değer giriniz!!!")
      kontrol2=1

  else:
      kontrol2=0

kontrol3 =1
while(kontrol3 ==1):
  final=int(input("final notunu giriniz: "))
  if(final<0):
      print("Lütfen geçerli bir değer giriniz!!!")
      kontrol3=1

  else:
      kontrol3=0
print("************************************************")
print("vize1: {}, vize2: {}, final: {}".format(vize1,vize2,final))

ortalama = (vize1*0.3)+(vize2*0.3)+(final*0.4)

print("ortalama notunuz: ",ortalama)
print("************************************************")

if(ortalama >=90):
    harf="AA"
elif(ortalama>=85):
    harf="BA"
elif(ortalama>=80):
    harf="BB"
elif(ortalama>=75):
    harf="CB"
elif(ortalama>=70):
    harf="CC"
elif(ortalama>=65):
    harf="DC"
elif(ortalama>=60):
    harf="DD"
elif(ortalama>=55):
    harf="FD"
else:
    harf="FF"

print("harf notunuz: ",harf)
