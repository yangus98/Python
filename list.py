"""utente1 = ["Pino", "Demarco", 22, "Bologna", "BO"]
utente2 = ["Giovanni", "Servedio", 50, "Torino", "TO"]
utente3 = ["Michele", "Volpe", 30, "Milano", "MI"]
utente4 = ["Raji", "Mahal", 18, "Roma", "RO"]

newList = [utente1, utente2, utente3, utente4]

for i in range(len(newList)):
    print(newList[i][0:])"""

primi = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

match = int(input("Inserisci il valore da trovare: "))
trovato = False

for j in range(len(primi)):
    if primi[j] == match:
        trovato = True
        print(f"Valore trovato alla posizione {primi.index(match)}!")

if trovato == False:
    print("Valore non trovato!")

if match in primi:
    print(f"l'elemento {match} è stato trovato alla posizione {primi.index(match)}")
else:
    print(f"l'elemento {match} non è stato trovato")

