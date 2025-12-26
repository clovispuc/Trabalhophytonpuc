import sys
from logger import configurar_logger
from backup import realizar_backup

def main():
    # 1. Verifica se o usuário passou os argumentos (origem e destino)
    # Exemplo de uso: python main.py ./dados ./backups
    if len(sys.argv) != 3:
        print("Uso incorreto. Tente: python main.py <origem> <destino>", file=sys.stderr)
        sys.exit(1)

    diretorio_origem = sys.argv[1]
    diretorio_destino = sys.argv[2]

    # 2. Configura o logger apontando para a pasta destino
    logger = configurar_logger(diretorio_destino)
    logger.info("Iniciando processo de automação de backup...")

    # 3. Executa o backup [cite: 20]
    sucesso = realizar_backup(diretorio_origem, diretorio_destino)

    if sucesso:
        logger.info("Processo finalizado com sucesso.")
    else:
        logger.error("Processo finalizado com erros.")
        sys.exit(1)

if __name__ == "__main__":
    main()