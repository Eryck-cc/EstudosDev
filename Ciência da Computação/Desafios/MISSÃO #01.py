'''🎯 Objetivo:
Criar um programa que:

peça a quantidade de ouro
peça a quantidade de aventureiros
calcule quanto cada um receberá

⚔️ Regras:
✅ usar função
✅ usar return
✅ usar try/except
✅ usar if
✅ usar divisão

💀 Mini Boss:
Se a quantidade de aventureiros for 0, mostrar:
“Não é possível dividir ouro para ninguém”

👑 Ultra Mini Boss:
Criar uma função:
def dividir_ouro(ouro, aventureiros)'''

try:
    ouro = int(input("Digite a quantidade de ouro: "))
    aventureiros = int(input("Digite a quantidade de aventureiros: "))

    if aventureiros <= 0:
        print("Não é possível dividir ouro para ninguém")
    else:
        def dividir_ouro(a, b):
            return a / b
        
    print(f"A quantidade de ouro dividida será {dividir_ouro(ouro, aventureiros)} para cada um!")
except:
    print("Você digitou algo errado, tente novamente")
