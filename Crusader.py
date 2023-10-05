import random

scelta = "s"
numManovre = int(input("Benvenuto, inserisci il numero di manovre preparate: "))
numIniziali = int(input("Inserisci il numero di manovre iniziali: "))
manovrePreparate = []

for x in range(numManovre):
    insManovra = input(f"Inserisci la {x+1}° manovra: ")
    manovrePreparate.append(insManovra)

print(f"Hai inserito: {manovrePreparate}")

while scelta == "s":
    copiaManovrePreparate = manovrePreparate.copy()

    manovreDisponibili = random.sample(copiaManovrePreparate, numIniziali)
    print(f"Le manovre che puoi usare sono: {manovreDisponibili}")

    copiaManovrePreparate = [elemento for elemento in copiaManovrePreparate if elemento not in manovreDisponibili]
    print(f"Ti rimangono da pescare: {copiaManovrePreparate}")

    while len(copiaManovrePreparate) > 0:
     manovraUsata = input("Inserisci la manovra da usare(scrivila esattamente come l'hai scritta prima...): ")
     while manovraUsata in manovreDisponibili:
       manovreDisponibili.remove(manovraUsata)

     indiceCasuale = random.randint(0, len(copiaManovrePreparate) - 1)
     valoreCasuale = copiaManovrePreparate[indiceCasuale]
     manovreDisponibili.append(valoreCasuale)
     print(f"Le manovre che puoi usare sono: {manovreDisponibili}")

     copiaManovrePreparate = [elemento
        for elemento in copiaManovrePreparate
        if elemento not in manovreDisponibili]
     print(f"Ti rimangono da pescare: {copiaManovrePreparate}")

    if len(copiaManovrePreparate) == 0:
      scelta = input("Vuoi continuare? (s/n): ")
