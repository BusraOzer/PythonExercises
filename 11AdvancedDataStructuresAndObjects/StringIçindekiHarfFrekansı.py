

string="ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

sözlük=dict()
for i in string:

    if (i in sözlük):
        sözlük[i]+=1

    else:
        sözlük[i]=1


for i,j in sözlük.items():
    print("{} = {}".format(i,j))

