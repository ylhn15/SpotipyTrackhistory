# SpotipyTracklist
## Description
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
    ],
    "external_url": "open://spotify/path-to-track"
  }
]
````
## Explanation

The main reason behind this project is to get more familiar with different techniques in software development, for example using a third party API (in this case Spotify) to read data and parse it into an usable format. Hosting the read data in a docker container and access said docker container from different applications.

Additionally to the backend I started to write different frontend - applications to access the data in a more human readable way.
[Browser based JavaScript](https://github.com/ylhn15/SpotipyTracklist_Frontend)
[iOS Application written in Swift](https://github.com/ylhn15/Spotipy_Tracklist_iOS)
[Progressive Web Ap written in Flutter](https://github.com/ylhn15/SpotipyTrackList-Flutter)
 
## Next up
- [ ] Rewrite backend in Go
- [ ] Add search function
- [ ] Improve usability of the iOS Application
- [ ] Add dummy data for every frontend - application
