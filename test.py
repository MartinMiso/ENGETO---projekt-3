import requests
from bs4 import BeautifulSoup
import csv
import argparse

print("Ahoj")

with open ("soubor.txt", "w", encoding="UTF-8") as testovaci_soubor:
    testovaci_soubor.write("Zapiš text a uvidíme")
    print("Soubor vytvořen")

with open ("soubor.txt", "r", encoding="UTF-8") as cteni_souboru:
   obsah = cteni_souboru.read()
   print(obsah)

print("Máme vypsanej obsah")

# txt_soubor = open("soubor.txt", "r", encoding="UTF-8")
# obsah = txt_soubor.read()
# print(obsah)
# txt_soubor.close()