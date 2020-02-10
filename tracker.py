import requests
import smtplib
import time
from bs4 import BeautifulSoup
def check_price(URL,precio):
    headers = {"User-Agent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}

    page = requests.get(URL, headers = headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')   
    title = soup2.find(id="productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    price = price[0:price.find(',')]
    converted_price = float(price)
    if converted_price < precio :
        send_mail(title,URL)

def send_mail(title,URL):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    email = 'dgarciacosio@gmail.com'
    server.login(email,'jvngwpfcxykvsrug')
    subject = "Ha bajado el precio " 
    body = "Mira Amazon " + URL
    msg = f'Subject:{subject}\n\n{body}'
    server.sendmail(
        email,
        email,
        msg
    )
    print("CORREO ENVIADO!")
    server.quit()
while(True):
    check_price("https://www.amazon.es/gp/product/B01MSHO3NB/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1",30)
    time.sleep(60*60*24)