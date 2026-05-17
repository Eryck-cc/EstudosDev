num = int(input("Digite um número para ser fatorado: "))
fat = 1

while num > 0:
    fat = fat * num
    num = num - 1
print(f"O resultado foi {fat}!")