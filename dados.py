import os
import csv

ARQ_TREINOS      = "arquivos/treinos.csv"
ARQ_EXERCICIOS   = "arquivos/exercicios.csv"
ARQ_COMPETICOES  = "arquivos/competicoes.csv"

treinos      = []
horarios     = []
duracoes     = []
intensidades = []

exercicios   = []
tempos       = []
distancias   = []
cargas       = []
repeticoes   = []

competicoes  = []
locais       = []
datas        = []
categorias   = []


def carregar_dados():
    global treinos, horarios, duracoes, intensidades
    global exercicios, tempos, distancias, cargas, repeticoes
    global competicoes, locais, datas, categorias

    # ---- TREINOS ----
    if os.path.exists(ARQ_TREINOS):
        with open(ARQ_TREINOS, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                treinos.append(row.get("nome", ""))
                horarios.append(row.get("horario", ""))
                duracoes.append(row.get("duracao", ""))
                intensidades.append(row.get("intensidade", ""))
    else:
        print("Arquivo de treinos não encontrado. Iniciando vazio.")

    # ---- EXERCÍCIOS ----
    if os.path.exists(ARQ_EXERCICIOS):
        with open(ARQ_EXERCICIOS, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                exercicios.append(row.get("nome", ""))
                tempos.append(row.get("tempo", ""))
                distancias.append(row.get("distancia", ""))
                cargas.append(row.get("carga", ""))
                repeticoes.append(row.get("repeticoes", ""))
    else:
        print("Arquivo de exercícios não encontrado. Iniciando vazio.")

    # ---- COMPETIÇÕES ----
    if os.path.exists(ARQ_COMPETICOES):
        with open(ARQ_COMPETICOES, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                competicoes.append(row.get("nome", ""))
                datas.append(row.get("data", ""))
                locais.append(row.get("local", ""))
                categorias.append(row.get("categoria", ""))
    else:
        print("Arquivo de competições não encontrado. Iniciando vazio.")


def salvar_dados():
    # ---- TREINOS ----
    with open(ARQ_TREINOS, "w", newline="", encoding="utf-8") as f:
        campos = ["nome", "horario", "duracao", "intensidade"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for i in range(len(treinos)):
            if not treinos[i]:
                continue
            writer.writerow({
                "nome":        treinos[i],
                "horario":     horarios[i],
                "duracao":     duracoes[i],
                "intensidade": intensidades[i],
            })

    # ---- EXERCÍCIOS ----
    with open(ARQ_EXERCICIOS, "w", newline="", encoding="utf-8") as f:
        campos = ["nome", "tempo", "distancia", "carga", "repeticoes"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for i in range(len(exercicios)):
            if not exercicios[i]:
                continue
            writer.writerow({
                "nome":        exercicios[i],
                "tempo":       tempos[i],
                "distancia":   distancias[i],
                "carga":       cargas[i],
                "repeticoes":  repeticoes[i],
            })

    # ---- COMPETIÇÕES ----
    with open(ARQ_COMPETICOES, "w", newline="", encoding="utf-8") as f:
        campos = ["nome", "data", "local", "categoria"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for i in range(len(competicoes)):
            if not competicoes[i]:
                continue
            writer.writerow({
                "nome":       competicoes[i],
                "data":       datas[i],
                "local":      locais[i],
                "categoria":  categorias[i],
            })