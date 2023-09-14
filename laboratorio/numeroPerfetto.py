"""Esercizio 3
Scrivi un programma in python che verifichi se un numero è perfetto oppure no.
Un numero perfetto è un numero naturale uguale alla somma dei suoi divisori positivi, escluso sé stesso."""

div = 2
somma = 1

while True:
        try:
            richiesta = int(input("inserisci l'elemento da verificare: "))
            if richiesta>= 0:
               break
            else:
               print("il numero deve essere positivo!")
        except ValueError:
            print("Inserisci un numero, riprova!")

while div <= richiesta / 2:
   if richiesta % div == 0:
      somma = somma + div
   div = div + 1
else:
   if somma == richiesta:
      print(f"{richiesta} è un numero perfetto")
   else:
      print(f"{richiesta} non è un numero perfetto")
