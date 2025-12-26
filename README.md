Ferramenta de Backup Automatizado (Projeto DevOps)
Este projeto é uma solução em Python para a automação de backups, desenvolvida como atividade final para a disciplina de Python para Automação em DevOps. A aplicação foca na modularização, tratamento de erros, logs detalhados e portabilidade via Docker.



Arquitetura do Sistema
A aplicação foi dividida em módulos independentes para garantir a reutilização de código e facilidade de manutenção:



main.py: O script principal que orquestra a execução, integra os módulos e processa os argumentos de entrada via linha de comando (sys.argv).


backup.py: Contém a lógica de negócio para a cópia de diretórios. Implementa o bónus de versionamento através de pastas nomeadas com timestamp (ex: backup_20231216_120000).



logger.py: Centraliza a configuração de logs, permitindo o rastreio tanto no terminal como no ficheiro logs/backup.log.



tests/: Pasta dedicada a testes unitários automatizados utilizando o framework pytest.

Tecnologias Utilizadas

Python 3.9+.



Pytest: Para validação da qualidade e funcionalidade do código.



Docker: Para isolamento e garantia de que a aplicação corre em qualquer ambiente.


Logging: Biblioteca padrão para registos INFO e ERROR.


Como construir a imagem Docker do Projeto:
docker build -f ./Dockerfile -t trabalhophytonpuc:latest .

Como Executar o Projeto localmente no Windows:
python .\main.py c:\diretorio\origem c:\diretorio\destino

Como executar o projeto baseado em Docker:
 docker run --rm  -v "C:\diretorio\origem:/app/origem:ro"  -v "C:\diretorio\destino:/app/destino"  trabalhophytonpuc:latest /app/origem /app/destino

Qualidade e Testes
O projeto inclui testes unitários que cobrem os requisitos específicos:

Sucesso: Valida se os ficheiros são copiados corretamente para o destino.

Falha: Simula cenários de diretórios inexistentes e valida se o erro é tratado adequadamente.


Para executar os testes no seu ambiente Linux:

Bash

python3 -m pytest tests/

Demonstração de Resultados

Logs Gerados: Os registos são salvos automaticamente em logs/backup.log, contendo o timestamp e o status de cada operação.


Portabilidade: Graças ao Dockerfile, todas as dependências (como o pytest) são instaladas automaticamente dentro do container
