'''# Missão Diária 006 manhã

## Médio

🧙 Missão RPG: O Tradutor de Runas

Os magos da guilda encontraram um pergaminho antigo escrito em runas mágicas. 📜✨

Felizmente, os estudiosos já descobriram o significado de algumas runas e armazenaram tudo em um grimório mágico.

Sua missão é criar um tradutor de runas.

---

🎯 Objetivo

Criar um programa que:

✅ Crie um dicionário contendo pelo menos 5 runas e seus significados

✅ Pergunte ao usuário qual runa deseja traduzir

✅ Mostre o significado da runa

✅ Caso a runa não exista, exiba uma mensagem de erro

---

🧩 Exemplo

Runa:
ignis

🔥 Significado: Fogo

---

📜 Regras da Missão

⚔️ O programa deve utilizar:

✅ Dicionário ("dict")

✅ Chaves e valores

✅ "input()"

✅ "if"

✅ Operador "in"

✅ f-string

❌ Não vale usar vários "if" para cada runa

❌ Não vale armazenar os significados em listas

---

👹 Mini Boss (Opcional)

🟢 Mostrar todas as runas disponíveis antes da consulta

🟢 Permitir traduzir mais de uma runa usando "while"

🟡 Mostrar quantas runas existem no grimório

🟡 Permitir adicionar uma nova runa ao dicionário

---

Boa sorte estudiosos das runas! 📜✨'''

dicionario = {"Ignis": "Fogo",
        "Algiz": "Proteção",
        "Raidho": "Jornada",
        "Kenaz": "Tocha",
        "Laguz": "Água"}

while True:
    print("Digite [1] para perguntar o significado de uma runa e [2] para adicionar uma runa e seu significado ao grimorio e [3] para sair!")
    escolha = int(input("Digite: "))

    if escolha == 1:
        for i in range(1):
            print(f"A quantidade de runas é {len(dicionario)}")
        print("As runas disponiveis são:")
        for n in dicionario:
            print(n)
        runa = input("Digite o nome da runa que você deseja saber o significado (Escreva de forma correta): ")

        if runa in dicionario:
            print(f"O significado de {runa} é {dicionario[runa]}")
    
    elif escolha == 2:
        nome = input("Digite o nome da runa: ")
        significado = input("Seu significado: ")
        dicionario.update({nome: significado})

    elif escolha == 3:
        print("...finalizando")
        break
    else:
        print("Número incorreto tente novamente")