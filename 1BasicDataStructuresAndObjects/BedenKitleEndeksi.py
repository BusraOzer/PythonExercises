boy=float(input("Boyunuzu griniz: "))
kilo=int(input("Kilonuzu giriniz: "))

print("GİRİLEN BOY: {} GİRİLEN KİLO {}  ".format(boy,kilo))

bke=kilo / (boy ** 2)

print("Beden Kitle İndeksi:",bke)

if(bke<18.5):
    print("Zayıfsınız")

elif (18.5<bke < 25):
      print("Normal Kilodasınız")

elif (25<bke < 30):
      print("Fazla Kilolusunuz")

elif (30<bke ):
      print("OBEZ!!!!")