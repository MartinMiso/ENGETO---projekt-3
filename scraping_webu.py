from requests import get
from bs4 import BeautifulSoup as bs

def naformatuj_odkaz(rok):
    return f"https://cs.wikipedia.org/wiki/Wikipedie:%C4%8Cl%C3%A1nek_t%C3%BDdne/{rok}"


def ziskej_parsovanou_odpoved(url):
    return bs(get(url).text, features="html.parser")


def najdi_vsechny_a_tagy(rozdelene_html, tag):
    return rozdelene_html.find_all(tag, {"class": "mw-file-description"})


def najdi_titulky(vsechny_a, atribut):
    seznam_titulku = list()

    for a_tag in vsechny_a:
        seznam_titulku.append(a_tag.attrs.get(atribut, "Chybí klíč 'title'"))

    return seznam_titulku


def projdi_vsechny_roky():
    vsechny_clanky = dict()

    for rok in range(2017, 2022):
        rozdelene = ziskej_parsovanou_odpoved(naformatuj_odkaz(rok))
        vsechny_a = najdi_vsechny_a_tagy(rozdelene, "a")
        vsechny_clanky[rok] = najdi_titulky(vsechny_a, "title")

    return vsechny_clanky

if __name__ == "__main__":
    print(projdi_vsechny_roky())