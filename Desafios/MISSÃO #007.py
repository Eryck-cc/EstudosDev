'''# Missão Diária 007 Manhã:

## Médio


🏰 Missão RPG: O Portal da Guilda
Os magos da guilda criaram um portal mágico capaz de transportar aventureiros para diferentes regiões do reino. ✨
Porém, o portal só pode ser ativado com a quantidade correta de energia mágica.

🎯 Objetivo
Criar um programa que:
✅ Pergunte o nome do aventureiro
✅ Pergunte a quantidade de energia mágica disponível
✅ Classifique o destino de acordo com a energia informada

🌳 Menor que 50 → Floresta Inicial

⛰️ Entre 50 e 99 → Montanhas Antigas

🏰 Entre 100 e 199 → Castelo da Guilda

🐉 200 ou mais → Covil do Dragão

✅ Exiba uma mensagem informando para onde o aventureiro foi teleportado

---

🧩 Exemplo:

Nome do aventureiro: Treloso
Energia: 120

✨ Treloso foi teleportado para o Castelo da Guilda!

---

## 📜 Regras da Missão:


⚔️ O programa deve utilizar:
✅ input()
✅ int()
✅ Variáveis
✅ if
✅ elif
✅ else
✅ f-string
❌ Não vale usar apenas um if
❌ Não vale deixar alguma faixa de energia sem classificação

---
# 👹 Mini Boss (Opcional)
🟢 Criar uma mensagem especial para energia exatamente igual a 100
🟢 Mostrar quantos pontos de energia faltam para o próximo destino
🟡 Permitir analisar 3 aventureiros usando for ou while
🟡 Criar uma área secreta para energias acima de 500

---

Boa sorte aventureiros! ✨'''
def classificacao(energia):
        if energia > 500:
             return "Área Secreta"
        elif energia >= 200:
            return "Covil do Dragão"
        elif energia > 100:
            return "Castelo da Guilda"
        elif energia == 100:
            return "Entrando no Castelo da Guilda"
        elif energia >= 50:
            return "Montanhas Antigas"
        else:
            return "Floresta Inicial"
        
def proximo_destino(energia):
    if energia < 50:
        return 50 - energia
    elif energia < 100:
        return 100 - energia
    elif energia < 200:
        return 200 - energia
    elif energia < 500:
        return 500 - energia
    else:
        return 0
        
for i in range(3):
    nome = input("Digite o seu nome de aventureiro: ")
    energia = int(input("Digite a quantidade de energia magica disponivel: "))
    print(f"Aventureiro {nome} você está no destino {classificacao(energia)} e falta {proximo_destino(energia)} pontos para seu proximo destino.")