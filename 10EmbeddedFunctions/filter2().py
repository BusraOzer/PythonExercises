from functools import reduce

def çift (sayı):
    toplam=0
    if (sayı%2==0):
        return True
    else:
        return False


liste=[1,2,3,4,5,6,7,8,9,10]
liste1=[]
liste1=list(filter(çift,liste))

print(liste1)



print(reduce(lambda x,y : x + y,liste1))


