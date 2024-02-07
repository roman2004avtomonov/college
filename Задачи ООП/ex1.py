import random


class MusicAlbum:
    def __init__(self, title, artist, release_year, genre, tracklist):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.tracklist = tracklist

    def play_random_track(self):
        if self.tracklist:
            random_track = random.choice(self.tracklist)
            print("Воспроизводится трек {}: {}".format(self.tracklist.index(random_track) + 1, random_track))
        else:
            print("В данном альбоме нет треков.")


album = MusicAlbum("Dark Side of the Moon", "Pink Floyd", 1973, "Progressive Rock",
                   ['Speak to Me', 'Breathe', 'On the Run', 'Time',
                    'The Great Gig in the Sky', 'Money', 'Us and Them',
                    'Any Colour You Like', 'Brain Damage', 'Eclipse'])
print("Название: ", album.title)
print("Исполнитель: ", album.artist)
print("Год: ", album.release_year)
print("Жанр: ", album.genre)
print("Треки: ", album.tracklist)

album.play_random_track()