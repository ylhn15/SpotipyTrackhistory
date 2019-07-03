class Track:
    def __init__(self, name="", artists="",album="", played_date="", external_url="", thumbnail=""):
        self.name = name
        self.artists = artists 
        self.album = album
        self.played_date = played_date
        self.external_url = external_url
        self.thumbnail = thumbnail
    def get_track_as_dict(self):
        track_as_dict = {"name" : self.name, "artists" : self.artists, "album" : self.album, "played_date" : self.played_date, "external_url": self.external_url, "thumbnail": self.thumbnail}
        return track_as_dict
