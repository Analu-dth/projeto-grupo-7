import os

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
                treinos      = linhas[0].strip().split(",") if linhas[0].strip() else []
                horarios     = linhas[1].strip().split(",") if linhas[1].strip() else []
                duracoes     = linhas[2].strip().split(",") if linhas[2].strip() else []
                intensidades = linhas[3].strip().split(",") if linhas[3].strip() else []

                exercicios   = linhas[4].strip().split(",") if linhas[4].strip() else []
                tempos       = linhas[5].strip().split(",") if linhas[5].strip() else []
                distancias   = linhas[6].strip().split(",") if linhas[6].strip() else []
                cargas       = linhas[7].strip().split(",") if linhas[7].strip() else []
                repeticoes   = linhas[8].strip().split(",") if linhas[8].strip() else []

                competicoes  = linhas[9].strip().split(",")  if linhas[9].strip()  else []
                locais       = linhas[10].strip().split(",") if linhas[10].strip() else []
                datas        = linhas[11].strip().split(",") if linhas[11].strip() else []
                categorias   = linhas[12].strip().split(",") if linhas[12].strip() else []
            else:
                print("Arquivo incompleto. Iniciando listas vazias.")
    else:
        print("Arquivo não encontrado. Iniciando listas vazias.")


def salvar_dados():
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        f.write(",".join(treinos)      + "\n")
        f.write(",".join(horarios)     + "\n")
        f.write(",".join(duracoes)     + "\n")
        f.write(",".join(intensidades) + "\n")

        f.write(",".join(exercicios)   + "\n")
        f.write(",".join(tempos)       + "\n")
        f.write(",".join(distancias)   + "\n")
        f.write(",".join(cargas)       + "\n")
        f.write(",".join(repeticoes)   + "\n")

        f.write(",".join(competicoes)  + "\n")
        f.write(",".join(locais)       + "\n")
        f.write(",".join(datas)        + "\n")
        f.write(",".join(categorias)   + "\n")