import requests
from bs4 import BeautifulSoup as bs

bi_url = "https://markets.businessinsider.com/commodities/gold-price"
dol_url = "https://www.kurzy.cz/kurzy-men/aktualni/czk-usd/"
pocasi_url = "https://www.chmi.cz/predpovedi/predpovedi-pocasi/ceska-republika/tydenni-predpoved"
#
# def ziskej_cenu_zlata(url: str):
#     odpoved_serveru = requests.get(url)
#     rozdeleny_text = bs(odpoved_serveru.content, features="html.parser")
#     cena_zlata = rozdeleny_text.find(name="span", attrs={"class": "price-section__current-value"}).get_text()
#     return cena_zlata
#
# def kurz_dolaru(url: str):
#     server_dolar = requests.get(url)
#     rozdeleny_text_dolar = bs(server_dolar.content, features="html.parser")
#     kurz_dolar = rozdeleny_text_dolar.find(name="span", attrs={"class": "clrred"}).get_text()
#     return kurz_dolar
#
# cena = ziskej_cenu_zlata(bi_url)
# print(f"Cena zlata: {cena} USD/oz")
#
# dolar = kurz_dolaru(dol_url)
# print(f"Kurz dolaru: {dolar} 1 USD/Kč")
#
# def cena_gram_zlata(zlato, kurz):
#     return round((float(zlato)/31.103*float(kurz)), 0)
#
# print(f"Cena zlata: {cena_gram_zlata(cena, dolar)} Kč/1g")

def pocasi(url: str):
    server_pocasi = requests.get(url)
    rozdeleny_text_pocasi = bs(server_pocasi.content, features="html.parser")
    predpoved_pocasi = rozdeleny_text_pocasi.get_text()
    return predpoved_pocasi

print(pocasi(pocasi_url))
