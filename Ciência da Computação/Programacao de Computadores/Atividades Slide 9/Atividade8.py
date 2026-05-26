# 8. Leia uma matriz 4x4 e informe qual é o maior número armazenado nela
n = 4 #numero de linhas
m = 4 #numero de colunas
matriz = []

for i in range(n):
    linha = []
    for j in range(m):
        numero = int(input(f"Digite um número para a posição [{i}][{j}]: "))
        linha.append(numero)
    matriz.append(linha)


print("A matriz em formato 4x4")

for i in range(n):
    print(matriz[i])

maximo = 0

for i in range(n):
    if i > maximo:
        maximo = i
print(f"O maior numero é {maximo}")