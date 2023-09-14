try:
    traduzioni = {
        "ciao": "hello",
        "arrivederci": "goodbye",
        "uova": "eggs",
        "gatto": "cat",
        "arancia": "orange",
        "birra": "beer",
    }

    trovata = False
    cerca = str(input("Inserisci la chiave da cercare: "))

    while cerca.isdigit() == True:
        cerca = input("Non puoi cercare numeri! ")

    for chiave in traduzioni.keys():
        if chiave == cerca:
            trovata = True
            valore = traduzioni[cerca]

    if trovata == True:
        print(f"chiave {cerca} trovata e il suo valore è {valore}!")
    else:
        print(f"chiave {cerca} non trovata!")

    aggiungiRis = str(input("Vuoi inserire un record?(s/n) "))

    if aggiungiRis == "s":
        insChiave = str(input("Inserisci la chiave: "))
        insValore = str(input("Inserisci il valore: "))

        while insChiave.isdigit() == True:
            insChiave = input("Inserisci una chiave che è una stringa! ")

        while insValore.isdigit() == True:
            insValore = input("Inserisci un valore che è una stringa! ")

        print(traduzioni.setdefault(insChiave, insValore))

    print(f"dizionario attuale: {traduzioni}")
except ValueError as e:
    print(f"Errore: {e}")
    print("Tipo sbagliato!")
except NameError as f:
    print(f"Errore: {f}")
    print("Tipo sbagliato pt. 2!")
finally:
    print("Fine Applicazione!")
