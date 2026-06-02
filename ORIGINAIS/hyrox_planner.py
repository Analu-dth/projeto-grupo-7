import os

ARQUIVO_DADOS = "hyroox_planner_dados.txt"

treinos = []
horarios = []
duraçoes = []
intensidades = []

exercicios = [] 
tempos = []
distancias = []
cargas = []
repeticoes = []

def carregar_dados():
    """Carrega todos os dados das listas de um arquivo TXT."""
    global treinos, horarios, duraçoes, intensidades, \
           exercicios, tempos, distancias, cargas, repeticoes

    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
            if len(linhas) >= 9: 
                treinos = linhas[0].strip().split(',') if linhas[0].strip() else []
                horarios = linhas[1].strip().split(',') if linhas[1].strip() else []
                duraçoes = linhas[2].strip().split(',') if linhas[2].strip() else []
                intensidades = linhas[3].strip().split(',') if linhas[3].strip() else []
                exercicios = linhas[4].strip().split(',') if linhas[4].strip() else []
                tempos = linhas[5].strip().split(',') if linhas[5].strip() else []
                distancias = linhas[6].strip().split(',') if linhas[6].strip() else []
                cargas = linhas[7].strip().split(',') if linhas[7].strip() else []
                repeticoes = linhas[8].strip().split(',') if linhas[8].strip() else []
            else:
                print("Atenção: O arquivo de dados está incompleto ou vazio. Iniciando com listas vazias.")
    else:
        print("Arquivo de dados não encontrado. Iniciando com listas vazias.")

def salvar_dados():
    """Salva todos os dados das listas em um arquivo TXT."""
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        f.write(','.join(treinos) + '\n')
        f.write(','.join(horarios) + '\n')
        f.write(','.join(duraçoes) + '\n')
        f.write(','.join(intensidades) + '\n')
        f.write(','.join(exercicios) + '\n')
        f.write(','.join(tempos) + '\n')
        f.write(','.join(distancias) + '\n')
        f.write(','.join(cargas) + '\n')
        f.write(','.join(repeticoes) + '\n')

carregar_dados()

