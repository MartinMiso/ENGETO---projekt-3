import requests
from bs4 import BeautifulSoup as bs

#mesto = input("Zadej město: ").capitalize()
mesto = "Jeseník"
# Krok 1: Načti hlavní stránku s výsledky voleb
url = "https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
response = requests.get(url)
soup_hlavni = bs(response.text, "html.parser")


# Projdeme všechny <td> elementy a zjistíme, zda jejich text přesně odpovídá zadanému městu.
for td in soup_hlavni.find_all("td"):
    if td.get_text(strip=True) == mesto:
        # Najdeme rodičovský řádek, ve kterém se objevuje daná obec
        row = td.find_parent("tr")
        tds = row.find_all("td")
        # Předpokládáme, že první <td> obsahuje jméno a druhé odkaz
        if len(tds) > 1:
            link_td = tds[3]  # druhé <td>
            a_tag = link_td.find("a")
            if a_tag:
                odkaz_mesto = a_tag.get("href")
                print(f"Nalezený odkaz pro {mesto}: {odkaz_mesto}")

# Výsledná url pro dané město
url_mesto = (f"https://www.volby.cz/pls/ps2017nss/{odkaz_mesto}")
print(url_mesto)
response = requests.get(url_mesto)
soup_mesto = bs(response.text, "html.parser")

# Krok 4: Najdi výsledky v detailní stránce
# Příklad: předpokládáme, že výsledky jsou v tabulce, najdeme tabulku a vytáhneme z ní data
table = soup_mesto.find(name="table", attrs={"class": "table"})
if table:
    # Iterace přes řádky tabulky
    rows = table.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        # Zde podle struktury tabulky vyber správné sloupce
        data = [cell.get_text(strip=True) for cell in cells]
        print(data)
else:
    print("Tabulka s výsledky nebyla nalezena.")

