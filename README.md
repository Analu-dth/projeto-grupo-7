# HYROX Planner

Um aplicativo em Python para gerenciar e organizar treinos de HYROX de forma simples e intuitiva.

## 📋 Descrição

O HYROX Planner é um programa de linha de comando que permite:
- ✅ Adicionar, visualizar, editar e excluir treinos padrão
- ✅ Gerenciar exercícios específicos do HYROX com controle de desempenho
- ✅ Planejar, editar e excluir competições com contagem regressiva
- ✅ Acompanhar evolução e progresso dos treinos
- ✅ Receber sugestões personalizadas de treinamento por nível
- ✅ Visualizar dados em tabelas formatadas
- ✅ Planejar semana de treinos com acompanhamento de RPE e humor

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

### 4. Acompanhamento de Evolução ✅
- **Análise de Progresso**: Visualize melhorias de tempo e aumento de carga nos exercícios
- **Comparação**: Acompanhe a evolução entre o primeiro e último registro de cada exercício
- **Indicadores de Desempenho**: Melhoras, estabilidade ou redução de desempenho

### 5. Sugestões de Treinamento ✅
- **Três Níveis**: Iniciante, Intermediário e Avançado
- **Treinos Personalizados**: Recomendações específicas para cada nível com:
  - Nome do treino
  - Descrição detalhada
  - Dias por semana
  - Foco do treinamento
  - Duração em minutos
  - Nível de intensidade

### 6. Planejador Semanal de Treinos ✅
- **Configurar Dias**: Defina treinos para cada dia da semana
- **Registro de Dados**: Anote data, treino realizado, RPE (1-10), humor e observações
- **Visualizar Semana**: Tabela formatada com todos os dados da semana
- **Editar Dias**: Modifique qualquer dia já configurado

## 📁 Estrutura do Projeto

```
projeto-grupo-7/
├── main.py                 # Arquivo principal com menu interativo
├── dados.py               # Gerenciamento de dados e persistência em CSV
├── README.md              # Esta documentação
├── .gitignore             # Configuração do Git
├── ORIGINAIS - ESQUEÇAM/  # Arquivos originais (backup)
├── menus/                 # Módulos de menu
│   ├── treinos.py         # Menu e funções de CRUD de treinos
│   ├── exercicios.py      # Menu e funções de gerenciamento de exercícios
│   ├── competicoes.py     # Menu e funções de planejamento de competições
│   ├── evolucoes.py       # Funções de acompanhamento de evolução ✅
│   ├── sugestoes.py       # Menu de sugestões de treinamento ✅
│   ├── extra.py           # Planejador semanal de treinos ✅
│   └── segredo.py         # Menu secreto com funcionalidades adicionais
└── arquivos/              # Armazenamento de dados
    ├── treinos.csv        # Dados de treinos
    ├── exercicios.csv     # Dados de exercícios
    ├── competicoes.csv    # Dados de competições
    ├── calendario.csv     # Dados do calendário semanal
    └── sugestoes.csv      # Dados de sugestões personalizadas
```

## 💾 Armazenamento de Dados

Os dados são salvos automaticamente em arquivos CSV no diretório `arquivos/`:
- **treinos.csv**: Treinos (nome, horário, duração, intensidade)
- **exercicios.csv**: Exercícios (nome, tempo, distância, carga, repetições)
- **competicoes.csv**: Competições (nome, data, local, categoria)
- **calendario.csv**: Dados semanais (data, peso, altura, treino)
- **sugestoes.csv**: Sugestões personalizadas por nível

Formato: Cada arquivo utiliza CSV com headers para fácil leitura e manutenção.

## 🛠️ Como Usar

### Instalação e Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/analu-dev/projeto-grupo-7.git
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
O programa oferece 7 opções principais:
- `1` - CRUD de Treinos
- `2` - Exercícios e Controle de Desempenho
- `3` - Planejamento de Competições
- `4` - Acompanhamento de Evolução ✅
- `5` - Sugestões de Treinamento ✅
- `6` - Planejador Semanal ✅
- `CS` - Menu Secreto (funcionalidades ocultas)
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

### Acompanhamento de Evolução (opção 4)
- Visualização automática de progresso em tempo e carga
- Comparação entre registros iniciais e finais
- Indicadores de melhora, estabilidade ou redução

### Sugestões de Treinamento (opção 5)
- `1` - Treinos para Iniciantes
- `2` - Treinos para Intermediários
- `3` - Treinos para Avançados
- Visualização de detalhes completos de cada sugestão

### Planejador Semanal (opção 6)
- `1` - Configurar um dia da semana
- `2` - Visualizar tabela semanal completa
- `3` - Editar um dia já configurado
- `0` - Voltar

## 📝 Requisitos

- Python 3.x
- Sistema operacional com suporte a comando `cls` (Windows) ou adaptação para Linux/Mac

## 🎯 Exemplos de Uso

- **Treino Padrão**: Corrida matinal com 45 minutos de duração, intensidade moderada
- **Exercício Específico**: Sled Push com 80kg, 100m de distância, 30 repetições
- **Competição**: HYROX São Paulo no dia 15/06/2024, categoria Elite
- **Evolução**: Acompanhe sua melhora do Sled Push de 15s inicialmente para 12s
- **Sugestão**: Treinamento intermediário com foco em resistência muscular
- **Planejamento Semanal**: Configure sua semana com RPE e humor diário

## ⚠️ Notas Técnicas

- O programa utiliza `os.system("cls")` para limpar a tela (compatível com Windows)
- Para Linux/Mac, pode ser necessário adaptar o comando para `clear`
- Validação de formato de data implementada (DD/MM/AAAA)
- Tratamento de erros para entradas inválidas
- Dados persistidos em CSV para fácil portabilidade
- Competições possuem contagem regressiva automática de dias até a data do evento
- Sistema de análise de evolução com extração de números de valores registrados
- Menu secreto acessível digitando "CS" no menu principal

## 👥 Contribuidores

Projeto desenvolvido por grupo de desenvolvimento.

---

Desenvolvido para otimizar o planejamento de treinos HYROX! 💪
