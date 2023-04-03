import speech_recognition as sr
import pyttsx3
import openai
import spotify
import key
from leitorLivros import ler_livro
from programas import abrir_programa
from spotify import comandos_spotify,continuar_musica_spotify,pausar_musica_spotify,pular_musica_spotify,tocar_musica_spotify

openai.api_key = key.key


audio = sr.Recognizer()
maquina = pyttsx3.init()


def comandos(): 
    with sr.Microphone() as source:
        maquina.say(' Teste iniciado')
        maquina.runAndWait()
    while True:
        
        with sr.Microphone() as source:
            
            
            voz = audio.listen(source,timeout=10)
            
        try:
            comando = audio.recognize_google(voz, language='pt-BR')
            print(" Você perguntou: " + comando)

            if "dormir" in comando:
                maquina.say(" Mais Já, Nem precisava ter me chamado!")
                maquina.runAndWait()
                break
            elif 'tocar música' in comando or 'pausar música' in comando or 'continuar música' in comando or 'playlist' in comando or 'pular música' in comando:
                spotify.comandos_spotify(comando)
            elif 'Abrir' in comando or 'abrir' in comando:
                programa = comando.replace('Abrir', '').strip()
                abrir_programa(programa)
            elif 'Ler livro' in comando:
                livro = comando.replace('ler livro', '').strip()
                ler_livro(livro)
            else:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=comando,
                    max_tokens=4000
                )

                resposta = response["choices"][0]["text"]
                print(" A responsta é: " + resposta)

                maquina.say(resposta)
                maquina.runAndWait()
        except sr.UnknownValueError:
            print(" Não consegui entender a pergunta")
        except sr.RequestError as e:
            print(" Não foi possivel completar a solicitação. Error: ".format(e))


comandos()
  