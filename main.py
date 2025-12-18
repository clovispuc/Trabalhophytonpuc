import sys
from logger import configurar_logger
from backup import realizar_backup

def main():
    # 1. Configura o logger [cite: 21]
    logger = configurar_logger()
    logger.info("Iniciando processo de automação de backup...")

    # 2. Verifica se o usuário passou os argumentos (origem e destino)
    # Exemplo de uso: python main.py ./dados ./backups
    if len(sys.argv) != 3:
        logger.error("Uso incorreto. Tente: python main.py <origem> <destino>")
        sys.exit(1)

    diretorio_origem = sys.argv[1]
    diretorio_destino = sys.argv[2]

    # 3. Executa o backup [cite: 20]
    sucesso = realizar_backup(diretorio_origem, diretorio_destino)

    if sucesso:
        logger.info("Processo finalizado com sucesso.")
    else:
        logger.error("Processo finalizado com erros.")
        sys.exit(1)

if __name__ == "__main__":
    main()