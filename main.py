import os
import dados
from menus.treinos import menu_treinos
from menus.exercicios import menu_exercicios
from menus.competicoes import menu_competicoes
from menus.evolucoes import mostrar_evolucao
from menus.sugestoes import menu_sugestoes
from menus.extra import menu_extra

dados.carregar_dados()

while True:
    os.system("cls")
    print("========== HYROOX PLANNER ==========")
    print("1 - CRUD de Treinos")
    print("2 - Exercícios e Controle de Desempenho")
    print("3 - Planejamento de Competições")
    print("4 - Acompanhamento de Evolução")
    print("5 - Sugestões de Treinamento")
    print("6- Função Extra")
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
    elif desejo == 4:
        mostrar_evolucao()
    elif desejo == 5:
        menu_sugestoes()
    elif desejo == 6:
        menu_extra()
    else:
        print("Opção inválida. Por favor, digite um número das Opções Disponiveis.")
        input("Pressione Enter para continuar...")
    