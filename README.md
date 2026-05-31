# HYROX Planner

Um aplicativo em Python para gerenciar e organizar treinos de HYROX de forma simples e intuitiva.

## 📋 Descrição

O HYROX Planner é um programa de linha de comando que permite:
- ✅ Adicionar, visualizar, editar e excluir treinos padrão
- 🏋️ Gerenciar exercícios específicos do HYROX com controle de desempenho
- 🏁 Planejar e acompanhar competições
- 📊 Visualizar dados em tabelas formatadas

## 🚀 Funcionalidades

### 1. CRUD de Treinos
- **Adicionar treino**: Registre nome, duração, horário e intensidade
- **Visualizar treinos**: Tabelas formatadas mostrando todos os treinos cadastrados
- **Editar treinos**: Modifique informações de treinos existentes
- **Excluir treinos**: Remova treinos do sistema

### 2. Exercícios e Controle de Desempenho
Gerencie os exercícios específicos do HYROX:
- **Sled Push**: Registre tempo, distância, carga e repetições
- **Sled Pull**: Controle de carga e repetições
- **Burpee Broad Jumps**: Acompanhe distância e repetições
- **Wall Balls**: Monitore tempo e carga
- **Farmer's Carry**: Registre distância e carga

Funcionalidades:
- Adicionar novos exercícios
- Visualizar exercícios em tabela formatada
- Editar dados de exercícios
- Excluir exercícios

### 3. Planejamento de Competições (Em Construção)
- **Cadastrar Competição**: Informe nome, data (DD/MM/AAAA), local e categoria
- **Visualizar Competições**: Tabela com informações das competições e contagem regressiva de dias

## 💾 Armazenamento de Dados

Os dados são salvos automaticamente em um arquivo `hyroox_planner_dados.txt` em formato de texto estruturado, com as seguintes seções:
- Treinos (nome, horário, duração, intensidade)
- Exercícios (nome, tempo, distância, carga, repetições)
- Competições (nome, data, local, categoria)

## 🛠️ Como Usar

1. Execute o programa:
   ```bash
   python hyrox-tabelasep.py
   ```

2. Escolha uma opção no menu principal:
   - `1` - CRUD de Treinos
   - `2` - Exercícios e Controle de Desempenho
   - `3` - Planejamento de Competições
   - `0` - Sair

### Menu de Treinos (opção 1)
   - `1` - Adicionar treino
   - `2` - Visualizar treinos
   - `3` - Editar treino
   - `4` - Excluir treino
   - `0` - Voltar

### Menu de Exercícios (opção 2)
   - `1` - Adicionar exercício
   - `2` - Visualizar exercícios
   - `3` - Editar exercício
   - `4` - Excluir exercício
   - `0` - Voltar

### Menu de Competições (opção 3)
   - `1` - Cadastrar Competição
   - `2` - Visualizar Competições
   - `0` - Voltar

## 📝 Requisitos

- Python 3.x
- Sistema operacional com suporte a comando `cls` (Windows) ou adaptação para Linux/Mac

## 🎯 Exemplos de Uso

- **Treino Padrão**: Corrida matinal com 45 minutos de duração, intensidade moderada
- **Exercício Específico**: Sled Push com 80kg, 100m de distância, 30 repetições
- **Competição**: HYROX São Paulo no dia 15/06/2024, categoria Elite

## ⚠️ Notas

- O programa utiliza `os.system("cls")` para limpar a tela (compatível com Windows)
- Para Linux/Mac, pode ser necessário adaptar o comando para `clear`
- Validação de formato de data implementada (DD/MM/AAAA)
- Tratamento de erros para entradas inválidas

---

Desenvolvido para otimizar o planejamento de treinos HYROX! 💪
