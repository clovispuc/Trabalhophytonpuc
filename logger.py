import logging
import os

def configurar_logger():
    """
    Configura o sistema de logs para salvar em arquivo e mostrar na tela.
    Garante que não haja handlers duplicados e que 'logs/backup.log' seja usado.
    """
    # Garante que a pasta logs existe
    if not os.path.exists('logs'):
        os.makedirs('logs')

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
    fh = logging.FileHandler("logs/backup.log")
    fh.setFormatter(fmt)
    sh = logging.StreamHandler()
    sh.setFormatter(fmt)

    root.setLevel(logging.INFO)
    root.addHandler(fh)
    root.addHandler(sh)

    return root