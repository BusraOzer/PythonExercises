import requests
import time
from bs4 import BeautifulSoup
import sys
import urllib
def main():
    while(1):
            response = urllib.request.urlopen('https://www.doviz.com/',)
            soup = BeautifulSoup(response.read(),"html.parser")
            for i in soup.find_all("span", {"class": "menu-row1"}):
                print(i.text)
            for i in soup.find_all("span", {"class": "menu-row2"}):
                print(i.text)
            time.sleep(10)
            response.close()


if __name__ == "__main__":
    if(len(sys.argv)!=2):
        print("Usage: python3 dovizUygulamasi3.py url")
    main()
