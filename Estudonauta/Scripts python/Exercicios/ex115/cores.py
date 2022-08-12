def vermelho(msg=0):
    txt = str(f'\033[1;31m{msg}\033[0;0m')
    return txt


def azul(txt=0):
    txt = str(f'\033[1;34m{txt}\033[0;0m')
    return txt


def preto(txt=0):
    txt = str(f'\033[1;30m{txt}\033[0;0m')
    return txt


def amarelo(txt=0):
    txt = str(f'\033[1;33m{txt}\033[0;0m')
    return txt


def verde(txt=0):
    txt = str(f'\033[1;32m{txt}\033[0;0m')
    return txt


def branco(txt=0):
    txt = str(f'\033[1;97m{txt}\033[0;0m')
    return txt