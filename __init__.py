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

    import sys
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

    print(artist, f"{sys.getsizeof(artist)} b")
    print(song, f"{sys.getsizeof(song)} b")
    print(album, f"{sys.getsizeof(album)} b")
    print(playlist, f"{sys.getsizeof(playlist)} b")
    print(record, f"{sys.getsizeof(record)} b")
    print(playlist2, f"{sys.getsizeof(playlist2)} b")
    print(artist.genre)
