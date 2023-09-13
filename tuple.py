parole = ("casa", "auto", "giardino", "mestolo")

parolaLunga = max(parole, key=len)
parolaPiccola = min(parole, key=len)

print(parolaLunga, parolaPiccola)

numeri = 33, 78, 5, 42, 23
partenza = -10
totale = sum(numeri, partenza)

print(totale)

languages = ['Python', 'Java', 'JavaScript']

print(list(enumerate(languages)))