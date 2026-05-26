#1. Crie um programa que receba uma palavra e mostre quantas vogais existem nela.

palavra = input("Digite uma palavra e o sistema irá dizer quantas vogais tem: ")
quantidadevo = 0
quantidadecon = 0
vogais = ("a", "e", "i", "o", "u")

for letra in palavra:
    if letra in vogais:
        quantidade = quantidadevo + 1
    else:
        quantidadecon = quantidadecon + 1
print(f"Essa palavra tem {quantidade} vogais!")
print(f"Essa palavra tem {quantidadecon} consoantes!")