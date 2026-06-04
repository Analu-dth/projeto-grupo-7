import os
import dados
from dados import salvar_dados


def menu_treinos():
    while True:
        os.system("cls")
        print("========== CRUD DE TREINOS ==========")
        print("1 - Adicionar treino")
        print("2 - Visualizar treinos")
        print("3 - Editar treino")
        print("4 - Excluir treino")
        print("0 - Voltar")
        print()
        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um NÚMERO.")
            input("Pressione Enter...")
            continue

        if escolha == 0:
            break
        elif escolha == 1:
            adicionar_treino()
        elif escolha == 2:
            visualizar_treinos()
        elif escolha == 3:
            editar_treino()
        elif escolha == 4:
            excluir_treino()
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")


def adicionar_treino():
        os.system("cls")

        treino     = input("Digite o nome do treino: ")
        duracao    = input("Digite a duração (Minutos): ")
        horario    = input("Digite o horário: ")
        intensidade = input("Digite a intensidade: ")

        dados.treinos.append(treino)
        dados.duracoes.append(duracao)
        dados.horarios.append(horario)
        dados.intensidades.append(intensidade)

        # Entradas vazias para manter alinhamento com exercícios
        dados.exercicios.append("")
        dados.tempos.append("")
        dados.distancias.append("")
        dados.cargas.append("")
        dados.repeticoes.append("")

        salvar_dados()
        print("\n✓ Treino adicionado com sucesso!")
        input("Pressione Enter para continuar...")


def visualizar_treinos():
    os.system("cls")
    print("========== TREINOS CADASTRADOS ==========\n")

    if not any(t for t in dados.treinos if t):
        print("Nenhum treino cadastrado.")
    else:
        col1, col2, col3, col4 = 20, 12, 12, 15
        sep = f"+{'-'*col1}+{'-'*col2}+{'-'*col3}+{'-'*col4}+"

        print(sep)
        print(
            f"| {'Treino':<{col1-2}} "
            f"| {'Horário':<{col2-2}} "
            f"| {'Duração':<{col3-2}} "
            f"| {'Intensidade':<{col4-2}} |"
        )
        print(sep)

        for i in range(len(dados.treinos)):
            if dados.treinos[i]:
                print(
                    f"| {dados.treinos[i]:<{col1-2}} "
                    f"| {dados.horarios[i]:<{col2-2}} "
                    f"| {dados.duracoes[i]:<{col3-2}} "
                    f"| {dados.intensidades[i]:<{col4-2}} |"
                )
        print(sep)

    input("\nPressione Enter para continuar...")


def editar_treino():
    while True:
        os.system("cls")
        treinos_validos = [i for i, t in enumerate(dados.treinos) if t]

        if not treinos_validos:
            print("Nenhum treino cadastrado.")
            input("Pressione Enter...")
            return

        print("========== EDITAR TREINOS ==========\n")
        for idx, i in enumerate(treinos_validos):
            print(f"{idx + 1} - {dados.treinos[i]}")

        try:
            selecao = int(input("\nEscolha o treino: ")) - 1
            if 0 <= selecao < len(treinos_validos):
                n = treinos_validos[selecao]
                dados.treinos[n]      = input(f"Novo nome ({dados.treinos[n]}): ")      or dados.treinos[n]
                dados.duracoes[n]     = input(f"Nova duração ({dados.duracoes[n]}): ")  or dados.duracoes[n]
                dados.horarios[n]     = input(f"Novo horário ({dados.horarios[n]}): ")  or dados.horarios[n]
                dados.intensidades[n] = input(f"Nova intensidade ({dados.intensidades[n]}): ") or dados.intensidades[n]
                salvar_dados()
                print("\n✓ Treino editado!")
                input("Pressione Enter para concluir...")
                break
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um NÚMERO.")

        input("Pressione Enter para continuar...")


def excluir_treino():
    while True:
        os.system("cls")
        treinos_validos = [i for i, t in enumerate(dados.treinos) if t]

        if not treinos_validos:
            print("Nenhum treino cadastrado.")
            input("Pressione Enter...")
            return

        print("========== EXCLUIR TREINOS ==========\n")
        for idx, i in enumerate(treinos_validos):
            print(f"{idx + 1} - {dados.treinos[i]}")

        try:
            selecao = int(input("\nEscolha o treino: ")) - 1
            if 0 <= selecao < len(treinos_validos):
                n = treinos_validos[selecao]
                dados.treinos[n]      = ""
                dados.horarios[n]     = ""
                dados.duracoes[n]     = ""
                dados.intensidades[n] = ""
                salvar_dados()
                print("\n✓ Treino excluído!")
                input("Pressione Enter para continuar...")
                break
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um NÚMERO.")

        input("Pressione Enter para continuar...")