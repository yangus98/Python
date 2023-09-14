"""Progettate un algoritmo che scriva tutte le coppie di numeri che danno per prodotto 60."""
coppie = []

while True:
        try:
            numero = int(input("Inserisci il numero per le coppie: "))
            if numero > 0:
               break
            else:
               print("il numero deve essere maggiore di 0!")
        except ValueError:
            print("Inserisci un numero, riprova!")

for i in range(1, numero + 1):
    if numero % i == 0:
        coppie.append((f"|{i} x {numero // i}|"))
print(coppie)
    


