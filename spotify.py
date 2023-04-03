from spotipy.oauth2 import SpotifyOAuth
import spotipy

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id = 'e93a05c09fc3425ab0fbd54f57df2169',
        client_secret = 'e50fd824d7a14c7ba9860d3227e2f2d9',
        redirect_uri = 'http://localhost:8000',
        scope='user-library-read user-read-playback-state user-modify-playback-state',
        cache_path='.spotifycache'
    )
)
def tocar_musica_spotify(search_query):
    results = spotify.search(q=search_query, type='track', limit=1)
    items = results['tracks']['items']
    if len(items) > 0:
        track_uri = items[0]['uri']
        spotify.start_playback(uris=[track_uri])
    else:
        print('Música não encontrada')

def pausar_musica_spotify():
    spotify.pause_playback()

def continuar_musica_spotify():
    spotify.start_playback()

def pular_musica_spotify():
    spotify.next_track()

def tocar_playlist_spotify(search_query): 
    results = spotify.search(q=search_query, type='playlist', limit=1)
    items = results['playlists']['items']
    if len(items) > 0:
        playlist_uri = items[0]['uri']
        spotify.start_playback(context_uri=playlist_uri)
    


def comandos_spotify(comando):
    if 'tocar música' in comando:
        search_query = comando.replace('tocar música', '')
        tocar_musica_spotify(search_query)
    elif 'playlist' in comando:
        search_query = comando.replace('playlist', '')
        tocar_playlist_spotify(search_query)
    elif 'pausar música' in comando:
        pausar_musica_spotify()
    elif 'continuar música' in comando:
        continuar_musica_spotify()
    elif 'pular música' in comando:
        pular_musica_spotify()
    else:
        print('Comando não reconhecido')