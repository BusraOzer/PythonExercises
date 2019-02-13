import requests
from bs4 import BeautifulSoup

url =  "https://www.imdb.com/list/ls064079588/" # Site linkimiz

response =  requests.get(url) # Web sayfamızı çekiyoruz.

html_icerigi = response.content  # Web sayfamızın içeriğini alıyoruz.

soup =  BeautifulSoup(html_icerigi,"html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.

baslıklar = soup.find_all("h3",{"class":"lister-item-header"})
puanlar = soup.find_all("div",{"class":"ipl-rating-star small"})

for baslık,puan  in zip(baslıklar,puanlar):

    baslık=baslık.text
    puan=puan.text

    baslık=baslık.strip()
    baslık=baslık.replace("\n","")

    puan = puan.strip()
    puan = puan.replace("\n", "")

    print("Başlık:",baslık)
    print("Puan:",puan)
