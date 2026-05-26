# 7. Crie uma matriz 3x3 com números inteiros e mostre a soma de todos os elementos
n = 3  # número de linhas
m = 3  # número de colunas
matriz = []

for i in range(n):
    linha = []
    for j in range(m):
        numero = int(input(f"Digite um número para a posição [{i}][{j}]: "))
        linha.append(numero)   # adiciona o número na linha
    matriz.append(linha)       # adiciona a linha completa na matriz

print("\nMatriz 3x3:")
for i in range(n):
    print(matriz[i])

# soma dos elementos
soma = 0
for i in range(n):
    for j in range(m):
        soma += matriz[i][j]

print(f"\nA soma de todos os elementos é: {soma}")


