import random

while True:
    try:
        scelta = "s"
        numManovre = int(input("Benvenuto, inserisci il numero di manovre preparate: "))
        numIniziali = int(input("Inserisci il numero di manovre iniziali: "))

        while numIniziali > numManovre:
            print("Il numero di manovre iniziali non può essere maggiore del numero di manovre preparate!")
            numManovre = int(input("Inserisci il numero di manovre preparate: "))
            numIniziali = int(input("Inserisci il numero di manovre iniziali: "))
          
        manovrePreparate = []

        for x in range(numManovre):
            insManovra = input(f"Inserisci la {x+1}° manovra: ")

            while insManovra.isdigit():
                insManovra = input(f"Non puoi inserire numeri, reinserisci la {x+1}° manovra: ")

            manovrePreparate.append(insManovra)

        while scelta == "s":
            copiaManovrePreparate = manovrePreparate.copy()

            manovreDisponibili = random.sample(copiaManovrePreparate, numIniziali)
            print(f"Le manovre che puoi usare sono: {manovreDisponibili}")

            copiaManovrePreparate = [elemento for elemento in copiaManovrePreparate if elemento not in manovreDisponibili]

            while len(copiaManovrePreparate) > 0:
                adaptive = input("RESET: Vuoi usare il talento Adaptive Style?(s/n) ")
                while adaptive.isdigit() or adaptive.lower() not in ['s', 'n']:
                    adaptive = input("Inserisci (s/n): ")

                if adaptive == "s":
                    copiaManovrePreparate = []
                    numManovre = int(input("Inserisci il numero di manovre preparate: "))
                    numIniziali = int(input("Inserisci il numero di manovre iniziali: "))

                    while numIniziali > numManovre:
                     print("Il numero di manovre iniziali non può essere maggiore del numero di manovre preparate!")
                     numManovre = int(input("Inserisci il numero di manovre preparate: "))
                     numIniziali = int(input("Inserisci il numero di manovre iniziali: "))

                    manovrePreparate = []

                    for x in range(numManovre):
                     insManovra = input(f"Inserisci la {x+1}° manovra: ")

                     while insManovra.isdigit():
                      insManovra = input(f"Non puoi inserire numeri, reinserisci la {x+1}° manovra: ")

                     manovrePreparate.append(insManovra)

                    break
                
                manovraUsata = input("Inserisci la manovra da usare (scrivila esattamente come l'hai scritta prima...): ")

                while manovraUsata.isdigit():
                    manovraUsata = input("Non puoi inserire numeri, reinserisci il nome della manovra: ")

                while manovraUsata in manovreDisponibili:
                    manovreDisponibili.remove(manovraUsata)

                indiceCasuale = random.randint(0, len(copiaManovrePreparate) - 1)
                valoreCasuale = copiaManovrePreparate[indiceCasuale]
                manovreDisponibili.append(valoreCasuale)
                print(f"Le manovre che puoi usare sono: {manovreDisponibili}")

                copiaManovrePreparate = [elemento for elemento in copiaManovrePreparate if elemento not in manovreDisponibili]

            if len(copiaManovrePreparate) == 0:
                print("Hai finito le manovre da pescare e/o le stai resettando.")
                scelta = input("Vuoi continuare? (s/n): ")

                while scelta.isdigit() or scelta.lower() not in ['s', 'n']:
                    scelta = input("Inserisci 's' per continuare o 'n' per terminare: ")

    except ValueError:
        print("Inserisci un numero intero.")
