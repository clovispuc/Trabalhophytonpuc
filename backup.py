import shutil
import os
from datetime import datetime
import logging

def realizar_backup(origem, destino):
    """
    Copia arquivos da origem para o destino com timestamp.
    """
    logger = logging.getLogger() # Pega o logger configurado

    # Verifica se o diretório de origem existe (Simulação de falhas )
    if not os.path.exists(origem):
        logger.error(f"Diretório de origem não encontrado: {origem}")
        return False

    # Cria o diretório de destino se não existir
    if not os.path.exists(destino):
        try:
            os.makedirs(destino)
            logger.info(f"Diretório de destino criado: {destino}")
        except OSError as e:
            logger.error(f"Falha ao criar diretório destino: {e}")
            return False

    # Gera um timestamp para a pasta de backup (Bônus )
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    pasta_destino_final = os.path.join(destino, f"backup_{timestamp}")

    try:
        # Copia a árvore de diretórios inteira
        shutil.copytree(origem, pasta_destino_final)
        logger.info(f"Backup realizado com sucesso de '{origem}' para '{pasta_destino_final}'")
        return True
    except Exception as e:
        logger.error(f"Erro ao realizar backup: {e}")
        return False