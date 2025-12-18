import logging
import os

def configurar_logger():
    """
    Configura o sistema de logs para salvar em arquivo e mostrar na tela.
    """
    # Garante que a pasta logs existe
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Configuração básica
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("logs/backup.log"), # Salva no arquivo [cite: 32]
            logging.StreamHandler()                 # Mostra no terminal
        ]
    )
    return logging.getLogger()