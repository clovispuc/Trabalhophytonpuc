# 📋 Relatório do Sistema - trabalhophytonpuc

**Data de geração:** 2025-12-26 (atualizado: testes executados em 2025-12-26) ✅

---

## 🏗️ 1. Arquitetura

- **Linguagem:** Python 3.9+
- **Estrutura principal:**
  - `main.py` — ponto de entrada; recebe **<origem> <destino>** e chama `backup.realizar_backup`.
  - `backup.py` — lógica para cópia de diretórios e versionamento em pasta com timestamp.
  - `logger.py` — configura logs (console + `logs/backup.log`).
  - `tests/` — testes unitários com `pytest`.
- **Docker:** existe um `Dockerfile` que define `WORKDIR /app`, usa `ENTRYPOINT ["python","main.py"]` e instala `pytest` na imagem.

---

## ▶️ 2. Como executar

### 🖥️ Local (Windows PowerShell)
- Instalar dependências (se aplicável):

```powershell
python -m pip install -U -r requirements.txt
```

- Executar a aplicação:

```powershell
python .\main.py C:\teste\a C:\teste\b
```

### 🐳 Docker (build + run)
- Build:

```bash
docker build -t trabalhophytonpuc:latest .
```

- Run (montando volumes; origem como leitura):

```powershell
docker run --rm -v "C:\teste\a":/app/origem:ro -v "C:\teste\b":/app/destino trabalhophytonpuc:latest /app/origem /app/destino
```

> 💡 Dica: use `:ro` no volume de origem para prevenir gravações acidentais.

---

## 🧪 3. Resultados dos testes

- **Status atual:** Todos os testes passaram.

**Saída do `pytest` (execução completa):**

```
.....
5 passed in 0.05s
```

### Como executar os testes
- Local (instalar `pytest` se necessário):

```bash
python -m pip install -U pytest
python -m pytest tests -q
```

- Via Docker (sem instalar localmente):

```powershell
docker run --rm -v "C:\Users\Emanuel\Documents\Projetos\Trabalhophytonpuc":/app -w /app python:3.9-slim sh -c "pip install -q pytest && pytest tests -q"
```

---

## 🔍 4. Observações importantes

- ✅ `tests/test_logger.py` contém testes que verificam criação da pasta `logs`, escrita no arquivo `logs/backup.log`, não-duplicação de handlers e que o `FileHandler` aponta para `backup.log`.
- ✅ `tests/test_backup.py` cobre casos de origem inexistente e backup bem-sucedido.
- 🔧 Corrigi `configurar_logger()` para reconfigurar handlers de forma determinística (remove handlers antigos e adiciona `FileHandler` + `StreamHandler`), resolvendo falhas anteriores nos testes.