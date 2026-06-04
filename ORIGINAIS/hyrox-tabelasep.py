import os
from datetime import datetime, date

ARQUIVO_DADOS = "hyroox_planner_dados.txt"

treinos = []
horarios = []
duracoes = []
intensidades = []

exercicios = []
tempos = []
distancias = []
cargas = []
repeticoes = []

competicoes = []
locais = []
datas = []
categorias = []


def carregar_dados():
    global treinos, horarios, duracoes, intensidades
    global exercicios, tempos, distancias, cargas, repeticoes
    global competicoes, locais, datas, categorias

    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            linhas = f.readlines()

            if len(linhas) >= 13:
                treinos = linhas[0].strip().split(",") if linhas[0].strip() else []
                horarios = linhas[1].strip().split(",") if linhas[1].strip() else []
                duracoes = linhas[2].strip().split(",") if linhas[2].strip() else []
                intensidades = linhas[3].strip().split(",") if linhas[3].strip() else []

                exercicios = linhas[4].strip().split(",") if linhas[4].strip() else []
                tempos = linhas[5].strip().split(",") if linhas[5].strip() else []
                distancias = linhas[6].strip().split(",") if linhas[6].strip() else []
                cargas = linhas[7].strip().split(",") if linhas[7].strip() else []
                repeticoes = linhas[8].strip().split(",") if linhas[8].strip() else []

                competicoes = linhas[9].strip().split(",") if linhas[9].strip() else []
                locais = linhas[10].strip().split(",") if linhas[10].strip() else []
                datas = linhas[11].strip().split(",") if linhas[11].strip() else []
                categorias = linhas[12].strip().split(",") if linhas[12].strip() else []

            else:
                print("Arquivo incompleto. Iniciando listas vazias.")
    else:
        print("Arquivo não encontrado. Iniciando listas vazias.")


def salvar_dados():
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        f.write(",".join(treinos) + "\n")
        f.write(",".join(horarios) + "\n")
        f.write(",".join(duracoes) + "\n")
        f.write(",".join(intensidades) + "\n")

        f.write(",".join(exercicios) + "\n")
        f.write(",".join(tempos) + "\n")
        f.write(",".join(distancias) + "\n")
        f.write(",".join(cargas) + "\n")
        f.write(",".join(repeticoes) + "\n")

        f.write(",".join(competicoes) + "\n")
        f.write(",".join(locais) + "\n")
        f.write(",".join(datas) + "\n")
        f.write(",".join(categorias) + "\n")

def extrair_numero(texto):
    numero = ""

    for caractere in texto:
        if caractere.isdigit() or caractere == ".":
            numero += caractere

    if numero:
        return float(numero)

    return None

carregar_dados()

