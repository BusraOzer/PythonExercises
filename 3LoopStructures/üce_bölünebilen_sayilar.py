print(""" ******************************
1 - 100 arasındaki Sayılardan 3'e Bölünenleri Bulma

******************************
 """)
list=[]
for i in range(1,101):
    if((i%3)==0):
        list.append(i)

print(list)

'''
Diğer Yöntemi
for i in range(1,101):
    
    if (i % 3 != 0):
        continue
    print(i)
    
'''

