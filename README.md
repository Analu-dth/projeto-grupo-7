# HYROX Planner

Um aplicativo em Python para gerenciar e organizar treinos de HYROX de forma simples e intuitiva.

## 📋 Descrição

O HYROX Planner é um programa de linha de comando que permite:
- ✅ Adicionar, visualizar, editar e excluir treinos padrão
- 🏋️ Gerenciar exercícios específicos do HYROX com controle de desempenho
- 🏁 Planejar, editar e excluir competições com contagem regressiva
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

### 3. Planejamento de Competições
- **Cadastrar Competição**: Informe nome, data (DD/MM/AAAA), local e categoria
- **Visualizar Competições**: Tabela com informações das competições, datas e contagem regressiva de dias
- **Editar Competição**: Modifique nome, data, local e categoria
- **Excluir Competição**: Remova competições do sistema

### 4. Acompanhamento de Evolução
- ⚙️ **Em Construção**: Funcionalidade para acompanhar progressos ao longo do tempo

### 5. Sugestões de Treinamento
- ⚙️ **Em Construção**: Recomendações personalizadas para otimizar seus treinos

### 6. Funções Extras
- ⚙️ **Em Construção**: Recursos adicionais para complementar sua experiência

## 📁 Estrutura do Projeto

```
projeto-grupo-7/
├── main.py                 # Arquivo principal com menu interativo
├── dados.py               # Gerenciamento de dados e persistência em CSV
├── README.md              # Esta documentação
├── .gitignore             # Configuração do Git
├── ORIGINAIS/             # Arquivos originais (backup)
├── menus/                 # Módulos de menu
│   ├── treinos.py         # Menu e funções de CRUD de treinos
│   ├── exercicios.py      # Menu e funções de gerenciamento de exercícios
│   ├── competicoes.py     # Menu e funções de planejamento de competições
│   ├── evolucoes.py       # Funções de acompanhamento de evolução (em construção)
│   ├── sugestoes.py       # Menu de sugestões de treinamento (em construção)
│   └── extra.py           # Funções extras (em construção)
└── arquivos/              # Armazenamento de dados
    ├── treinos.csv        # Dados de treinos
    ├── exercicios.csv     # Dados de exercícios
    └── competicoes.csv    # Dados de competições
```

## 💾 Armazenamento de Dados

Os dados são salvos automaticamente em arquivos CSV no diretório `arquivos/`:
- **treinos.csv**: Treinos (nome, horário, duração, intensidade)
- **exercicios.csv**: Exercícios (nome, tempo, distância, carga, repetições)
- **competicoes.csv**: Competições (nome, data, local, categoria)

Formato: Cada arquivo utiliza CSV com headers para fácil leitura e manutenção.

## 🛠️ Como Usar

### Instalação e Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/Analu-dth/projeto-grupo-7.git
   cd projeto-grupo-7
   ```

2. Crie o diretório de arquivos (se não existir):
   ```bash
   mkdir -p arquivos
   ```

3. Execute o programa:
   ```bash
   python main.py
   ```

### Menu Principal
O programa oferece 6 opções principais:
- `1` - CRUD de Treinos
- `2` - Exercícios e Controle de Desempenho
- `3` - Planejamento de Competições
- `4` - Acompanhamento de Evolução *(em construção)*
- `5` - Sugestões de Treinamento *(em construção)*
- `6` - Função Extra *(em construção)*
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
- `3` - Editar Competição
- `4` - Excluir Competição
- `0` - Voltar

## 📝 Requisitos

- Python 3.x
- Sistema operacional com suporte a comando `cls` (Windows) ou adaptação para Linux/Mac

## 🎯 Exemplos de Uso

- **Treino Padrão**: Corrida matinal com 45 minutos de duração, intensidade moderada
- **Exercício Específico**: Sled Push com 80kg, 100m de distância, 30 repetições
- **Competição**: HYROX São Paulo no dia 15/06/2024, categoria Elite

## ⚠️ Notas Técnicas

- O programa utiliza `os.system("cls")` para limpar a tela (compatível com Windows)
- Para Linux/Mac, pode ser necessário adaptar o comando para `clear`
- Validação de formato de data implementada (DD/MM/AAAA)
- Tratamento de erros para entradas inválidas
- Dados persistidos em CSV para fácil portabilidade
- Competições possuem contagem regressiva automática de dias até a data do evento

## 👥 Contribuidores

Projeto desenvolvido por grupo de desenvolvimento.

---

Desenvolvido para otimizar o planejamento de treinos HYROX! 💪