while True:
    os.system("cls")
    print("========== HYROOX PLANNER ==========")
    print("1 - CRUD de Treinos")
    print("2 - Exercícios e Controle de Desempenho")
    print("3 - Planejamento de Competições")
    print("4 - Acompanhamento de evolução")
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
                escolha1 = int(input("Escolha uma opção: "))
            except ValueError:
                print("Entrada inválida. Por favor, digite um NÚMERO.")
                input("Pressione Enter...")
                continue
            if escolha1 == 0:
                break
            elif escolha1 == 1:
                os.system("cls")

                treino = input("Digite o nome do treino: ")
                duracao = input("Digite a duração: ")
                horario = input("Digite o horário: ")
                intensidade = input("Digite a intensidade: ")

                treinos.append(treino)
                duracoes.append(duracao)
                horarios.append(horario)
                intensidades.append(intensidade)

                exercicios.append("")
                tempos.append("")
                distancias.append("")
                cargas.append("")
                repeticoes.append("")
                salvar_dados()
                print("\n✓ Treino adicionado com sucesso!")
                input("Pressione Enter para continuar...")

            elif escolha1 == 2:
                os.system("cls")
                print("========== TREINOS CADASTRADOS ==========\n")
                if not any(t for t in treinos if t):
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

                    for i in range(len(treinos)):
                        if treinos[i]:
                            print(
                                f"| {treinos[i]:<{col1-2}} "
                                f"| {horarios[i]:<{col2-2}} "
                                f"| {duracoes[i]:<{col3-2}} "
                                f"| {intensidades[i]:<{col4-2}} |"
                            )

                    print(sep)

                input("\nPressione Enter para continuar...")

            elif escolha1 == 3:
                while True:
                    os.system("cls")
                    treinos_validos = [i for i, t in enumerate(treinos) if t]
                    if not treinos_validos:
                        print("Nenhum treino cadastrado.")
                        input("Pressione Enter...")
                        break
                    print("========== EDITAR TREINOS ==========\n")
                    for idx, i in enumerate(treinos_validos):
                        print(f"{idx + 1} - {treinos[i]}")
                    try:
                        selecao = int(input("\nEscolha o treino: ")) - 1
                        if 0 <= selecao < len(treinos_validos):
                            numero = treinos_validos[selecao]
                            treinos[numero] = (input(f"Novo nome ({treinos[numero]}): ") or treinos[numero])
                            duracoes[numero] = (input(f"Nova duração ({duracoes[numero]}): ") or duracoes[numero])
                            horarios[numero] = (input(f"Novo horário ({horarios[numero]}): ") or horarios[numero])
                            intensidades[numero] = (input(f"Nova intensidade ({intensidades[numero]}): ") or intensidades[numero])
                            salvar_dados()
                            print("\n✓ Treino editado!")
                            break
                        else:
                            print("Número inválido.")
                            input("Pressione Enter e tente novamente...")
                            continue
                    except ValueError:
                        print("Entrada inválida. Por favor, digite um NÚMERO.")
                        input("Pressione Enter e tente novamente...")
                        continue
                input("Pressione Enter para continuar...")

            elif escolha1 == 4:
                while True:
                    os.system("cls")
                    treinos_validos = [i for i, t in enumerate(treinos) if t]
                    if not treinos_validos:
                        print("Nenhum treino cadastrado.")
                        input("Pressione Enter...")
                        break
                    print("========== EXCLUIR TREINOS ==========\n")

                    for idx, i in enumerate(treinos_validos):
                        print(f"{idx + 1} - {treinos[i]}")
                    try:
                        selecao = int(input("\nEscolha o treino: ")) - 1
                        if 0 <= selecao < len(treinos_validos):

                            numero = treinos_validos[selecao]

                            treinos[numero] = ""
                            horarios[numero] = ""
                            duracoes[numero] = ""
                            intensidades[numero] = ""

                            salvar_dados()
                            print("\n✓ Treino excluído!")
                            break
                        else:
                            print("Número inválido.")
                            input("Pressione Enter e tente novamente...")
                            continue
                    except ValueError:
                        print("Entrada inválida. Por favor, digite um NÚMERO.")
                        input("Pressione Enter e tente novamente...")
                        continue
                input("Pressione Enter para continuar...")
            else:
                print("Opção inválida.")
                input("Pressione Enter para continuar...")

    elif desejo == 2:
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
                escolha2 = int(input("Escolha uma opção: "))
            except ValueError:
                print("Entrada inválida. Por favor, digite um NÚMERO.")
                input("Pressione Enter...")
                continue
            if escolha2 == 0:
                break

            elif escolha2 == 1:
                while True:
                    os.system("cls")

                    print("=================================================")
                    print("Opções:\n"
                            "1- sled push\n"
                            "2- sled pull\n"
                            "3- burpee broad jumps\n"
                            "4- wall balls\n"
                            "5- farmer’s carry\n")
                    print("=================================================")

                    opcoes_exercicios = ["sled push", "sled pull", "burpee broad jumps", "wall balls", "farmer’s carry"]

                    try:
                        numero_escolhido= int(input("Digite o n° do exercício: "))

                        if 1 <= numero_escolhido <= len(opcoes_exercicios):
                            exercicio_nome = opcoes_exercicios[numero_escolhido - 1]
                            break
                        else:
                            print("\n Opção inválida! Escolha um número de 1 a 5.")
                            input("Pressione Enter e tente novamente...")
                            continue
                    except ValueError:
                        print("\n Entrada inválida! Por favor, digite um NÚMERO.")
                        input("Pressione Enter e tente novamente...")
                        continue


                tempo = input("Digite o tempo: ")
                distancia = input("Digite a distância: ")
                carga = input("Digite a carga: ")
                repeticao = input("Digite as repetições: ")

                treinos.append("")
                horarios.append("")
                duracoes.append("")
                intensidades.append("")

                exercicios.append(exercicio_nome)
                tempos.append(tempo)
                distancias.append(distancia)
                cargas.append(carga)
                repeticoes.append(repeticao)

                salvar_dados()
                print("\n✓ Exercício adicionado!")
                input("Pressione Enter para continuar...")
            elif escolha2 == 2:
                os.system("cls")
                print("========== EXERCÍCIOS CADASTRADOS ==========\n")
                if not any(e for e in exercicios if e):
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
                    for i in range(len(exercicios)):
                        if exercicios[i]:
                            print(
                                f"| {exercicios[i]:<{col1-2}} "
                                f"| {tempos[i]:<{col2-2}} "
                                f"| {distancias[i]:<{col3-2}} "
                                f"| {cargas[i]:<{col4-2}} "
                                f"| {repeticoes[i]:<{col5-2}} |"
                            )
                    print(sep)
                input("\nPressione Enter para continuar...")

            elif escolha2 == 3:
                while True:
                    os.system("cls")
                    exercicios_validos = [i for i, e in enumerate(exercicios) if e]
                    if not exercicios_validos:
                        print("Nenhum exercício cadastrado.")
                        input("Pressione Enter...")
                        break
                    print("========== EDITAR EXERCÍCIOS ==========\n")
                    for idx, i in enumerate(exercicios_validos):
                        print(f"{idx + 1} - {exercicios[i]}")
                    try:
                        selecao = int(input("\nEscolha o exercício: ")) - 1
                        if 0 <= selecao < len(exercicios_validos):
                            numero = exercicios_validos[selecao]
                            exercicios[numero] = (input(f"Novo exercício ({exercicios[numero]}): ") or exercicios[numero])
                            tempos[numero] = (input(f"Novo tempo ({tempos[numero]}): ") or tempos[numero])
                            distancias[numero] = (input(f"Nova distância ({distancias[numero]}): ") or distancias[numero])
                            cargas[numero] = (input(f"Nova carga ({cargas[numero]}): ") or cargas[numero])
                            repeticoes[numero] = (input(f"Novas repetições ({repeticoes[numero]}): ") or repeticoes[numero])
                            salvar_dados()
                            print("\n✓ Exercício editado!")
                            break
                        else:
                            print("Número inválido.")
                            input("Pressione Enter e tente novamente...")
                            continue
                    except ValueError:
                        print("Entrada inválida. Por favor, digite um NÚMERO.")
                        input("Pressione Enter e tente novamente...")
                        continue
                input("Pressione Enter para continuar...")
            elif escolha2 == 4:
                while True:
                    os.system("cls")
                    exercicios_validos = [
                        i for i, e in enumerate(exercicios) if e]
                    if not exercicios_validos:
                        print("Nenhum exercício cadastrado.")
                        input("Pressione Enter...")
                        break
                    print("========== EXCLUIR EXERCÍCIOS ==========\n")
                    for idx, i in enumerate(exercicios_validos):
                        print(f"{idx + 1} - {exercicios[i]}")
                    try:
                        selecao = int(input("\nEscolha o exercício: ")) - 1
                        if 0 <= selecao < len(exercicios_validos):
                            numero = exercicios_validos[selecao]
                            exercicios[numero] = ""
                            tempos[numero] = ""
                            distancias[numero] = ""
                            cargas[numero] = ""
                            repeticoes[numero] = ""
                            salvar_dados()
                            print("\n✓ Exercício excluído!")
                            break
                        else:
                            print("Número inválido.")
                            input("Pressione Enter e tente novamente...")
                            continue
                    except ValueError:
                        print("Entrada inválida. Por favor, digite um NÚMERO.")
                        input("Pressione Enter e tente novamente...")
                        continue
                input("Pressione Enter para continuar...")
            else:
                print("Opção inválida.")
                input("Pressione Enter para continuar...")
    elif desejo == 3:
        while True:
            os.system("cls")
            print("===== PAINEL DE COMPETIÇÕES =====")
            print("1 - Cadastrar Competição")
            print("2 - Visualizar Competição")
            print("3 - Editar Competição")
            print("4 - Excluir Competição")
            print("0 - Voltar")
            print()
            try:
                escolha3 = int(input("Escolha uma opção: "))
            except ValueError:
                print("Entrada inválida. Por favor, digite um NÚMERO.")
                input("Pressione Enter...")
                continue
            if escolha3 == 0:
                break
            elif escolha3 == 1:
                os.system("cls")

                competicao = input("Informe o nome da Competição: ")
                
                while True:
                    data_str = input("Informe a Data desta Competição (DD/MM/AAAA): ")
                    try:
                        datetime.strptime(data_str, "%d/%m/%Y").date()
                        break
                    except ValueError:
                        print("Formato de data inválido. Por Favor, use DD/MM/AAAA.")

                local = input("Informe o Local da Competição: ")
                categoria = input("Informe a categoria da Competição: ")

                competicoes.append(competicao)
                datas.append(data_str)
                locais.append(local)
                categorias.append(categoria)

                competicoes.append("")
                datas.append("")
                locais.append("")
                categorias.append("")
                salvar_dados()
                print("\n✓ Competição adicionada com sucesso!")
                input("Pressione Enter para continuar...")
            elif escolha3 == 2:
                os.system("cls")
                print("========== COMPETIÇÕES CADASTRADAS ==========\n")
                if not any(e for e in competicoes if e):
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
                    
                    for i in range(len(competicoes)):
                        if competicoes[i]:
                            dias_restantes_str = "N/A"
                            try:
                                data_competicao = datetime.strptime(datas[i], "%d/%m/%Y").date()
                                diferenca = data_competicao - hoje
                                dias_restantes = diferenca.days

                                if dias_restantes > 0:
                                    dias_restantes_str = f"{dias_restantes} dias"
                                elif dias_restantes == 0:
                                    dias_restantes_str = "HOJE!"
                                else:
                                    dias_restantes_str = f"Há {-dias_restantes} dias"
                            except ValueError:
                                dias_restantes_str = "Data Inválioda"
                            print(
                                f"| {competicoes[i]:<{col1-2}} "
                                f"| {datas[i]:<{col2-2}} "
                                f"| {locais[i]:<{col3-2}} "
                                f"| {categorias[i]:<{col4-2}} "
                                f"| {dias_restantes_str:<{col5-2}} |"
                            )
                    print(sep)
                input("\nPressione Enter para continuar...")

            elif escolha3 == 3:
                while True:
                    os.system("cls")
                    competicoes_validas = [i for i, e in enumerate(competicoes) if e]
                    if not competicoes_validas:
                        print("Nenhuma competição cadastrado.")
                        input("Pressione Enter...")
                        break
                    print("========== EDITAR COMPETIÇÕES ==========\n")
                    for idx, i in enumerate(competicoes_validas):
                        print(f"{idx + 1} - {competicoes[i]}")
                    try:
                        selecao_comp = int(input("\nEscolha a competição: ")) - 1
                        if 0 <= selecao_comp < len(competicoes_validas):
                            numero = competicoes_validas[selecao_comp]
                            competicoes[numero] = (input(f"Nova competição ({competicoes[numero]}): ") or competicoes[numero])
                            locais[numero] = (input(f"Novo local ({locais[numero]}): ") or locais[numero])
                            while True:
                                datas[numero] = (input(f"Nova data, use DD/MM/AAAA ({datas[numero]}): ") or datas[numero])
                                try:
                                    datetime.strptime(datas[numero], "%d/%m/%Y").date()
                                    break
                                except ValueError:
                                    print("Formato de data inválido. Por Favor, use DD/MM/AAAA.")
                            categorias[numero] = (input(f"Nova categoria ({categorias[numero]}): ") or categorias[numero])
                            salvar_dados()
                            print("\n✓ Competição editada!")
                            break
                        else:
                            print("Número inválido.")
                            input("Pressione Enter e tente novamente...")
                            continue
                    except ValueError:
                        print("Entrada inválida. Por favor, digite um NÚMERO.")
                        input("Pressione Enter e tente novamente...")
                        continue
                input("Pressione Enter para continuar...")
                
            elif escolha3 == 4:
                while True:
                    os.system("cls")
                    competicoes_validas = [
                        i for i, e in enumerate(competicoes) if e]
                    if not competicoes_validas:
                        print("Nenhuma competição cadastrada.")
                        input("Pressione Enter...")
                        break
                    print("========== EXCLUIR COMPETIÇÕES ==========\n")
                    for idx, i in enumerate(competicoes_validas):
                        print(f"{idx + 1} - {competicoes[i]}")
                    try:
                        selecao_comp = int(input("\nEscolha a competição: ")) - 1
                        if 0 <= selecao_comp < len(competicoes_validas):
                            numero = competicoes_validas[selecao_comp]
                            competicoes[numero] = ""
                            datas[numero] = ""
                            locais[numero] = ""
                            categorias[numero] = ""
                            salvar_dados()
                            print("\n✓ Competição excluída!")
                            break
                        else:
                            print("Número inválido.")
                            input("Pressione Enter e tente novamente...")
                            continue
                    except ValueError:
                        print("Entrada inválida. Por favor, digite um NÚMERO.")
                        input("Pressione Enter e tente novamente...")
                        continue
                input("Pressione Enter para continuar...")
            else:
                print("Opção inválida.")
                input("Pressione Enter para continuar...")
    elif desejo == 4:
        os.system("cls")
        print("===== ACOMPANHAMENTO DE EVOLUÇÃO =====\n")

        # Frequência de treinos
        total_treinos = len([t for t in treinos if t])

        # Exercícios válidos
        exercicios_validos = [
            i for i, e in enumerate(exercicios)
            if e and tempos[i] and cargas[i]
        ]

        print(f"Total de treinos cadastrados: {total_treinos}")

        if not exercicios_validos:
            print("\nNão há dados suficientes para análise de evolução.")
            input("\nPressione Enter para continuar...")
            continue

        print("\n========== EVOLUÇÃO DOS EXERCÍCIOS ==========\n")

        exercicios_unicos = list(set(
            exercicios[i] for i in exercicios_validos
        ))

        for nome_exercicio in exercicios_unicos:

            indices = [
                i for i in exercicios_validos
                if exercicios[i] == nome_exercicio
            ]

            if len(indices) < 2:
                continue

            primeiro = indices[0]
            ultimo = indices[-1]

            print(f"Exercício: {nome_exercicio}")

            # Evolução de tempo
            try:
                tempo_inicial = extrair_numero(tempos[primeiro])
                tempo_final = extrair_numero(tempos[ultimo])

                if tempo_inicial is not None and tempo_final is not None:
                    diferenca_tempo = tempo_inicial - tempo_final

                if diferenca_tempo > 0:
                    print(
                        f"  ✓ Melhora de tempo: {diferenca_tempo:.2f}"
                    )
                elif diferenca_tempo < 0:
                    print(
                        f"  ⚠ Tempo aumentou em {-diferenca_tempo:.2f}"
                    )
                else:
                    print("  Tempo mantido.")
            except ValueError:
                print("  Tempo não analisável.")

            # Evolução de carga
            try:
                carga_inicial = extrair_numero(cargas[primeiro])
                carga_final = extrair_numero(cargas[ultimo])
                if carga_inicial is not None and carga_final is not None:
                    diferenca_carga = carga_final - carga_inicial

                if diferenca_carga > 0:
                    print(
                        f"  ✓ Aumento de carga: {diferenca_carga:.2f}"
                    )
                elif diferenca_carga < 0:
                    print(
                        f"  Carga reduziu em {-diferenca_carga:.2f}"
                    )
                else:
                    print("  Carga mantida.")
            except ValueError:
                print("  Carga não analisável.")

            print("-" * 40)

        input("\nPressione Enter para continuar...")
    else:
        print("Opção inválida. Por favor, digite um NÚMERO.")
        input("Pressione Enter para continuar...")
