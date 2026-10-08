matriz = [
[5, 8, 3],
[2, 7, 9],
[4, 6, 1],
]

# soma todos os elementos

for linha in matriz:
   for numero in linha:
      print(numero)



# apenas numeros pares 


for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
              print(numero)


#apenas os numeros maiores que cinto
    
for linha in matriz:
    for numero in linha:
        if numero > 5:
            print(numero)
