import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()


mesaj["From"] = "deneme.buyuktanir@gmail.com"

mesaj["To"] = "deneme.buyuktanir@gmail.com"

mesaj["Subject"] = "Smtp Mail Gönderme"


yazi = """

Bu bir SMTP Deneme Mesajıdır

"""


mesaj_govdesi = MIMEText(yazi,"plain")

mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)

    mail.ehlo()

    mail.starttls()

    mail.login("deneme.buyuktanir@gmail.com","deneme.12")

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    print("Mail Başarıyla Gönderildi....")

    mail.close()

except:
    sys.stderr.write("Bir sorun oluştu!")
    sys.stderr.flush()

