#encontar variaveis

matriz = [
[7,8,9],
[5,6,7],
[8,9,10]
]

#soma de todos os valores 

# for linha in matriz:
#    for numero in linha:
#       print(numero)

# media dos valores

soma = 0 
quantidade = 0 
for linha in matriz:
    for numero in linha:
        soma += numero
        quantidade += 1

media = soma / quantidade
print("media dos valores:", media)






# #maior valor 
# maior = matriz[0][0]
# for linha in matriz:
#    for numero in linha:
#       if numero > maior:
#             maior = numero
# print("maior:", maior)



#menor valor



menor = matriz[0][0]
for linha in matriz:
   for numero in linha:
      if numero < menor:
            menor = numero
print("menor numero:", menor)