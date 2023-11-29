# Created By: Brendan (@AtlasDisease)
# Copyright: 2023
# Description: Music Package

# --- Imports --- #

try:
    from .artists import Artist
    from .songs import Song
    from .albums import Album, Playlist, Record
    from .genres import Genre
except:
    from artists import Artist
    from songs import Song
    from albums import Album, Playlist, Record
    from genres import Genre

    
# --- Testing --- #

if __name__ == "__main__":
    
    from dataclasses import asdict
    
    artist = Artist("Bob Wills & His Texas Playboys",
                    genre = Genre.COUNTRY)
    artist2 = Artist("AtlasDisease")
    song = Song("Faded Love", artist)
    album = Album("Tiffany Transcriptions Vol. 1",
                  artist,
                  songs = [song])
    playlist = Playlist("Swingin, Heartache, and Bob Wills Music",
                        artist2,
                        songs = [song])
    record = Record(**asdict(album))
    playlist2 = Playlist(**asdict(album))

    print(artist)
    print(song)
    print(album)
    print(playlist)
    print(record)
    print(playlist2)
    print(artist.genre)
