'''# Missão Diária 008 tarde

## Médio

⚔️ Missão RPG: Duelo da Guilda
Os aventureiros da guilda estão participando de um torneio para descobrir quem é o maior guerreiro do reino! 🏆
Em cada duelo, o desafiante e o Mestre da Arena escolhem uma técnica de combate.
As técnicas são:
🗡️ Espada

🛡️ Escudo

🏹 Arco

---

🎯 Objetivo
Criar um programa que:
✅ Permita ao jogador escolher uma técnica

✅ Faça o Mestre da Arena escolher uma técnica aleatoriamente

✅ Compare as escolhas

✅ Informe se o jogador venceu, perdeu ou empatou

---

# 🧩 Regras do Duelo:

🗡️ Espada vence 🏹 Arco

🏹 Arco vence 🛡️ Escudo

🛡️ Escudo vence 🗡️ Espada

Escolhas iguais resultam em empate

---

# 📜 Regras da Missão

⚔️ O programa deve utilizar:
✅ input()
✅ if, elif e else
✅ Variáveis
✅ Comparações
✅ Biblioteca random
✅ Lista
✅ f-string
❌ Não vale escolher a jogada do Mestre da Arena manualmente
❌ Não vale deixar de tratar empates

# 👹 Mini Boss (Opcional

🟢 Exibir uma contagem regressiva antes do resultado
🟢 Criar mensagens personalizadas para cada vitória e derrota
🟡 Implementar um sistema de melhor de 3
🟡 Mostrar quantas vitórias, derrotas e empates ocorreram

---

 # ☠️ Ultra Boss (Opcional)

🔴 Criar um ranking onde cada vitória concede 10 pontos ao jogador

🔴 Salvar a pontuação total durante várias partidas

⚫ Criar títulos de acordo com a pontuação:
🥉 Aprendiz da Arena
🥈 Guerreiro da Guilda
🥇 Campeão do Reino
👑 Lenda da Arena

---

Boa sorte guerreiros! ⚔️🏹'''
from time import sleep
import random

tecnicas = ["Espada", "Escudo", "Arco"]

guerreiro = input("Escolha uma tecnica entre Espada, Escudo ou Arco: ")

escolha_mestre = random.choice(tecnicas)


for i in range(10, -1, -1):
    print(i)
    sleep(1)

if guerreiro == "Espada" and escolha_mestre == "Arco":
    print("Guerreiro Venceu!")
elif escolha_mestre == "Espada" and guerreiro == "Arco":
    print("Mestre Venceu!")
elif guerreiro == "Arco" and escolha_mestre == "Escudo":
    print("Guerreiro Venceu!")
elif escolha_mestre == "Arco" and guerreiro == "Escudo":
    print("Mestre Venceu!")
elif guerreiro == "Escudo" and escolha_mestre == "Espada":
    print("Guerreiro Venceu")
elif escolha_mestre == "Escudo" and guerreiro == "Espada":
    print("Mestre Venceu")
elif guerreiro == escolha_mestre:
    print("Empate")





