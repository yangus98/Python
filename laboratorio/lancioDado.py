"""Lancio del Dado
Progettate un software dove l' utente sceglie un numero da 1 a 6, tramite la funzione random simulate 
il lancio di un dato e stampare a video se l' utente ha vinto o meno."""

import random

primoDado = random.randint(1,6)
secondoDado = random.randint(1,6)
primoDadoCPU = random.randint(1,6)
secondoDadoCPU = random.randint(1,6)

print(f"I tuoi risultati sono {primoDado} + {secondoDado}")
print(f"I risultati dell'avversario sono {primoDadoCPU} + {secondoDadoCPU}")

somma = primoDado+secondoDado
sommaCPU = primoDadoCPU+secondoDadoCPU
if somma > sommaCPU:
    print(f"Hai vinto con un punteggio di {somma} a {sommaCPU}")
elif somma == sommaCPU:
    print(f"Pareggio!")
else:
    print(f"Hai perso con un punteggio di {sommaCPU} a {somma}")


