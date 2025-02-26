import sys

soucet = [int(cislo ) for cislo in sys.argv[1:]]
pocet = len(sys.argv[1:])

print(f"Průměrná hodnota je {sum(soucet) / pocet}")
input("Dej enter pro ukončení...")