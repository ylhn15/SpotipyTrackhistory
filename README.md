# SpotipyTracklist
Create a tracklist from played tracks on Spotify with Spotipy.

Credentials are stored in credentials.json with the following format:
````
{
    "username" : "username",
    "client_id" : "client_id",
    "client_secret" : "client_secret",
    "redirect_url" : "redirect_url"
}
````

Tracks are saved into a JSON File in the following format:
````
[
  {
    "album": "name of the album", 
    "played_date": "2019-05-30 14:21:44.897898", 
    "name": "name of the track", 
    "artists": [
      "Artist 1", 
      "Artist 2",
      "..."
    ]
  }
]
````
