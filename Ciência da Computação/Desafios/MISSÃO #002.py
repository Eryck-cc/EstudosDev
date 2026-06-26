'''# Missão diária 002 

🧪 Missão RPG: A Poção Misteriosa

O alquimista da guilda perdeu a fórmula de uma poção mágica! ⚗️
Agora os aventureiros precisam testar ingredientes para descobrir se a poção será um sucesso… ou um desastre 💥

---

🎯 Objetivo

Criar um programa que:

✅ Coloque alguns ingredientes na tela 
✅ Pergunte o nome de um ingrediente
✅ Pergunte a quantidade do ingrediente
✅ Se a quantidade for maior que 5:
A poção explode 💥

✅ Se for 5 ou menor:
A poção fica pronta ✨

---

🧩 Exemplo

Digite o ingrediente:
Erva Lunar

Digite a quantidade:
3

✨ A poção de Erva Lunar foi criada com sucesso!

---

👹 Mini Boss (Opcional)

O alquimista pede uma melhoria no sistema!

🟢 Criar mensagens diferentes para cada ingrediente
🟢 Criar uma “Poção Lendária” caso a quantidade seja exatamente 5
🟡 Fazer resultados secretos dependendo do ingrediente escolhido

---

📜 Regras da Missão

⚔️ O programa deve utilizar:

✅ input()
✅ if e else
✅ Variáveis
✅ print()
✅ Comparação numérica (>, <, ==)

❌ Não vale copiar código pronto da internet
❌ Não vale deixar o programa sem mensagens personalizadas (coloca essa cabecinha de programador para pensar em uma mensagem criativa)
'''

print("Esses são os ingredientes disponiveis para a poção mágica: Erva Lunar, Cristal de Fogo, Pó de Estrela, Raiz de Mandrágora, Líquido Arcano.")
ingredientes = str(input("Digite um ingrediente: "))
quantidade = int(input("Agora sua quantidade: "))

if quantidade > 5:
    print("A poção explodiu 💥")
elif quantidade == 5:
    print("Poção léndaria criada!")
elif ingredientes == "Erva Lunar" and quantidade == 3:
    print("Poção secreta criada")
else:
    if ingredientes == "Erva Lunar":
        print(f"A poção {ingredientes} ficou pronta com sucesso ✨, surgiu uma lua.")
    elif ingredientes == "Cristal de Fogo":
        print(f"A poção {ingredientes} ficou pronta com sucesso ✨, surgiu fogo.")
    elif ingredientes == "Pó de Estrela":
        print(f"A poção {ingredientes} ficou pronta com sucesso ✨, surgiu uma estrela.")
    elif ingredientes == "Raiz de Mandrágora":
        print(f"A poção {ingredientes} ficou pronta com sucesso ✨, surgiu uma mangrágora.")
    elif ingredientes == "Líquido Arcano":
        print(f"A poção {ingredientes} ficou pronta com sucesso ✨, surgiu um arcano.")