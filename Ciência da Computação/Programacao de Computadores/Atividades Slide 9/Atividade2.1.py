# 2. Faça um programa que leia duas matrizes A e B 2x2 de inteiros e imprima a matriz C que é a soma das matrizes A e B.

n_linha = 2
n_coluna = 2
matriz_a = []
matriz_b = []
matriz_c = []


for i in range(n_linha):
    linhas_a = []
    linhas_b = []
    for j in range(n_coluna):
        numero_a = int(input(f"Digite o número para matriz A, posição {[i]}{[j]}: "))
        numero_b = int(input(f"Agora para a matriz B, posição {[i]}{[j]}: "))

        linhas_a.append(numero_a)
        linhas_b.append(numero_b)
    matriz_a.append(linhas_a)
    matriz_b.append(linhas_b)

for i in range(n_linha):
    linhas = []
    for j in range(n_coluna):
        soma = matriz_a[i][j] + matriz_b[i][j]

        linhas.append(soma)
    matriz_c.append(linhas)

for linhas in matriz_a:
    print(linhas)

for linhas in matriz_b:
    print(linhas)

for linhas in matriz_c:
    print(linhas)