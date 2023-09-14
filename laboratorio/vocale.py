"""Esercizio 1
Scrivi un programma in python che chieda all'utente una stringa composta da un solo carattere 
e dica se si tratta di una vocale oppure no."""

while True:
    lettera = input("inserisci una lettera : ")
    if lettera.isdigit() == True:
        print("Inserisci una lettera, riprova!")
    elif len(lettera) > 1:
        print("Inserisci solo una lettera, riprova!")
    else:
        break
    
vocali = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
trovato = False

for i in vocali:
   if i == lettera:
      trovato = True

if trovato == True:
   print(f"{lettera} è una vocale")
else:
   print(f"{lettera} non è una vocale")
