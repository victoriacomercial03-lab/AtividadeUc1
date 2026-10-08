assentos = [
[0, 1, 0, 0],
[1, 1, 0, 0],
[0, 0, 0, 1]

]

livres = 0
ocupados = 0

for fila in assentos:
    for assento in fila:
        if assento == 0:
            livres += 1
        elif assento == 1:
            ocupados += 1
            