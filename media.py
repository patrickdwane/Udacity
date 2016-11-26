"""
this module contains the Song class that will be used in the
entertainment_center.py file
"""


class Song():

    """
    Song object is initialized below.
    position:
        needs to be the published position of the song on the the Official UK Top 40 Singles Chart
    title:
        should be the song title as seen on the Official UK Top 40 Singles Chart
    artist:
        should be the artist name as listed on the Official UK Top 40 Singles Chart
    track_image
        should be the art associated with the song
    video:
        needs to be the youtube link to watch the music video
    new_entry:
        must be set to "New Entry this Week!" if True else False
    favourite:
        if the song is a recommedned favourite, favourite value should be boolean True,
        else False
    favourtite_icon:
        should be set to a null object value. this will be overwritten in the
        fresh_tomatoes.py file module based on the favourite boolean value and
        will display the "recommended" logo next to the position attribute.
    """
    def __init__(self, position, title, artist, track_image, video, new_entry, favourite, favourite_icon):
        self.position = position
        self.title = title
        self.artist = artist
        self.track_image = track_image
        self.video_url = video
        self.new_entry = new_entry
        self.favourite = favourite
        self.favourite_icon = favourite_icon