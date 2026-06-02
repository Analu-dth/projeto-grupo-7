import os
import dados
from dados import salvar_dados

OPCOES_EXERCICIOS = [
    "sled push",
    "sled pull",
    "burpee broad jumps",
    "wall balls",
    "farmer's carry",
]


def menu_exercicios():
    while True:
        os.system("cls")
        print("===== EXERCÍCIOS E CONTROLE DE DESEMPENHO =====")
        print("1 - Adicionar exercício")
        print("2 - Visualizar exercícios")
        print("3 - Editar exercício")
        print("4 - Excluir exercício")
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
            adicionar_exercicio()
        elif escolha == 2:
            visualizar_exercicios()
        elif escolha == 3:
            editar_exercicio()
        elif escolha == 4:
            excluir_exercicio()
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")


def adicionar_exercicio():
    os.system("cls")
    print("=================================================")
    for idx, nome in enumerate(OPCOES_EXERCICIOS, start=1):
        print(f"{idx}- {nome}")
    print("=================================================")

    try:
        numero_escolhido = int(input("Digite o n° do exercício: "))
        if 1 <= numero_escolhido <= len(OPCOES_EXERCICIOS):
            exercicio_nome = OPCOES_EXERCICIOS[numero_escolhido - 1]
        else:
            print("\nOpção inválida! Escolha um número de 1 a 5.")
            input("Pressione Enter e tente novamente...")
            return
    except ValueError:
        print("\nEntrada inválida! Por favor, digite um NÚMERO.")
        input("Pressione Enter e tente novamente...")
        return

    tempo     = input("Digite o tempo: ")
    distancia = input("Digite a distância: ")
    carga     = input("Digite a carga: ")
    repeticao = input("Digite as repetições: ")

    # Entradas vazias para manter alinhamento com treinos
    dados.treinos.append("")
    dados.horarios.append("")
    dados.duracoes.append("")
    dados.intensidades.append("")

    dados.exercicios.append(exercicio_nome)
    dados.tempos.append(tempo)
    dados.distancias.append(distancia)
    dados.cargas.append(carga)
    dados.repeticoes.append(repeticao)

    salvar_dados()
    print("\n✓ Exercício adicionado!")
    input("Pressione Enter para continuar...")


def visualizar_exercicios():
    os.system("cls")
    print("========== EXERCÍCIOS CADASTRADOS ==========\n")

    if not any(e for e in dados.exercicios if e):
        print("Nenhum exercício cadastrado.")
    else:
        col1, col2, col3, col4, col5 = 22, 12, 12, 12, 12
        sep = (
            f"+{'-'*col1}+{'-'*col2}+{'-'*col3}+"
            f"{'-'*col4}+{'-'*col5}+"
        )
        print(sep)
        print(
            f"| {'Exercício':<{col1-2}} "
            f"| {'Tempo':<{col2-2}} "
            f"| {'Distância':<{col3-2}} "
            f"| {'Carga':<{col4-2}} "
            f"| {'Reps':<{col5-2}} |"
        )
        print(sep)
        for i in range(len(dados.exercicios)):
            if dados.exercicios[i]:
                print(
                    f"| {dados.exercicios[i]:<{col1-2}} "
                    f"| {dados.tempos[i]:<{col2-2}} "
                    f"| {dados.distancias[i]:<{col3-2}} "
                    f"| {dados.cargas[i]:<{col4-2}} "
                    f"| {dados.repeticoes[i]:<{col5-2}} |"
                )
        print(sep)

    input("\nPressione Enter para continuar...")


def editar_exercicio():
    while True:
        os.system("cls")
        exercicios_validos = [i for i, e in enumerate(dados.exercicios) if e]

        if not exercicios_validos:
            print("Nenhum exercício cadastrado.")
            input("Pressione Enter...")
            return

        print("========== EDITAR EXERCÍCIOS ==========\n")
        for idx, i in enumerate(exercicios_validos):
            print(f"{idx + 1} - {dados.exercicios[i]}")

        try:
            selecao = int(input("\nEscolha o exercício: ")) - 1
            if 0 <= selecao < len(exercicios_validos):
                n = exercicios_validos[selecao]
                dados.exercicios[n]  = input(f"Novo exercício ({dados.exercicios[n]}): ")  or dados.exercicios[n]
                dados.tempos[n]      = input(f"Novo tempo ({dados.tempos[n]}): ")           or dados.tempos[n]
                dados.distancias[n]  = input(f"Nova distância ({dados.distancias[n]}): ")  or dados.distancias[n]
                dados.cargas[n]      = input(f"Nova carga ({dados.cargas[n]}): ")           or dados.cargas[n]
                dados.repeticoes[n]  = input(f"Novas repetições ({dados.repeticoes[n]}): ") or dados.repeticoes[n]
                salvar_dados()
                print("\n✓ Exercício editado!")
                input("Pressione Enter para continuar...")
                break
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um NÚMERO.")

        input("Pressione Enter para continuar...")


def excluir_exercicio():
    os.system("cls")
    exercicios_validos = [i for i, e in enumerate(dados.exercicios) if e]

    if not exercicios_validos:
        print("Nenhum exercício cadastrado.")
        input("Pressione Enter...")
        return

    print("========== EXCLUIR EXERCÍCIOS ==========\n")
    for idx, i in enumerate(exercicios_validos):
        print(f"{idx + 1} - {dados.exercicios[i]}")

    try:
        selecao = int(input("\nEscolha o exercício: ")) - 1
        if 0 <= selecao < len(exercicios_validos):
            n = exercicios_validos[selecao]
            dados.exercicios[n] = ""
            dados.tempos[n]     = ""
            dados.distancias[n] = ""
            dados.cargas[n]     = ""
            dados.repeticoes[n] = ""
            salvar_dados()
            print("\n✓ Exercício excluído!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um NÚMERO.")

    input("Pressione Enter para continuar...")