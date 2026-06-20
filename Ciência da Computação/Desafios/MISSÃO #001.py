'''# MISSÃO DE MANHÃ DIÁRIA!!! 001
## MISSÃO NIVEL FÁCIL/ MÉDIA:
🐍 Missão RPG: Lista da Taverna
A taverna da guilda está ficando sem organização! 🍖🍞
O dono precisa de aventureiros programadores para criar um sistema simples de pedidos.
🎯 Objetivo
Criar um programa em Python que:
✅ Adicione comidas em uma lista
✅ Mostre todas as comidas cadastradas
✅ Permita sair do programa
---
⚔️ O programa deve ter um menu parecido com isso:
[1] Adicionar comida
[2] Ver comidas
[3] Sair
---
🧩 Exemplo
Digite uma comida:
Pizza
Pizza adicionada à taverna!
MINI BOSS 💀
🟢 Não permitir nome vazio
🟢 Mostrar quantas comidas existem na lista
🟡 Não permitir comidas repetidas'''

comidas = []
while True:
    
    try:

        print("[1] Adicionar comida\n[2] Ver comidas\n[3] Sair")

        selecionado = int(input("Selecione oque você deseja fazer: "))

        if selecionado == 1:
            adicionar = input("Digite a comida que você deseja adicionar: ")

            if adicionar == "":
                print("Você digitou um campo vazio!")
            
            elif adicionar in comidas:
                print("Já existe essa comida na taverna, tente novamente!")

            else:
                comidas.append(adicionar)
                print(f"{adicionar} adicionado a taverna!")

        elif selecionado == 2:
            print(f"As comidas da taverna são: {comidas}.")

        elif selecionado == 3:
            break
    
        else:
            print("Opção incorreta selecione outra.")

        print(f"Existem {len(comidas)} comidas na taverna!")
        
    except ValueError:
        print("O que você selecionou não é um número, tente novamente.")
        continue