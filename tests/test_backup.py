import os
import pytest
from backup import realizar_backup
from logger import configurar_logger

# Configura o logger para os testes não quebrarem
configurar_logger()

def test_backup_diretorio_inexistente():
    """Testa se o sistema lida com origem inexistente """
    resultado = realizar_backup("pasta_que_nao_existe", "destino_qualquer")
    assert resultado is False

def test_backup_sucesso(tmp_path):
    """
    Testa um backup bem sucedido. 
    O tmp_path é um recurso do pytest que cria pastas temporárias.
    """
    # Cria pastas falsas para teste
    pasta_origem = tmp_path / "origem"
    pasta_origem.mkdir()
    arquivo = pasta_origem / "arquivo.txt"
    arquivo.write_text("conteudo teste")

    pasta_destino = tmp_path / "destino"
    
    # Executa a função
    resultado = realizar_backup(str(pasta_origem), str(pasta_destino))
    
    assert resultado is True
    # Verifica se algo foi criado no destino
    assert len(list(pasta_destino.iterdir())) > 0