import requests
import lxml
from bs4 import BeautifulSoup
import smtplib


My_email = "kunj1766@gmail.com"
Password = "abcd" 

URL = "https://www.amazon.in/Nike-Vision-Nature-Midnight-Numeric_9/dp/B0BNJMCV85/ref=sxin_25_slsr_d_i_fsnewarrivals_fa_cue_0_B0BNJMCV85?content-id=amzn1.sym.75fb7dbe-1dae-415e-a068-997b8c3956f7%3Aamzn1.sym.75fb7dbe-1dae-415e-a068-997b8c3956f7&crid=1WNW0FMVTDQT0&cv_ct_cx=Nike+shoes&keywords=Nike+shoes&pd_rd_i=B0BNJMCV85&pd_rd_r=3619b691-2964-4e8a-9a03-c83fe688405a&pd_rd_w=6wl0W&pd_rd_wg=7Cm7O&pf_rd_p=75fb7dbe-1dae-415e-a068-997b8c3956f7&pf_rd_r=R5D4B72J3699EBW9ZHBA&qid=1677925396&sprefix=nike+shoes%2Caps%2C250&sr=1-1-5b2ee5ec-0735-4782-9f3a-9d21a55133d0"

header = {
    'Accept-Language': "en-US,en;q=0.9",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" 
}



response = requests.get(url=URL, headers=header)


soap = BeautifulSoup(response.content, "lxml")
# print(soap.prettify())


price = soap.find_all(name="span", class_="a-price-whole")

BUY_Price = 2000

if(price<BUY_Price):
    with smtplib.SMTP("smtp.gmail.com") as connections:
        connections.starttls()
        connections.login(user=My_email, password=Password)
        connections.sendmail(from_addr=My_email, to_addrs="kunj.maheshwari2021@vitbhopal.ac.in", msg="Subject:Alert! Price Drop\n\n Check your shooping cart.")


