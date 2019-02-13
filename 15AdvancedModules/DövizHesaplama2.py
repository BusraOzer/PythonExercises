import requests
import time
from bs4 import BeautifulSoup

url =  "https://www.doviz.com/" # Site linkimiz

response =  requests.get(url) # Web sayfamızı çekiyoruz.
html_icerigi = response.content  # Web sayfamızın içeriğini alıyoruz.
soup =  BeautifulSoup(html_icerigi,"html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.

liste=[]
liste2=[]
liste3=[]

for i in soup.find_all("span",{"class":"menu-row1"}):
    liste.append(i.text)

for i in soup.find_all("span",{"class":"menu-row2"}):
    liste2.append(i.text)

for i in soup.find_all("span",{"class":"menu-row3"}):
    liste3.append(i.text)

dosya = open("doviz.csv","w",encoding="utf-8")
'''
CSV (Virgülle Ayrılan Değerler) dosyası, Excel'de oluşturabileceğiniz veya düzenleyebileceğiniz özel bir dosya türüdür.
Metin ve sayılar bir CSV dosyası olarak kaydedildiğinde, bir programdan diğerine kolayca taşınabilir. 
Örneğin, kişilerinizi CSV dosyasında Google'dan dışarı aktarıp sonra Outlook'a aktarabilirsiniz.

'''
dosya.write("TUR,DEGER,ORAN\n")

u = len(liste)
j=0
while j < 5:
 i=0
 while i < u:
    liste2[i]=liste2[i].replace(",",".")
    liste3[i] = liste3[i].replace(",", ".")

    print(liste[i]+"= "+liste2[i]+"  "+liste3[i])
    dosya.write(liste[i]+","+liste2[i]+","+liste3[i]+"\n")
    i+=1

 dosya.write("\n")
 time.sleep(10)
 j+=1