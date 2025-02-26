import sys

print("Název skriptu:", sys.argv[0])

def formatuj_jmeno(jmeno):
    print(f"Uživatel {jmeno} spouští program")


if len(sys.argv) != 2:
    print(
        "Pro spuštění chybí argument 'jmeno',",
        "Zapiš: python povinny_argument.py 'jmeno'", sep="\n"
    )
else:
    formatuj_jmeno(sys.argv[1])