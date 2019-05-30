class Track:
    def __init__(self, name="", artists="",album="", played_date=""):
        self.name = name
        self.artists = artists 
        self.album = album
        self.played_date = played_date

    def get_track_as_dict(self):
        track_as_dict = {"name" : self.name, "artists" : self.artists, "album" : self.album, "played_date" : self.played_date}
        return track_as_dict