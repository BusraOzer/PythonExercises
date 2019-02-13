import requests
from bs4 import BeautifulSoup

url =  "https://www.akademikpersonel.org/anasayfa/akademik-ilanlar/" # Site linkimiz

response =  requests.get(url) # Web sayfamızı çekiyoruz.

html_icerigi = response.content  # Web sayfamızın içeriğini alıyoruz.

soup =  BeautifulSoup(html_icerigi,"html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.

for i in soup.find_all("a"):
    print(i.get("href"))
