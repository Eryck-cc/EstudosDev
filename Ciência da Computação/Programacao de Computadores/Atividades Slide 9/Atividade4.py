# Receba uma frase e substitua todas as ocorrências de uma palavra específica por outra.

frase = input("Digite uma frase: ")
palavra = input(f"Sua frase é ({frase}) digite qual palavra você quer substituir por outra: ")
palavra_substituta = input("Agora qual palavra você quer colocar no lugar: ")

for palavra in frase:
    frase.replace(palavra, palavra_substituta)
print(frase)