import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import pandas as pd

client_id = 'fa2c4041be384d88b4f345813f46b12f'
client_secret = 'a4ef1c55a42c4e1684576c35eeb7d602'


client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)





def df_playlist(playlist_id,playlist_name): #code de la playlist, nom voulu pour le fichier csv
    
    results = sp.user_playlist_tracks(client_id,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    results = tracks    

    playlist_tracks_id = []
    playlist_tracks_popularity = []

    for i in range(len(results)):
        #print(i) # Counter
        if i == 0:
            playlist_tracks_id = results[i]['track']['id']
            playlist_tracks_popularity = results[i]['track']['popularity']
            

            features = sp.audio_features(playlist_tracks_id)
            features_df = pd.DataFrame(data=features, columns=features[0].keys())
            features_df['popularity'] = playlist_tracks_popularity
            features_df = features_df[['popularity',
                                       'danceability', 'energy', 'key', 'loudness',
                                       'mode', 'acousticness', 'instrumentalness',
                                       'speechiness','liveness', 'valence', 'tempo',
                                       'duration_ms', 'time_signature']]
            continue
        else:
            try:
                playlist_tracks_id = results[i]['track']['id']
                playlist_tracks_titles = results[i]['track']['name']
                playlist_tracks_first_release_date = results[i]['track']['album']['release_date']
                playlist_tracks_popularity = results[i]['track']['popularity']

                features = sp.audio_features(playlist_tracks_id)
                new_row ={'popularity':[playlist_tracks_popularity],
                'danceability':[features[0]['danceability']],
                'energy':[features[0]['energy']],
                'key':[features[0]['key']],
                'loudness':[features[0]['loudness']],
                'mode':[features[0]['mode']],
                'acousticness':[features[0]['acousticness']],
                'instrumentalness':[features[0]['instrumentalness']],
                'speechiness':[features[0]['speechiness']],
                'liveness':[features[0]['liveness']],
                'valence':[features[0]['valence']],
                'tempo':[features[0]['tempo']],
                'duration_ms':[features[0]['duration_ms']],
                'time_signature':[features[0]['time_signature']]
                }

                dfs = [features_df, pd.DataFrame(new_row)]
                features_df = pd.concat(dfs, ignore_index = True)
            except:
                continue
    features_df['genre'] = playlist_name
    features_df.to_csv(f'{playlist_name}.csv',index=False)
    return 'Creation csv success'