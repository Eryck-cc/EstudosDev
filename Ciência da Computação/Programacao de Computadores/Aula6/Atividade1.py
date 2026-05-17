nota = float(input("Digite uma nota: "))

while 0 <= nota >= 10:
    print("Valor fora do intervalo de 0 a 10, digite novamente!")
    nota = float(input("Digite uma nota: "))
print("Nota dentro do intervalo!")