matriz = [
[5, 8, 3],
[2, 7, 9],
[4, 6, 1],
]

#apenas os numeros maiores que 5


for linha in matriz:
    for numero in linha:
        if numero > 5:
            print(numero)
