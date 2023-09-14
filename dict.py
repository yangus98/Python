lista = [
    {'nome': 'Luiz', 'cognome': 'Miranda'},
    {'nome': 'Maria', 'cognome': 'Oliveira'},
    {'nome': 'Daniel', 'cognome': 'Silva'},
    {'nome': 'Eduardo', 'cognome': 'Moreira'},
    {'nome': 'Aline', 'cognome': 'Souza'},
]
l2 = sorted(lista, key=lambda item: item['cognome'])

numeri2 = [ x for x in range(11) if x % 2 == 0]

print(f"{l2}\n {numeri2}")

ita_eng = {"ciao": "hello", "arrivederci": "goodbye", "gatto": "cat"}

print(ita_eng.keys())
print(type(ita_eng))

for chiave in ita_eng.values():
    print(chiave)