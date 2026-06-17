# 3. Faça um programa que leia as dimensões de duas matrizes A e B, e depois leia as duas matrizes (os elementos devem ser inteiros). Se as matrizes forem de tamanhos compatíveis para multiplicação, multiplique as matrizes. Imprima as matrizes A, B e a matriz resultante da multiplicação.
matriz_a = []
matriz_b = []

nlinhas_a = int(input("Digite o número de linhas da matriz A: "))
ncolunas_a = int(input("Agora o número de colunas: "))

nlinhas_b = int(input("Digite o número de linhas da matriz B: "))
ncolunas_b = int(input("Agora o número de colunas: "))

for i in range(nlinhas_a):
    linhas_a = []
    for j in range(ncolunas_a):
        numero_a = int(input(f"Digite o número da posição {[i]}{[j]} da matriz A: "))
        linhas_a.append(numero_a)
    matriz_a.append(linhas_a)

for i in range(nlinhas_b):
    linhas_b = []
    for j in range(ncolunas_b):
        numero_b = int(input(f"Digite o número da posição {[i]}{[j]} da matriz B: "))
        linhas_b.append(numero_b)
    matriz_b.append(linhas_b)

print("Matriz A:")
for linhas in matriz_a:
    print(linhas)

print("Matriz B:")
for linhas in matriz_b:
    print(linhas)

if  ncolunas_a == nlinhas_b:

    matriz_c = []
    multi = 0

    for i in range(nlinhas_a):
        linhas_c = []
        for j in range(ncolunas_b):
            
            for k in range(ncolunas_a):
                multi = matriz_a[i][k] * matriz_b[k][j]
            linhas_c.append(multi)
        matriz_c.append(linhas_c)

    print("A matriz C é:")
    for linhas in matriz_c:
        print(linhas)