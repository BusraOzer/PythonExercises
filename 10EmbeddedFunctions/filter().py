def üçgen_mi (demet):
    kenar1=demet[0]
    kenar2 = demet[1]
    kenar3 = demet[2]

    if (kenar1+kenar2>kenar3 and kenar1+kenar3>kenar2 and kenar3+kenar2>kenar1):
        return True
    else:
        return False



liste = [(3,4,5),(6,8,10),(3,10,7)]

print(list(filter(üçgen_mi,liste)))