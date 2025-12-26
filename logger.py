import logging
import os

def configurar_logger(log_dir=None):
    """
    Configura o sistema de logs para salvar em arquivo e mostrar na tela.
    Se `log_dir` for fornecido, grava em `<log_dir>/logs/backup.log`.
    Garante que não haja handlers duplicados e que o arquivo seja criado.
    """
    # Determina o diretório de logs
    if log_dir:
        logs_path = os.path.join(log_dir, 'logs')
    else:
        logs_path = 'logs'

    os.makedirs(logs_path, exist_ok=True)

    root = logging.getLogger()
    # Remove handlers existentes para evitar duplicação e garantir comportamento determinístico
    for h in list(root.handlers):
        try:
            root.removeHandler(h)
            h.close()
        except Exception:
            pass

    # Configura handlers explícitos
    fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler(os.path.join(logs_path, 'backup.log'))
    fh.setFormatter(fmt)
    sh = logging.StreamHandler()
    sh.setFormatter(fmt)

    root.setLevel(logging.INFO)
    root.addHandler(fh)
    root.addHandler(sh)

    return root