age = 17
license = True
residence = input("Vivi in USA o in Italia? ")

while residence != "USA" and residence != "Italia":
    residence = input("Vivi in USA o in Italia? ")
    if age >= 18 and license == True:
        print("Puoi noleggiare una Ferrari!")
    elif age >= 18 and license == False:
        print("Fatti prima la patente!")
    elif (age >= 16 and age <= 18) and residence == "USA":
        if license == False:
            print("Puoi prendere la patente in USA")
    else:
        print("Puoi noleggiare una Ferrari")
    print("Puoi noleggiare una Ferrari in USA!")
else:
    print("Ripassa tra qualche anno")
