import sys

print("Název skriptu:", sys.argv[0])  # Vždy název souboru
if len(sys.argv) > 1:
    print("Argumenty:", sys.argv[1:])
else:
    print("Nebyl zadán žádný argument.")
