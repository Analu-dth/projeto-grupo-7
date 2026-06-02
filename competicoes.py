import os
from datetime import datetime, date
import dados
from dados import salvar_dados


def menu_competicoes():
    while True:
        os.system("cls")
        print("===== PAINEL DE COMPETIÇÕES =====")
        print("1 - Cadastrar Competição")
        print("2 - Visualizar Competições")
        print("3 - Editar Competição")
        print("4 - Excluir Competição")
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
            cadastrar_competicao()
        elif escolha == 2:
            visualizar_competicoes()
        elif escolha == 3:
            editar_competicao()
        elif escolha == 4:
            excluir_competicao()
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")


def cadastrar_competicao():
    os.system("cls")

    competicao = input("Informe o nome da Competição: ")

    while True:
        data_str = input("Informe a Data desta Competição (DD/MM/AAAA): ")
        try:
            datetime.strptime(data_str, "%d/%m/%Y").date()
            break
        except ValueError:
            print("Formato de data inválido. Por favor, use DD/MM/AAAA.")

    local     = input("Informe o Local da Competição: ")
    categoria = input("Informe a Categoria da Competição: ")

    dados.competicoes.append(competicao)
    dados.datas.append(data_str)
    dados.locais.append(local)
    dados.categorias.append(categoria)

    salvar_dados()
    print("\n✓ Competição adicionada com sucesso!")
    input("Pressione Enter para continuar...")


def visualizar_competicoes():
    os.system("cls")
    print("========== COMPETIÇÕES CADASTRADAS ==========\n")

    if not any(e for e in dados.competicoes if e):
        print("Nenhuma competição cadastrada.")
    else:
        col1, col2, col3, col4, col5 = 22, 12, 32, 32, 18
        sep = (
            f"+{'-'*col1}+{'-'*col2}+{'-'*col3}+"
            f"{'-'*col4}+{'-'*col5}+"
        )
        print(sep)
        print(
            f"| {'Competição':<{col1-2}} "
            f"| {'Data':<{col2-2}} "
            f"| {'Local':<{col3-2}} "
            f"| {'Categoria':<{col4-2}} "
            f"| {'Dias Restantes':<{col5-2}} |"
        )
        print(sep)

        hoje = date.today()
        for i in range(len(dados.competicoes)):
            if dados.competicoes[i]:
                try:
                    data_comp   = datetime.strptime(dados.datas[i], "%d/%m/%Y").date()
                    diferenca   = data_comp - hoje
                    dias        = diferenca.days

                    if dias > 0:
                        dias_str = f"{dias} dias"
                    elif dias == 0:
                        dias_str = "HOJE!"
                    else:
                        dias_str = f"Há {-dias} dias"
                except ValueError:
                    dias_str = "Data Inválida"

                print(
                    f"| {dados.competicoes[i]:<{col1-2}} "
                    f"| {dados.datas[i]:<{col2-2}} "
                    f"| {dados.locais[i]:<{col3-2}} "
                    f"| {dados.categorias[i]:<{col4-2}} "
                    f"| {dias_str:<{col5-2}} |"
                )
        print(sep)

    input("\nPressione Enter para continuar...")


def editar_competicao():
    os.system("cls")
    competicoes_validas = [i for i, e in enumerate(dados.competicoes) if e]

    if not competicoes_validas:
        print("Nenhuma competição cadastrada.")
        input("Pressione Enter...")
        return

    print("========== EDITAR COMPETIÇÕES ==========\n")
    for idx, i in enumerate(competicoes_validas):
        print(f"{idx + 1} - {dados.competicoes[i]}")

    try:
        selecao = int(input("\nEscolha a competição: ")) - 1
        if 0 <= selecao < len(competicoes_validas):
            n = competicoes_validas[selecao]
            dados.competicoes[n] = input(f"Nova competição ({dados.competicoes[n]}): ") or dados.competicoes[n]
            dados.locais[n]      = input(f"Novo local ({dados.locais[n]}): ")            or dados.locais[n]
            dados.datas[n]       = input(f"Nova data ({dados.datas[n]}): ")              or dados.datas[n]
            dados.categorias[n]  = input(f"Nova categoria ({dados.categorias[n]}): ")   or dados.categorias[n]
            salvar_dados()
            print("\n✓ Competição editada!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um NÚMERO.")

    input("Pressione Enter para continuar...")


def excluir_competicao():
    os.system("cls")
    competicoes_validas = [i for i, e in enumerate(dados.competicoes) if e]

    if not competicoes_validas:
        print("Nenhuma competição cadastrada.")
        input("Pressione Enter...")
        return

    print("========== EXCLUIR COMPETIÇÕES ==========\n")
    for idx, i in enumerate(competicoes_validas):
        print(f"{idx + 1} - {dados.competicoes[i]}")

    try:
        selecao = int(input("\nEscolha a competição: ")) - 1
        if 0 <= selecao < len(competicoes_validas):
            n = competicoes_validas[selecao]
            dados.competicoes[n] = ""
            dados.datas[n]       = ""
            dados.locais[n]      = ""
            dados.categorias[n]  = ""
            salvar_dados()
            print("\n✓ Competição excluída!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um NÚMERO.")

    input("Pressione Enter para continuar...")