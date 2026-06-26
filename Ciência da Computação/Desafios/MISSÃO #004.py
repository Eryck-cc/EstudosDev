'''# Missão Diária 004 manhã 

## Fácil/médio 

🧪 Missão RPG: O Laboratório Proibido

Os alquimistas encontraram um líquido misterioso em um laboratório abandonado. ⚗️

Sua missão é descobrir se ele pode ser usado com segurança.

---

🎯 Objetivo

Criar um programa que:

✅ Pergunte o nome da substância X

✅ Pergunte a temperatura da substância X

✅ Exiba um resultado de acordo com a temperatura:

🧊 Menor que 0:A substância congelou!

💧 Entre 0 e 49:A substância está estável.

🔥 Entre 50 e 99:A substância está superaquecida.

💥 100 ou mais:A substância explodiu!

---

📜 Regras da Missão

⚔️ O programa deve utilizar:

✅ input()

✅ int()

✅ Variáveis

✅ if

✅ elif

✅ else

✅ f-string

❌ Não vale usar apenas um if

---

👹 Mini Boss (Opcional)

🟢 Criar um alerta especial para temperatura exatamente igual a 100

🟢 Exibir o nome da substância em todas as mensagens

🟡 Fazer o programa analisar 3 substâncias usando um for ou while

---

Boa sorte alquimistas 🧪'''

substancia = input("Me diga o nome da substância: ")
temperatura = int(input("Me diga a temperatura em número inteiro: "))

def resultado(a):
    if a < 0: 
        return f"A substância {substancia} congelou 🧊"
    elif a >= 0 and a < 50:
        return f"A substância {substancia} está estável 💧"
    elif a > 49 and a < 100:
        return f"A substância {substancia} está superaquecida 🔥"
    elif a == 100:
        return f"A substância {substancia} está incrivelll!!!"
    else:
        return f"A substância {substancia} explodiu 💥"
    
print(resultado(temperatura))

for i in range(3):
    substancia = input("Me diga o nome da substância: ")
    temperatura = int(input("Me diga a temperatura em número inteiro: "))
    print(resultado(temperatura))