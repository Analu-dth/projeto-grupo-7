import os
import csv

ARQUIVO_SUGESTOES = "arquivos/sugestoes.csv"


def menu_sugestoes():
    while True:
        os.system("cls")
        print("===== SUGESTÕES PERSONALIZADAS =====\n")
        print("1 - Iniciante")
        print("2 - Intermediário")
        print("3 - Avançado")
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
            menu_nivel("iniciante", "INICIANTE")
        elif escolha == 2:
            menu_nivel("intermediario", "INTERMEDIÁRIO")
        elif escolha == 3:
            menu_nivel("avancado", "AVANÇADO")
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")


def carregar_sugestoes(nivel):
    sugestoes = []

    if not os.path.exists(ARQUIVO_SUGESTOES):
        return sugestoes

    with open(ARQUIVO_SUGESTOES, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("nivel", "").strip().lower() == nivel.lower():
                sugestoes.append(row)

    return sugestoes


def menu_nivel(nivel, titulo):
    """Menu intermediário que lista os nomes dos treinos do nível escolhido."""
    sugestoes = carregar_sugestoes(nivel)

    if not sugestoes:
        os.system("cls")
        print(f"===== SUGESTÕES PARA {titulo} =====\n")
        print("Nenhuma sugestão encontrada para este nível.")
        input("\nPressione Enter para continuar...")
        return

    while True:
        os.system("cls")
        print(f"===== SUGESTÕES PARA {titulo} =====\n")
        print("Selecione um treino para ver os detalhes:\n")

        for idx, s in enumerate(sugestoes, start=1):
            print(f"{idx} - {s.get('nome_treino', '')}")

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
        elif 1 <= escolha <= len(sugestoes):
            exibir_detalhe(sugestoes[escolha - 1], titulo)
        else:
            print("Número inválido.")
            input("Pressione Enter para continuar...")


def exibir_detalhe(sugestao, titulo):
    """Exibe os detalhes completos de um treino específico."""
    os.system("cls")
    print(f"===== SUGESTÕES PARA {titulo} =====\n")
    print(f"Treino      : {sugestao.get('nome_treino', '')}")
    print(f"Descrição   : {sugestao.get('descricao', '')}")
    print(f"Dias/semana : {sugestao.get('dias_semana', '')}")
    print(f"Foco        : {sugestao.get('foco', '')}")
    print(f"Duração     : {sugestao.get('duracao_minutos', '')} min")
    print(f"Intensidade : {sugestao.get('intensidade', '')}")
    print("-" * 50)
    input("\nPressione Enter para continuar...")