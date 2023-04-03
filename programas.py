import os
import winshell

def abrir_programa(programa):
    try:
        programa = fr'C:\Users\Public\Desktop\{programa}.lnk'
        alvo = winshell.shortcut(programa).path
        os.startfile(alvo)
    except Exception as e:
        print(f'Não foi possível abrir o programa {programa}. Erro: {e}')