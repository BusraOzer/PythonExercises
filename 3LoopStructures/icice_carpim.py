print(""" ******************************
İç İçe Çarpım Tablosu
******************************
 """)


kontrol=1
i=1
j=1
çarpım=1
while (kontrol<11):
    for j in range(1,11):
        çarpım=i*j
        print("{} * {} = {}".format(i,j,çarpım))
    print("*********************************")
    j+=1
    i+=1
    kontrol+=1
''' 
Diğer yöntem
for i in range(1,11):
    print("*************************************************")
    for j in range(1,11):
        
        print("{} x {} = {}".format(i,j,i*j))

'''