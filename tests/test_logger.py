import logging
from pathlib import Path
import pytest
from logger import configurar_logger

@pytest.fixture(autouse=True)
def _isolate_logging():
    root = logging.getLogger()
    old_handlers = list(root.handlers)
    # remove existing handlers to isolate tests
    for h in list(root.handlers):
        root.removeHandler(h)
    try:
        yield
    finally:
        # close and remove handlers added during the test
        for h in list(root.handlers):
            try:
                h.flush()
                h.close()
            except Exception:
                pass
            root.removeHandler(h)
        # restore old handlers
        for h in old_handlers:
            root.addHandler(h)


def test_configurar_logger_cria_pasta_e_arquivo(tmp_path, monkeypatch):
    """Verifica que a pasta 'logs' é criada e que o arquivo contém a mensagem de log."""
    monkeypatch.chdir(tmp_path)
    logger = configurar_logger()

    logs_dir = tmp_path / 'logs'
    assert logs_dir.exists() and logs_dir.is_dir()

    logger.info('mensagem de teste')
    # força flush dos file handlers para garantir escrita
    for h in logger.handlers:
        if isinstance(h, logging.FileHandler):
            h.flush()

    content = (logs_dir / 'backup.log').read_text(encoding='utf-8')
    assert 'mensagem de teste' in content


def test_configurar_logger_nao_duplicar_handlers(tmp_path, monkeypatch):
    """Verifica que chamar configurar_logger várias vezes não adiciona handlers extras."""
    monkeypatch.chdir(tmp_path)

    # Conta handlers iniciais (pode haver handlers do pytest); garantimos que não aumente ao reconfigurar
    initial = len(logging.getLogger().handlers)

    configurar_logger()
    handlers = logging.getLogger().handlers
    assert any(isinstance(h, logging.FileHandler) for h in handlers)
    assert any(isinstance(h, logging.StreamHandler) for h in handlers)
    num = len(handlers)

    configurar_logger()
    assert len(logging.getLogger().handlers) == num
    # Número de handlers não deve ser menor que o inicial (reconfiguração não remove handlers além do necessário)
    assert num >= initial


def test_filehandler_usa_backup_log(tmp_path, monkeypatch):
    """Verifica que o FileHandler grava em 'backup.log'."""
    monkeypatch.chdir(tmp_path)
    configurar_logger()
    handlers = logging.getLogger().handlers
    file_handlers = [h for h in handlers if isinstance(h, logging.FileHandler)]
    assert file_handlers, 'Nenhum FileHandler encontrado'
    fh = file_handlers[0]
    assert Path(fh.baseFilename).name == 'backup.log'
