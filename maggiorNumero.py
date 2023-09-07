# for numero in range(2, 6, 2):
#     print(numero)

# range(inizio, fine, quanto incrementa ogni volta)

print("---Calcolo del numero maggiore---")
volteNum = int(input("Inserisci quanti numeri vuoi confrontare "))

listaNum = []

for counter in range(0, volteNum):
    num = int(input("Inserisci il numero: "))
    # nomeArray.insert(posizione, valore)
    listaNum.insert(counter, num)

print(f"Hai inserito i seguenti numeri: {listaNum}")
print(f"Il numero più grande è {max(listaNum)}")

# con else if
numberA = input("Inserisci primo numero")
numberB = input("Inserisci secondo numero")
numberC = input("Inserisci terzo numero")

if numberA > numberB and numberA > numberC:
    print(f"{numberA} è il piu grande")
elif numberB > numberA and numberB > numberC:
    print(f"{numberB} è il piu grande")
else:
    print(f"{numberC} è il piu grande") 