# Ferramenta de Backup Automatizado para DevOps

Este projeto representa a entrega final da disciplina **Python para Automação em DevOps**, com o objetivo de desenvolver uma solução para a automação de rotinas de backup. A aplicação foi concebida para ser portátil, confiável e facilmente integrável em pipelines de CI/CD, utilizando conteinerização e testes unitários.

## Funcionalidades Principais

A ferramenta de backup foi desenvolvida com foco em automação e rastreabilidade:

| Funcionalidade | Descrição |
| :--- | :--- |
| **Automação de Backup** | Cópia completa de diretórios de origem para destino, utilizando a biblioteca padrão `shutil`. |
| **Versionamento** | Cada execução de backup cria uma nova pasta no destino com um *timestamp* (`backup_YYYYMMDD_HHMMSS`), garantindo a integridade de versões anteriores. |
| **Sistema de Logs** | Configuração centralizada de logs (via `logger.py`) que registra todas as operações e erros tanto no console quanto em um arquivo dedicado (`logs/backup.log`). |
| **Portabilidade com Docker** | O projeto é totalmente conteinerizado, permitindo sua execução em qualquer ambiente que suporte Docker, isolando dependências e garantindo a reprodutibilidade. |
| **Testes Unitários** | Cobertura de testes com `pytest` para validar a lógica de backup e o tratamento de erros (e.g., diretórios de origem inexistentes). |

## ️ Arquitetura do Projeto

O projeto segue uma arquitetura modular em Python, facilitando a manutenção e a expansão:

*   **`main.py`**: O ponto de entrada da aplicação. Ele orquestra o processo, valida os argumentos de linha de comando (`<origem>` e `<destino>`), configura o sistema de logs e invoca a função de backup.
*   **`backup.py`**: Contém a lógica de negócio principal. É responsável por verificar a existência dos diretórios, criar a pasta de destino com *timestamp* e executar a cópia dos arquivos.
*   **`logger.py`**: Módulo dedicado à configuração do `logging` do Python, garantindo que os logs sejam persistidos em arquivo e exibidos no console simultaneamente.
*   **`Dockerfile`**: Define o ambiente de execução, utilizando a imagem `python:3.9-slim` e configurando o `pytest` para o ambiente de testes.

## ️ Tecnologias Utilizadas

*   **Linguagem:** Python 3.9+
*   **Conteinerização:** Docker
*   **Testes:** Pytest
*   **Bibliotecas Padrão:** `shutil` (cópia de arquivos), `logging` (rastreamento de eventos), `sys` (argumentos de linha de comando).

##  Como Executar

### 1. Pré-requisitos

Para executar o projeto, você precisará ter o **Python 3.9+** e o **Docker** instalados em seu sistema.

### 2. Execução Local

O script principal requer dois argumentos de linha de comando: o caminho do diretório de origem e o caminho do diretório de destino.

```bash
# Exemplo de execução em sistemas baseados em Unix/Linux
python main.py /caminho/para/origem /caminho/para/destino

# Exemplo de execução no Windows PowerShell
python .\main.py C:\dados\origem C:\backups\destino
```

### 3. Execução com Docker (Recomendado)

A conteinerização garante que o ambiente de execução seja idêntico em qualquer máquina.

#### A. Construir a Imagem

Navegue até o diretório raiz do projeto e execute o comando de *build*:

```bash
docker build -t trabalhophytonpuc:latest .
```

#### B. Executar o Container

Para que o container possa acessar os diretórios do seu sistema operacional, é necessário montar volumes (`-v`). Recomenda-se montar o volume de origem como somente leitura (`:ro`) para evitar modificações acidentais.

```bash
# Exemplo de execução (ajuste os caminhos locais conforme necessário)
docker run --rm \
  -v "/caminho/local/origem:/app/origem:ro" \
  -v "/caminho/local/destino:/app/destino" \
  trabalhophytonpuc:latest /app/origem /app/destino
```

##  Testes Unitários

O projeto inclui testes unitários para garantir a qualidade e o comportamento esperado da aplicação em diferentes cenários, incluindo sucesso na cópia e tratamento de erros (e.g., diretório de origem inexistente).

### Executar Testes Localmente

Certifique-se de ter o `pytest` instalado (`pip install pytest`) e execute:

```bash
python -m pytest tests/
```

### Executar Testes via Docker

Você pode executar os testes dentro de um container, garantindo que o ambiente de teste seja isolado:

```bash
docker run --rm \
  -v "$(pwd):/app" \
  -w /app \
  python:3.9-slim \
  sh -c "pip install -q pytest && pytest tests -q"
```

---
