"""Esercizio 7
Inserire 20 numeri random da 10 a 100 con un ciclo for. 
Dopo controllare con un altro ciclo quanti valori maggiori di 50 sono stati inseriti."""

import random

numeriRandom = []
counter = 0

for num in range(20):
    numeriRandom.append(random.randint(10,100))

for rand in numeriRandom:
    if rand > 50:
        counter += 1

print(f"Ci sono {counter} elementi maggiori di 50!")
print(numeriRandom)