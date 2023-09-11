print("-----SCEGLI:-----")
scelta = int(
    input(
        f"1.PARLA CON CPU\n2.QUADRATO DI UN NUMERO\nPREMI QUALSIASI ALTRO TASTO PER USCIRE... "
    )
)
while scelta <= 2:
    match scelta:
        case 1:
            cpuName = "Windows"
            cpuAge = 50

            print(f"-----------------\nCiao sono {cpuName} e ho {cpuAge} anni.")

            userName = input("Invece tu sei? ")
            while userName.isdigit():
                userName = input("Inserisci una stringa! ")
            userName = userName.capitalize()

            userAge = input("...e quanti anni hai? ")
            while userAge.isdigit() == False:
                userAge = input("Inserisci un numero! ")
            else:
                while int(userAge) > 100:
                    userAge = input("Inserisci un numero fino a 100! ")

            ageDifference = int(cpuAge) - int(userAge)
            print(f"Fammi capire, quindi sei {userName} e hai {userAge} anni.")
            print(
                f"Lo sai che abbiamo ben {ageDifference} anni di differenza!?!"
            )

            print("-----SCEGLI:-----")
            scelta = int(
                input(
                    f"1.PARLA CON CPU\n2.QUADRATO DI UN NUMERO\nPREMI QUALSIASI ALTRO TASTO PER USCIRE... "
                )
            )
        case 2:
            quadrato = int(input("Inserisci un numero "))
            print(
                f"Il quadrato di {quadrato} è {quadrato * quadrato}!"
            )
            
            print("-----SCEGLI:-----")
            scelta = int(
                input(
                    f"1.PARLA CON CPU\n2.QUADRATO DI UN NUMERO\nPREMI QUALSIASI ALTRO TASTO PER USCIRE... "
                )
            )
else:
    print("Arrivederci!")
