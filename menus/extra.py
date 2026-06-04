# menus/extra.py
import os

def menu_extra():
    os.system("cls")
    import os
from datetime import datetime

dias_semana = [
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo"
]

tabela = {}

for dia in dias_semana:
    tabela[dia] = {
        "Data": "",
        "Treino": "",
        "RPE": "",
        "Humor": "",
        "Observacoes": ""
    }


def configurar_dia():
    os.system("cls")

    print("===== ESCOLHA O DIA =====\n")

    for i, dia in enumerate(dias_semana):
        print(f"{i+1} - {dia}")

    try:
        escolha = int(input("\nDigite o número do dia: ")) - 1

        if escolha < 0 or escolha >= len(dias_semana):
            print("Dia inválido.")
            input("Pressione Enter...")
            return

    except ValueError:
        print("Digite um número válido.")
        input("Pressione Enter...")
        return

    dia_escolhido = dias_semana[escolha]

    os.system("cls")
    print(f"===== CONFIGURANDO {dia_escolhido.upper()} =====\n")

    print("1 - Usar data de hoje")
    print("2 - Digitar uma data")

    opcao_data = input("\nEscolha: ")

    if opcao_data == "1":
        data = datetime.now().strftime("%d/%m/%Y")
    else:
        data = input("Digite a data (DD/MM/AAAA): ")

    treino = input("Treino realizado: ")

    while True:
        try:
            rpe = int(input("RPE (1-10): "))
            if 1 <= rpe <= 10:
                break
            else:
                print("Digite um valor entre 1 e 10.")
        except ValueError:
            print("Digite um número válido.")

    print("\nHumor:")
    print("1 - Bem")
    print("2 - Ok")
    print("3 - Cansado")

    humor_op = input("Escolha: ")

    if humor_op == "1":
        humor = "Bem"
    elif humor_op == "2":
        humor = "Ok"
    else:
        humor = "Cansado"

    observacoes = input("Observações: ")

    tabela[dia_escolhido]["Data"] = data
    tabela[dia_escolhido]["Treino"] = treino
    tabela[dia_escolhido]["RPE"] = str(rpe)
    tabela[dia_escolhido]["Humor"] = humor
    tabela[dia_escolhido]["Observacoes"] = observacoes

    print("\n✓ Dia configurado com sucesso!")
    input("Pressione Enter...")


def visualizar_tabela():
    os.system("cls")

    print("============== TABELA SEMANAL ==============\n")

    cab = (
        f"+{'-'*16}+{'-'*12}+{'-'*22}+"
        f"{'-'*6}+{'-'*12}+{'-'*32}+"
    )

    print(cab)
    print(
        f"| {'Dia':<14}"
        f"| {'Data':<10}"
        f"| {'Treino':<20}"
        f"| {'RPE':<4}"
        f"| {'Humor':<10}"
        f"| {'Observações':<30}|"
    )
    print(cab)

    for dia in dias_semana:
        print(
            f"| {dia:<14}"
            f"| {tabela[dia]['Data']:<10}"
            f"| {tabela[dia]['Treino']:<20}"
            f"| {tabela[dia]['RPE']:<4}"
            f"| {tabela[dia]['Humor']:<10}"
            f"| {tabela[dia]['Observacoes']:<30}|"
        )

    print(cab)
    input("\nPressione Enter para continuar...")


def editar_dia():
    os.system("cls")

    print("===== EDITAR UM DIA =====\n")

    for i, dia in enumerate(dias_semana):
        print(f"{i+1} - {dia}")

    try:
        escolha = int(input("\nEscolha o dia: ")) - 1

        if escolha < 0 or escolha >= len(dias_semana):
            print("Dia inválido.")
            input("Pressione Enter...")
            return

    except ValueError:
        print("Digite um número válido.")
        input("Pressione Enter...")
        return

    dia = dias_semana[escolha]

    os.system("cls")

    print(f"Editando {dia}\n")
    print("Deixe vazio e pressione Enter para manter o valor atual.\n")

    novo = input(f"Data ({tabela[dia]['Data']}): ")
    if novo != "":
        tabela[dia]["Data"] = novo

    novo = input(f"Treino ({tabela[dia]['Treino']}): ")
    if novo != "":
        tabela[dia]["Treino"] = novo

    novo = input(f"RPE ({tabela[dia]['RPE']}): ")
    if novo != "":
        tabela[dia]["RPE"] = novo

    novo = input(f"Humor ({tabela[dia]['Humor']}): ")
    if novo != "":
        tabela[dia]["Humor"] = novo

    novo = input(f"Observações ({tabela[dia]['Observacoes']}): ")
    if novo != "":
        tabela[dia]["Observacoes"] = novo

    print("\n✓ Informações atualizadas com sucesso!")
    input("Pressione Enter...")


def menu_extra():

    while True:
        os.system("cls")

        print("======= PLANEJADOR SEMANAL DE TREINOS =======")
        print("1 - Configurar um dia da semana")
        print("2 - Visualizar tabela semanal")
        print("3 - Editar um dia")
        print("0 - Voltar")
        print()

        try:
            op = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite um número válido.")
            input("Pressione Enter...")
            continue

        if op == 0:
            break

        elif op == 1:
            configurar_dia()

        elif op == 2:
            visualizar_tabela()

        elif op == 3:
            editar_dia()

        else:
            print("Opção inválida.")
            input("Pressione Enter...")
