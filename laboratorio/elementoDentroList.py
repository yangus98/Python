"""Esercizio 2
Scrivi un programma in python che a partire da un elemento e una lista di elementi dica in output 
se l'elemento passato sia presente o meno nella lista.
Qualora l'elemento sia presente nella lista, il programma dovrà comunicarci l'indice 
dell'elemento tramite il metodo index."""

negozio = ["maglia", "pantalone", "calzini", "scarpe", "cappello"]
trovato = False

while True:
    ricerca = input("inserisci l'elemento da ricercare: ")
    if ricerca.isdigit() == True:
        print("Inserisci una stringa, riprova!")
    else:
        break

for i in negozio:
    if i == ricerca:
        trovato = True
        posizione = negozio.index(ricerca)
        
if trovato == True:
    print(f"Elemento {ricerca} trovato alla posizione {posizione}")
else:
    print("elemento non trovato!")

    