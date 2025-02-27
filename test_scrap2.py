import pandas as pd
import csv
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
url_city = (f"https://www.volby.cz/pls/ps2017nss/{odkaz_mesto}")
print(url_city)
response_city = requests.get(url_city)
soup_city = bs(response_city.text, "html.parser")

# Krok 4: Najdi výsledky v detailní stránce
# Příklad: předpokládáme, že výsledky jsou v tabulce, najdeme tabulku a vytáhneme z ní data
#table = soup_mesto.find_all(name="table", attrs={"class": "table"})
upravena_data = []
for table in soup_city.find_all("table"):
#if table:
    # Iterace přes řádky tabulky
    rows_city = table.find_all("tr")
    for row in rows_city:
        cells = row.find_all("td")
        # Zde podle struktury tabulky vyber správné sloupce
        data = [cell.get_text(strip=True) for cell in cells]
        if data and len(data) >= 2 and data[0]:
            print(data[:2])
            upravena_data.append(data[:2])
            #print(upravena_data)
        else:
            pass
# Vytvoříme DataFrame a zadáme názvy sloupců
df = pd.DataFrame(upravena_data, columns=["Číslo", "Obec"])
print(df)

# Data můžeme také uložit do CSV:
df.to_csv("data_3.csv", index=False, encoding="UTF-8")
# print(upravena_data)
# with open("data_3.csv", "a", newline="", encoding="UTF-8") as data_csv:
#     writer = csv.writer(data_csv).writerow(data)





