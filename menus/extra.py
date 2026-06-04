# evolucao.py
import os
import dados

def menu_extra():
   elif desejo == 4:
    while True:
        os.system("cls")

        print("========== CALENDÁRIO ==========")
        print("1 - Cadastrar novo dia")
        print("2 - Visualizar dias cadastrados")
        print("0 - Voltar")
        print()

        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite um número válido!")
            input("Pressione Enter para continuar...")
            continue

        if escolha == 0:
            break

        elif escolha == 1:
            os.system("cls")

            while True:
                data = input("Digite a data (DD/MM/AAAA): ")

                try:
                    datetime.strptime(data, "%d/%m/%Y")
                    break
                except ValueError:
                    print("Data inválida! Use o formato DD/MM/AAAA.")

            peso = input("Informe o peso (kg): ")
            altura = input("Informe a altura (m): ")
            treino = input("Informe o treino realizado: ")

            datas_calendario.append(data)
            pesos.append(peso)
            alturas.append(altura)
            treinos_dia.append(treino)

            print("\n✓ Dia cadastrado com sucesso!")
            input("Pressione Enter para continuar...")

        elif escolha == 2:
            os.system("cls")

            print("========== DIAS CADASTRADOS ==========\n")

            if len(datas_calendario) == 0:
                print("Nenhum dia cadastrado.")

            else:
                largura1 = 15
                largura2 = 10
                largura3 = 10
                largura4 = 35

                separador = (
                    "+" + "-" * largura1 +
                    "+" + "-" * largura2 +
                    "+" + "-" * largura3 +
                    "+" + "-" * largura4 + "+"
                )

                print(separador)
                print(
                    f"| {'Data':<{largura1-2}}"
                    f"| {'Peso':<{largura2-2}}"
                    f"| {'Altura':<{largura3-2}}"
                    f"| {'Treino':<{largura4-2}}|"
                )
                print(separador)

                for i in range(len(datas_calendario)):
                    print(
                        f"| {datas_calendario[i]:<{largura1-2}}"
                        f"| {pesos[i]:<{largura2-2}}"
                        f"| {alturas[i]:<{largura3-2}}"
                        f"| {treinos_dia[i]:<{largura4-2}}|"
                    )

                print(separador)

            input("\nPressione Enter para continuar...")

        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")
