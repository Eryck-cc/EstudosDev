# 3. Faça um programa que verifique se uma palavra é um palíndromo (ex.: “arara”)

palavra = input("Digite uma palvra: ")

palavra_inversa = palavra [::-1]

if palavra == palavra_inversa:
    print("É palíndromo")
else:
    print("Não é palíndromo")