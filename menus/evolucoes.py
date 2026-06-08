# evolucao.py
import os
import dados
from dados import treinos
from dados import exercicios
from dados import tempos
from dados import cargas

def extrair_numero(texto):
    numero = ""

    for caractere in texto:
        if caractere.isdigit() or caractere == ".":
            numero += caractere

    if numero:
        return float(numero)

def mostrar_evolucao():
        os.system("cls")
        print("===== ACOMPANHAMENTO DE EVOLUÇÃO =====\n")

        total_treinos = len([t for t in treinos if t])
        exercicios_validos = [
            i for i, e in enumerate(exercicios)
            if e and tempos[i] and cargas[i]
        ]

        print(f"Total de treinos cadastrados: {total_treinos}")

        if not exercicios_validos:
            print("\nNão há dados suficientes para análise de evolução.")
            input("\nPressione Enter para continuar...")
            return
        else:
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
                    return
    
                primeiro = indices[0]
                ultimo = indices[-1]
    
                print(f"Exercício: {nome_exercicio}")
    
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
