# 6. Crie uma matriz 3x3 preenchida pelo usuário e exiba todos os valores na tela.

print("Digite nome do produto, seu preço, e estoque dele.")

matriz_produto = []


for i in range(3):
    nome = input("Digite nome do produto: ")
    preço = int(input("Digite preço do produto: "))
    estoque = int(input("Digite estoque: "))

    matriz_produto.append([nome, preço, estoque])

for linha in matriz_produto:
    print(linha)
    