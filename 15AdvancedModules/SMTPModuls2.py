import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

file=open("mailler.txt","r",encoding="utf-8")

liste=file.readlines()

file.close()


for i in liste:
    liste2=i.split(",")

    liste2[1]=liste2[1].rstrip("\n")

    mesaj = MIMEMultipart()

    mesaj["From"] = "deneme.buyuktanir@gmail.com"

    mesaj["To"] = liste2[1]

    mesaj["Subject"] = "Smtp ile Deneme Maili Gönderme"

    yazi = "Merhaba "+liste2[0]+"\nBu Bir Python Ödevidir"


    mesaj_govdesi = MIMEText(yazi, "plain")

    mesaj.attach(mesaj_govdesi)

    try:
        mail = smtplib.SMTP("smtp.gmail.com", 587)

        mail.ehlo()

        mail.starttls()

        mail.login("deneme.buyuktanir@gmail.com", "deneme.12")

        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())

        print("Mail Başarıyla Gönderildi....")

        mail.close()

    except:
        sys.stderr.write("Bir sorun oluştu!")
        sys.stderr.flush()














