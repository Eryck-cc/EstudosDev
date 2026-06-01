# 1. Faça um programa que leia uma matriz 3x3 de inteiros e multiplique os elementos da diagonal principal da matriz por um número k. Imprima a matriz na tela antes

n_linhas = 3
n_colunas = 3
matriz = []
multi = 0

k = int(input("Digite um número: "))

for i in range(n_linhas):
    linhas = []
    
    for j in range(n_colunas):
        numero = int(input(f"Digite o número da posição {[i]}{[j]}: "))
        linhas.append(numero)
    matriz.append(linhas)

for linha in matriz:
    print(linha)

for n in range(len(matriz)):
    multi = k * matriz[n][n]
    print(f"{matriz[n][n]} x {k} = {multi}")

print(f"O resultado da multiplicação dos números da diagonal é {multi}.")
