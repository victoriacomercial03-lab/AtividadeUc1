matriz = []
for  i in range(3):
    linha = []

    for j in range(3):
        numero = int(input("digite um numero: "))
        linha.append(numero)



        matriz.append(linha)



 # sugestao de organização 
for linha in matriz:
    print(linha)



#como somar as matrizes:
soma = 0 
quantidade = 0
for linha in matriz:
    for numero in linha:
        soma += numero

        print("soma:", soma)


# encontrando numeros pares (entendi)

for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            print(numero)


# encontrando numeros pares 02
for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            quantidade += 1

print("quantidade de pares:", quantidade)


# maior valor da matriz

maior = matriz [0][0]

for linha in matriz:
    for numero in linha:
        if numero > maior:
            maior = numero

print("maior:", maior)


#Soma de uma linha

soma = 0 
for numero in matriz[0]:
    soma += numero 

    print("soma da primeira:", soma)

# Soma de coluna

soma = 0 
for i in range(len(matriz)):
    soma += matriz[i][0]

print("soma da primeira coluna:" , soma)


