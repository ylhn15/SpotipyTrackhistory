import time
import urllib
import spotipy
import spotipy.util as util
import os
from Track import Track
import json
import datetime


name_of_current_track = ""

def get_spotify_connection():
    credentials_dict = {}
    with open('credentials.json') as credentials: 
        credentials_dict = json.load(credentials) 
    scope = 'user-read-currently-playing'
    username = credentials_dict['username']
    client_id = credentials_dict['client_id']
    client_secret = credentials_dict['client_secret']
    redirect_url = credentials_dict['redirect_url']
    
    token = util.prompt_for_user_token(username,scope,client_id=client_id,client_secret=client_secret,redirect_uri=redirect_url)
    spotify = spotipy.Spotify(auth=token)
    return spotify

def get_current_track():
    artists = []
    spotify = get_spotify_connection()
    now_playing = spotify.current_user_playing_track()
    if now_playing is not None: 
        track_name = now_playing['item']['name']
        if track_name == name_of_current_track:
            return None
        album_name = now_playing['item']['album']['name']
        temp_artists = now_playing['item']['artists']
        played_date = datetime.datetime.now()
        played_date = str(played_date)
        external_url = now_playing['item']['external_urls']['spotify']
        thumbnail = now_playing['item']['album']['images'][0]['url']
        print(played_date)
        for artist in temp_artists:
            artists.append(artist['name'])
        track = Track(name=track_name, artists= artists, album=album_name, played_date=played_date, external_url=external_url, thumbnail=thumbnail)
        track_as_dict = track.get_track_as_dict()
        return track_as_dict
    return None


def write_track_to_file():
    global name_of_current_track
    track_as_dict = get_current_track()
    exists = os.path.isfile('tracklist.json')
    if exists:
        if track_as_dict is not None:
            with open('tracklist.json') as tracklist:
                tracks = json.load(tracklist)
                tracks.append(track_as_dict)
                name_of_current_track = tracks[-1]['name']
            with open('tracklist.json', mode='w') as f:
                f.write(json.dumps(tracks, indent=2))
    else:
        with open('tracklist.json', mode='w') as f:
            json.dump([], f)

def init_name_of_current_track():
    global name_of_current_track
    exists = os.path.isfile('tracklist.json')
    if exists:
        with open('tracklist.json') as tracklist:
            tracks = json.load(tracklist)
            if len(tracks) > 0:
                name_of_current_track = tracks[-1]['name']

def main():
    init_name_of_current_track()
    while True:
        write_track_to_file()
        time.sleep(5)

if __name__ == "__main__":
    main()
