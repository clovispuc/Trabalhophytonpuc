# Usa uma imagem leve do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala o pytest (dependência) [cite: 39]
RUN pip install pytest

# Copia todos os arquivos do projeto para o container [cite: 39]
COPY . .

# Comando padrão ao iniciar o container. 
# Usamos ENTRYPOINT para permitir passar argumentos [cite: 41]
ENTRYPOINT ["python", "main.py"]