import pyttsx3

maquina = pyttsx3.init()

def ler_livro(livro):
    with open(livro, 'r') as f:
        for linha in f:
            maquina.say(linha)
            maquina.runAndWait()