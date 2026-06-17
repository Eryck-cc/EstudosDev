# 4. Faç•a um programa que leia uma matriz 3x3 de inteiros e retorne a linha de maior soma. Imprima na tela a matriz, a linha de maior soma e a soma.
matriz = []
nlinhas = 3
ncolunas = 3

for i in range(nlinhas):
    linhas = []
    for j in range(ncolunas):
        numero = int(input(f"Digite o numero da posição {[i]}{[j]}"))
        linhas.append(numero)
    matriz.append(linhas)


print("Matriz")
for linhas in matriz:
    print(matriz)

linhamaior = matriz[0]

maiorsoma = sum(matriz[0])

for linha in matriz:
    soma = sum(linha)

    if soma > maiorsoma:
        maiorsoma = soma
        linhamaior = linha

print("Linha de maior soma:")
print(linhamaior)

print(f"Soma da linha: {maiorsoma}")