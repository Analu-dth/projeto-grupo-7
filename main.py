import os
import dados
from treinos import menu_treinos
from exercicios import menu_exercicios
from competicoes import menu_competicoes

dados.carregar_dados()

while True:
    os.system("cls")
    print("========== HYROOX PLANNER ==========")
    print("1 - CRUD de Treinos")
    print("2 - Exercícios e Controle de Desempenho")
    print("3 - Planejamento de Competições")
    print("0 - Sair")
    print()
    try:
        desejo = int(input("Selecione a opção desejada: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um NÚMERO.")
        input("Pressione Enter para continuar...")
        continue

    if desejo == 0:
        os.system("cls")
        print("Saindo...")
        break
    elif desejo == 1:
        menu_treinos()
    elif desejo == 2:
        menu_exercicios()
    elif desejo == 3:
        menu_competicoes()
    else:
        print("Opção inválida. Por favor, digite um NÚMERO.")
        input("Pressione Enter para continuar...")