while True:
    os.system('cls')
    print("==========HYROOX Planner==========")
    print("1 - adicionar treinos")
    print("2 - visualizar treinos")
    print("3 - editar treinos ")
    print("4 - excluir treinos")
    print("0 - sair")
    print()

    try:
        escolha = int(input("selecione a opção desejada: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        input("Pressione Enter para continuar...")
        continue

    if escolha == 0:
        os.system('cls')
        break
    elif escolha == 1:
        os.system('cls')
        escolha1 = input("deseja fazer um treino (padrão ou especifico)? ").lower()
        if escolha1 == "padrão" or escolha1 == "padrao":
            treino = input("Digite o nome do treino: ")
            treinos.append(treino)
            duracao = input("Digite a duração (ex: 45min): ")
            duraçoes.append(duracao)
            horario = input("Digite o horário (ex: 07:00): ")
            horarios.append(horario)
            intensidade = input("Digite a intensidade (Leve/Moderada/Alta): ")
            intensidades.append(intensidade)
            exercicios.append('')
            tempos.append('')
            distancias.append('')
            cargas.append('')
            repeticoes.append('')

            salvar_dados()
            print("✓ Treino padrão adicionado!\n")
            input("Pressione Enter para continuar...")
        elif escolha1 == "especifico" or escolha1 == "específico":
            print("Opções: sled push,sled pull, burpee broad jumps, wall balls, farmer’s carry")
            exercicio_nome = input("Digite o nome do exercício: ") 
            tempo = input("Digite o tempo (ex: 02:30): ")
            distancia = input("Digite a distância (ex: 100m): ")
            carga = input("Digite a carga (ex: 80kg): ")
            repeticao = input("Digite as repetições: ")

            treinos.append('')
            horarios.append('')
            duraçoes.append('')
            intensidades.append('')

            exercicios.append(exercicio_nome)
            tempos.append(tempo)
            distancias.append(distancia)
            cargas.append(carga)
            repeticoes.append(repeticao)

            salvar_dados() 
            print("\n✓ Desempenho registrado!")
            input("Pressione Enter para continuar...")
        else:
            print("Opção não encontrada, digite novamente!!!")
            input("Pressione Enter para continuar...")


    elif escolha == 2:
        os.system('cls')
        print("\n========== TREINOS PADRÃO CADASTRADOS ==========")
        if not any(t for t in treinos if t): 
            print("Nenhum treino padrão cadastrado ainda! \n")
        else:
            col1, col2, col3, col4 = 20, 12, 10, 12
            sep = f"+{'-'*col1}+{'-'*col2}+{'-'*col3}+{'-'*col4}+"

            print(sep)
            print(f"| {'Treino':<{col1-2}} | {'Horário':<{col2-2}} | {'Duração':<{col3-2}} | {'Intensidade':<{col4-2}} |")
            print(sep)

            for i in range(len(treinos)):
                if treinos[i]: 
                    print(f"| {treinos[i]:<{col1-2}} | {horarios[i]:<{col2-2}} | {duraçoes[i]:<{col3-2}} | {intensidades[i]:<{col4-2}} |")

            print(sep)
            print(f"  Total de treinos padrão: {len([t for t in treinos if t])}\n") 

        print("\n========== EXERCÍCIOS ESPECÍFICOS CADASTRADOS ==========")
        if not any(e for e in exercicios if e): 
            print("Nenhum exercício específico cadastrado ainda!\n")
        else:
            col1, col2, col3, col4, col5 = 22, 12, 12, 12, 12
            sep = (
                f"+{'-'*col1}+{'-'*col2}+{'-'*col3}+"
                f"{'-'*col4}+{'-'*col5}+"
            )
            print(sep)
            print(
                f"| {'Exercício':<{col1-2}} | "
                f"{'Tempo':<{col2-2}} | "
                f"{'Distância':<{col3-2}} | "
                f"{'Carga':<{col4-2}} | "
                f"{'Reps':<{col5-2}} |"
            )
            print(sep)

            for i in range(len(exercicios)):
                if exercicios[i]: 
                    print(
                        f"| {exercicios[i]:<{col1-2}} | "
                        f"{tempos[i]:<{col2-2}} | "
                        f"{distancias[i]:<{col3-2}} | "
                        f"{cargas[i]:<{col4-2}} | "
                        f"{repeticoes[i]:<{col5-2}} |"
                    )
            print(sep)
            print(f"  Total de exercícios específicos: {len([e for e in exercicios if e])}\n") 

        input("Pressione Enter para continuar...")

    elif escolha == 3:
        os.system('cls')
        if not any(t for t in treinos if t) and not any(e for e in exercicios if e):
            print("Nenhum treino cadastrado ainda! \n")
        else:
            print("Qual tipo de treino deseja editar?")
            print("1 - Treino Padrão")
            print("2 - Exercício Específico")
            try:
                tipo_edicao = int(input("Selecione a opção: "))
                if tipo_edicao == 1:
                    treinos_validos_indices = [i for i, t in enumerate(treinos) if t]
                    if not treinos_validos_indices:
                        print("Nenhum treino padrão para editar.")
                    else:
                        print("\n--- Treinos Padrão ---")
                        for idx, i in enumerate(treinos_validos_indices):
                            print(f"{idx + 1} - {treinos[i]}")

                        try:
                            selecao = int(input("Qual número do treino padrão quer editar? ")) - 1
                            if 0 <= selecao < len(treinos_validos_indices):
                                numero = treinos_validos_indices[selecao] 
                                treinos[numero]      = input(f"Novo nome ({treinos[numero]}): ") or treinos[numero]
                                duraçoes[numero]     = input(f"Nova duração ({duraçoes[numero]}): ") or duraçoes[numero]
                                horarios[numero]     = input(f"Novo horário ({horarios[numero]}): ") or horarios[numero]
                                intensidades[numero] = input(f"Nova intensidade ({intensidades[numero]}): ") or intensidades[numero]
                                salvar_dados() 
                                print("Treino padrão editado!\n")
                            else:
                                print("Número de treino inválido.")
                        except ValueError:
                            print("Entrada inválida. Por favor, digite um número.")
                elif tipo_edicao == 2:
                    exercicios_validos_indices = [i for i, e in enumerate(exercicios) if e]
                    if not exercicios_validos_indices:
                        print("Nenhum exercício específico para editar.")
                    else:
                        print("\n--- Exercícios Específicos ---")
                        for idx, i in enumerate(exercicios_validos_indices):
                            print(f"{idx + 1} - {exercicios[i]}")

                        try:
                            selecao = int(input("Qual número do exercício específico quer editar? ")) - 1
                            if 0 <= selecao < len(exercicios_validos_indices):
                                numero = exercicios_validos_indices[selecao] 
                                exercicios[numero] = input(f"Novo nome do exercício ({exercicios[numero]}): ") or exercicios[numero]
                                tempos[numero] = input(f"Novo tempo ({tempos[numero]}): ") or tempos[numero]
                                distancias[numero] = input(f"Nova distância ({distancias[numero]}): ") or distancias[numero]
                                cargas[numero] = input(f"Nova carga ({cargas[numero]}): ") or cargas[numero]
                                repeticoes[numero] = input(f"Novas repetições ({repeticoes[numero]}): ") or repeticoes[numero]
                                salvar_dados() 
                                print("Exercício específico editado!\n")
                            else:
                                print("Número de exercício inválido.")
                        except ValueError:
                            print("Entrada inválida. Por favor, digite um número.")
                else:
                    print("Opção de edição inválida.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
        input("Pressione Enter para continuar...")

    elif escolha == 4:
        os.system('cls')
        if not any(t for t in treinos if t) and not any(e for e in exercicios if e):
            print("Nenhum treino cadastrado ainda! \n")
        else:
            print("Qual tipo de treino deseja excluir?")
            print("1 - Treino Padrão")
            print("2 - Exercício Específico")
            try:
                tipo_exclusao = int(input("Selecione a opção: "))
                if tipo_exclusao == 1:
                    treinos_validos_indices = [i for i, t in enumerate(treinos) if t]
                    if not treinos_validos_indices:
                        print("Nenhum treino padrão para excluir.")
                    else:
                        print("\n--- Treinos Padrão ---")
                        for idx, i in enumerate(treinos_validos_indices):
                            print(f"{idx + 1} - {treinos[i]}")

                        try:
                            selecao = int(input("Qual número do treino padrão quer excluir? ")) - 1
                            if 0 <= selecao < len(treinos_validos_indices):
                                numero = treinos_validos_indices[selecao] 
                                treinos[numero] = ''
                                horarios[numero] = ''
                                duraçoes[numero] = ''
                                intensidades[numero] = ''
                                salvar_dados() 
                                print("Treino padrão excluído!\n")
                            else:
                                print("Número de treino inválido.")
                        except ValueError:
                            print("Entrada inválida. Por favor, digite um número.")
                elif tipo_exclusao == 2:
                    exercicios_validos_indices = [i for i, e in enumerate(exercicios) if e]
                    if not exercicios_validos_indices:
                        print("Nenhum exercício específico para excluir.")
                    else:
                        print("\n--- Exercícios Específicos ---")
                        for idx, i in enumerate(exercicios_validos_indices):
                            print(f"{idx + 1} - {exercicios[i]}")

                        try:
                            selecao = int(input("Qual número do exercício específico quer excluir? ")) - 1
                            if 0 <= selecao < len(exercicios_validos_indices):
                                numero = exercicios_validos_indices[selecao] 
                                exercicios[numero] = ''
                                tempos[numero] = ''
                                distancias[numero] = ''
                                cargas[numero] = ''
                                repeticoes[numero] = ''
                                salvar_dados() 
                                print("Exercício específico excluído!\n")
                            else:
                                print("Número de exercício inválido.")
                        except ValueError:
                            print("Entrada inválida. Por favor, digite um número.")
                else:
                    print("Opção de exclusão inválida.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
        input("Pressione Enter para continuar...")
    else:
        print("Opção inválida. Tente novamente.")
        input("Pressione Enter para continuar...")