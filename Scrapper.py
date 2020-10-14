import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Conbre-MultipleXR2-V380-Ultra-Connectivity/dp/B07ZMKFXVL/ref=sr_1_1?dchild=1&keywords=camers&qid=1602653296&sr=8-1'

headers ={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()


    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[2:7].replace(",", ""))

    if(converted_price>10):
        send_mail()

    print(title.strip())
    print(converted_price)

def send_mail():
    server= smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("somushukla190301@gmail.com", "uegnwtsbwptgssmg")
    subject="Price fell down"
    body= "Check the amazon price link  https://www.amazon.in/Conbre-MultipleXR2-V380-Ultra-Connectivity/dp/B07ZMKFXVL/ref=sr_1_1?dchild=1&keywords=camers&qid=1602653296&sr=8-1"


    msg = f"Subject: {subject}\n\n {body}"

    server.sendmail('somushukla190301@gmail.com',
        'akashshukla190301@gmail.com',
        msg
    )
    print("Email has been sent")
    server.quit()


while(True):
    check_price()
    time.sleep(60*60)