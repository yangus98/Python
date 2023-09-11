def sceltaUtente():
    global scelta

    print("\n*BENVENUTO*")
    scelta = int(input("Scegli l'area da calcolare:\n1. Cerchio\n2. Quadrato\n3. Rettangolo\n4. Triangolo\nPREMI QUALSIASI ALTRO TASTO PER USCIRE... "))

def areaCerchio(raggio):
    print(f"*L'area del cerchio è {raggio**2 * 3.14}*")

def areaQuadrato(lato):
    print(f"*L'area del quadrato è {lato*lato}*")

def areaRettangolo(base, altezza):
    print(f"*L'area del rettangolo è {base*altezza}*")

def areaTriangolo(base, altezza):
    print(f"*L'area del triangolo è {base*altezza/2}*")

sceltaUtente()

while scelta <= 4:
    try:
     match scelta:
        case 1:
            raggio = float(input("Inserisci il raggio "))

            areaCerchio(raggio)
            sceltaUtente()
        case 2:
            lato = float(input("Inserisci il lato "))

            areaQuadrato(lato)
            sceltaUtente()
        case 3:
            base = float(input("Inserisci la base "))
            altezza = float(input("Inserisci l'altezza "))

            areaRettangolo(base, altezza)
            sceltaUtente()
        case 4:
            base = float(input("Inserisci la base "))
            altezza = float(input("Inserisci l'altezza "))

            areaTriangolo(base, altezza)
            sceltaUtente()
    except:
        print("Non hai inserito un numero, riprova! ")
else:
    print("Arrivederci!")
